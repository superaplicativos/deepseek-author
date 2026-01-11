#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Coleta palavras-chave mais buscadas (sugestões de busca) para compra de livros
em toda Amazon, por marketplace, usando o endpoint de sugestões.

Estratégia:
- Usa seeds por idioma para alto intento de compra de livros.
- Consulta /search/suggestions em cada domínio com alias stripbooks e digital-text.
- Agrega resultados por mercado e estima um índice via Google Trends.
- Salva CSV em relatorio_growth/amazon_keywords_top_global.csv
"""

import os
import csv
import time
import json
from pathlib import Path
from typing import Dict, List, Tuple

import requests
from pytrends.request import TrendReq

# Mapas simplificados de marketplaces (domínio, país, linguagem e geo do Google Trends)
MARKETS = [
    {"country":"Estados Unidos","domain":"www.amazon.com","lang":"en_US","geo":"US"},
    {"country":"Reino Unido","domain":"www.amazon.co.uk","lang":"en_US","geo":"GB"},
    {"country":"Alemanha","domain":"www.amazon.de","lang":"de_DE","geo":"DE"},
    {"country":"França","domain":"www.amazon.fr","lang":"fr_FR","geo":"FR"},
    {"country":"Itália","domain":"www.amazon.it","lang":"it_IT","geo":"IT"},
    {"country":"Espanha","domain":"www.amazon.es","lang":"es_ES","geo":"ES"},
    {"country":"Países Baixos","domain":"www.amazon.nl","lang":"nl_NL","geo":"NL"},
    {"country":"Bélgica","domain":"www.amazon.be","lang":"nl_NL","geo":"BE"},
    {"country":"Suécia","domain":"www.amazon.se","lang":"sv_SE","geo":"SE"},
    {"country":"Polônia","domain":"www.amazon.pl","lang":"pl_PL","geo":"PL"},
    {"country":"Turquia","domain":"www.amazon.com.tr","lang":"tr_TR","geo":"TR"},
    {"country":"Emirados Árabes","domain":"www.amazon.ae","lang":"ar_AE","geo":"AE"},
    {"country":"Arábia Saudita","domain":"www.amazon.sa","lang":"ar_SA","geo":"SA"},
    {"country":"Egito","domain":"www.amazon.eg","lang":"ar_EG","geo":"EG"},
    {"country":"Japão","domain":"www.amazon.co.jp","lang":"ja_JP","geo":"JP"},
    {"country":"Índia","domain":"www.amazon.in","lang":"en_IN","geo":"IN"},
    {"country":"Austrália","domain":"www.amazon.com.au","lang":"en_AU","geo":"AU"},
    {"country":"Singapura","domain":"www.amazon.sg","lang":"en_SG","geo":"SG"},
    {"country":"Canadá","domain":"www.amazon.ca","lang":"en_CA","geo":"CA"},
    {"country":"México","domain":"www.amazon.com.mx","lang":"es_MX","geo":"MX"},
    {"country":"Brasil","domain":"www.amazon.com.br","lang":"pt_BR","geo":"BR"},
]

# Seeds por idioma com alto intento de compra de livros
BOOK_SEEDS: Dict[str, List[str]] = {
    "en_US": ["books","novel","romance","thriller","fantasy","science fiction","children books","coloring book","activity book","word search","sudoku","cookbook","self help","journal","workbook"],
    "es_ES": ["libros","novela","romance","thriller","fantasía","ciencia ficción","libros infantiles","libro para colorear","libro de actividades","sopa de letras","sudoku","libro de cocina","autoayuda","diario","cuaderno de ejercicios"],
    "pt_BR": ["livros","romance","thriller","fantasia","ficção científica","livros infantis","livro de colorir","livro de atividades","caça-palavras","sudoku","livro de receitas","autoajuda","diário","caderno de exercícios"],
    "fr_FR": ["livres","roman","romance","thriller","fantasy","science-fiction","livres enfants","livre de coloriage","livre d’activités","mots mêlés","sudoku","livre de cuisine","développement personnel","journal","cahier d’exercices"],
    "it_IT": ["libri","romanzo","rosa","thriller","fantasy","fantascienza","libri per bambini","libro da colorare","libro di attività","cruciverba","sudoku","libro di cucina","autoaiuto","diario","quaderno di esercizi"],
    "de_DE": ["bücher","roman","liebesroman","thriller","fantasy","science fiction","kinderbücher","malbuch","aktivitätsbuch","wortsuche","sudoku","kochbuch","ratgeber","tagebuch","arbeitsbuch"],
    "nl_NL": ["boeken","roman","thriller","fantasy","sciencefiction","kinderboeken","kleurboek","activiteitenboek","woordzoeker","sudoku","kookboek","zelfhulp","dagboek","werkboek"],
    "sv_SE": ["böcker","roman","thriller","fantasy","science fiction","barnböcker","målarbok","aktivitetsbok","korsord","sudoku","kokbok","självhjälp","dagbok","arbetsbok"],
    "pl_PL": ["książki","powieść","romans","thriller","fantastyka","science fiction","książki dla dzieci","kolorowanka","książka aktywności","krzyżówka","sudoku","książka kucharska","poradnik","dziennik","zeszyt ćwiczeń"],
    "tr_TR": ["kitaplar","roman","aşk romanı","gerilim","fantastik","bilimkurgu","çocuk kitapları","boyama kitabı","aktivite kitabı","bulmaca","sudoku","yemek kitabı","kişisel gelişim","günlük","çalışma kitabı"],
    "ar_AE": ["كتب","رواية","رومانسية","تشويق","فانتازيا","خيال علمي","كتب أطفال","كتاب تلوين","كتاب نشاط","كلمات متقاطعة","سودوكو","كتاب طبخ","تطوير الذات","مفكرة","كتاب تمارين"],
    "ja_JP": ["本","小説","恋愛小説","ミステリー","ファンタジー","SF","子供向け本","塗り絵","アクティビティブック","クロスワード","数独","料理本","自己啓発","日記","ワークブック"],
    # idiomas en_* fallback
    "en_IN": ["books","novel","romance","thriller","fantasy","science fiction","children books","coloring book","activity book","word search","sudoku","cookbook","self help","journal","workbook"],
    "en_AU": ["books","novel","romance","thriller","fantasy","science fiction","children books","coloring book","activity book","word search","sudoku","cookbook","self help","journal","workbook"],
    "en_SG": ["books","novel","romance","thriller","fantasy","science fiction","children books","coloring book","activity book","word search","sudoku","cookbook","self help","journal","workbook"],
    "en_CA": ["books","novel","romance","thriller","fantasy","science fiction","children books","coloring book","activity book","word search","sudoku","cookbook","self help","journal","workbook"],
}

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/118.0 Safari/537.36"
)

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": UA,
    "Accept": "application/json, text/plain, */*",
})


def fetch_suggestions(domain: str, prefix: str, alias: str) -> List[str]:
    """Busca sugestões da Amazon para um prefixo e alias (stripbooks/digital-text)."""
    url = f"https://{domain}/search/suggestions"
    params = {
        "limit": "20",
        "prefix": prefix,
        "suggestion-type": "KEYWORD",
        "client-id": "amazon-search-ui",
        "search-alias": alias,
    }
    headers = {
        "Referer": f"https://{domain}/s?k={prefix}&i={alias}",
        "Accept": "application/json",
    }
    try:
        r = SESSION.get(url, params=params, headers=headers, timeout=10)
        r.raise_for_status()
        data = r.json()
        suggestions = [s.get("value", "").strip() for s in data.get("suggestions", [])]
        return [s for s in suggestions if s]
    except Exception:
        return []


def estimate_trends_volume(term: str, geo: str) -> float:
    """Obtém um índice de interesse do Google Trends para o termo no país (geo)."""
    try:
        py = TrendReq(hl="en-US", tz=360)
        py.build_payload([term], timeframe="today 12-m", geo=geo)
        df = py.interest_over_time()
        if df is None or df.empty:
            return 0.0
        # média dos últimos 8 valores como proxy
        vals = df[term].dropna().tolist()[-8:]
        if not vals:
            return 0.0
        return float(sum(vals) / len(vals))
    except Exception:
        return 0.0


def collect_market_keywords(market: Dict) -> List[Dict]:
    domain = market["domain"]
    country = market["country"]
    lang = market["lang"]
    geo = market["geo"]
    seeds = BOOK_SEEDS.get(lang, BOOK_SEEDS.get("en_US", []))

    aggregated: Dict[str, Dict] = {}

    for seed in seeds:
        # stripbooks
        s1 = fetch_suggestions(domain, seed, alias="stripbooks")
        # digital-text (Kindle)
        s2 = fetch_suggestions(domain, seed, alias="digital-text")
        all_sugs = s1 + s2
        for sug in all_sugs:
            item = aggregated.get(sug)
            if not item:
                aggregated[sug] = {
                    "keyword": sug,
                    "freq_seed_hits": 1,
                    "source_aliases": set(["stripbooks" if sug in s1 else "digital-text"]),
                }
            else:
                item["freq_seed_hits"] += 1
                if sug in s1:
                    item["source_aliases"].add("stripbooks")
                if sug in s2:
                    item["source_aliases"].add("digital-text")
        time.sleep(0.2)  # evitar limitar

    # calcular trends
    results: List[Dict] = []
    for sug, meta in aggregated.items():
        vol = estimate_trends_volume(sug, geo)
        score = meta["freq_seed_hits"] * (1.0 + vol / 100.0)
        results.append({
            "marketplace": domain,
            "pais": country,
            "idioma": lang,
            "keyword": sug,
            "freq_seed_hits": meta["freq_seed_hits"],
            "aliases": ",".join(sorted(list(meta["source_aliases"]))),
            "trends_volume_index": round(vol, 2),
            "score_composite": round(score, 3),
        })

    # ordenar
    results.sort(key=lambda x: (x["score_composite"], x["trends_volume_index"], x["freq_seed_hits"]), reverse=True)
    # top N por mercado
    top_n = int(os.getenv("TOP_N_PER_MARKET", "50"))
    return results[:top_n]


def main():
    base = Path('.')
    out_dir = base / 'relatorio_growth'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / 'amazon_keywords_top_global.csv'

    all_rows: List[Dict] = []
    for mk in MARKETS:
        rows = collect_market_keywords(mk)
        all_rows.extend(rows)
        print(f"Coletados {len(rows)} termos — {mk['country']} ({mk['domain']})")

    # salvar
    fieldnames = ["marketplace","pais","idioma","keyword","freq_seed_hits","aliases","trends_volume_index","score_composite"]
    with open(out_csv, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in all_rows:
            w.writerow(r)

    print(f"✅ CSV global salvo em: {out_csv}")


if __name__ == '__main__':
    main()