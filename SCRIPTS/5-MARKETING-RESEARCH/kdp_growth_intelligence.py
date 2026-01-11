#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KDP Growth Intelligence - MVP
Coleta volumes no Google Trends e faz scraping leve da Amazon Kindle
para ranquear nichos por país/idioma com base em volume, competição e proxy de vendas.

Saídas:
- ./relatorio_growth/ranking_top_50_nichos.csv
- ./relatorio_growth/insights_por_idioma.json
- ./relatorio_growth/keywords_otimizadas.json
- ./relatorio_growth/recomendacoes_praticas.txt
"""

import os
import re
import json
import time
import math
import logging
from pathlib import Path
from typing import List, Dict, Any

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pytrends.request import TrendReq

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("KDPGrowth")

# Configuração (inspirada em aligner/NEW/dir.txt)
CONFIG = {
    "idiomas_alvo": ["pt_BR", "en_US", "es_MX", "es_ES"],
    "mercados": [
        {"nome": "Brasil", "dominio": "amazon.com.br", "geo": "BR"},
        {"nome": "EUA", "dominio": "amazon.com", "geo": "US"},
        {"nome": "Canadá", "dominio": "amazon.ca", "geo": "CA"},
        {"nome": "México", "dominio": "amazon.com.mx", "geo": "MX"},
        {"nome": "Reino Unido", "dominio": "amazon.co.uk", "geo": "GB"},
        {"nome": "Alemanha", "dominio": "amazon.de", "geo": "DE"},
        {"nome": "França", "dominio": "amazon.fr", "geo": "FR"},
        {"nome": "Itália", "dominio": "amazon.it", "geo": "IT"},
        {"nome": "Espanha", "dominio": "amazon.es", "geo": "ES"},
        {"nome": "Holanda", "dominio": "amazon.nl", "geo": "NL"},
        {"nome": "Bélgica", "dominio": "amazon.be", "geo": "BE"},
        {"nome": "Suécia", "dominio": "amazon.se", "geo": "SE"},
        {"nome": "Polônia", "dominio": "amazon.pl", "geo": "PL"},
        {"nome": "Turquia", "dominio": "amazon.com.tr", "geo": "TR"},
        {"nome": "Emirados Árabes Unidos", "dominio": "amazon.ae", "geo": "AE"},
        {"nome": "Arábia Saudita", "dominio": "amazon.sa", "geo": "SA"},
        {"nome": "Egito", "dominio": "amazon.eg", "geo": "EG"},
        {"nome": "Japão", "dominio": "amazon.co.jp", "geo": "JP"},
        {"nome": "Índia", "dominio": "amazon.in", "geo": "IN"},
        {"nome": "Austrália", "dominio": "amazon.com.au", "geo": "AU"},
        {"nome": "Singapura", "dominio": "amazon.sg", "geo": "SG"},
    ],
    "max_keywords": 40,
    "asins_por_keyword": 10,
    "limite_competicao_maxima": 0.65,
}

# Seeds por idioma (combinações simples para MVP)
SEEDS = {
    "en_US": [
        "cozy mystery short", "romance short read", "word search large print",
        "coloring book adult", "activity book kids", "gratitude journal women"
    ],
    "pt_BR": [
        "livro de atividades para crianças", "palavras cruzadas adultos", "romance curto",
        "livro para colorir adultos", "mistério aconchegante", "diário de gratidão"
    ],
    "es_MX": [
        "libro actividades niños", "romance lectura corta", "sopa de letras adultos",
        "libro para colorear adultos", "misterio acogedor", "diario gratitud mujeres"
    ],
    "es_ES": [
        "libro actividades niños", "romance lectura corta", "sopa de letras adultos",
        "libro para colorear adultos", "misterio acogedor", "diario gratitud"
    ],
}

# Helpers
SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
})

pytrends = TrendReq(hl='en-US', tz=360)

def generate_keywords(idioma: str, max_keywords: int) -> List[str]:
    seeds = SEEDS.get(idioma, [])
    base = []
    # Gerar combinações simples com termos de alta conversão
    suffixes = [" for kids", " for women", " kindle", " ebook", " 2025"] if idioma == "en_US" else [" para crianças", " para mulheres", " kindle", " ebook", " 2025"]
    for s in seeds:
        base.append(s)
        for suf in suffixes:
            base.append(f"{s}{suf}")
    # Normalização simples
    base = [re.sub(r"\s+", " ", k).strip() for k in base]
    # Limitar
    uniq = []
    seen = set()
    for k in base:
        if k.lower() not in seen:
            uniq.append(k)
            seen.add(k.lower())
        if len(uniq) >= max_keywords:
            break
    return uniq

def get_trends_volume(keyword: str, geo: str) -> float:
    try:
        pytrends.build_payload([keyword], timeframe='today 12-m', geo=geo)
        df = pytrends.interest_over_time()
        if df is None or df.empty or keyword not in df.columns:
            return 0.0
        # média como proxy de volume
        return float(df[keyword].mean())
    except Exception as e:
        logger.debug(f"Trends falhou para '{keyword}'/{geo}: {e}")
        return 0.0

def scrape_amazon_search(keyword: str, dominio: str, limit: int = 10) -> List[Dict[str, Any]]:
    # Focar em Kindle (digital-text)
    url = f"https://{dominio}/s?k={requests.utils.quote(keyword)}&i=digital-text"
    items = []
    try:
        resp = SESSION.get(url, timeout=20)
        if resp.status_code != 200:
            return items
        soup = BeautifulSoup(resp.text, 'html.parser')
        results = soup.select('div.s-result-item[data-component-type="s-search-result"]')
        for r in results[:limit]:
            title_el = r.select_one('h2 a span')
            link_el = r.select_one('h2 a')
            price_whole = r.select_one('span.a-price-whole')
            rating_el = r.select_one('span.a-icon-alt')
            reviews_el = r.select_one('span[aria-label$="ratings"]') or r.select_one('span[aria-label$="ratings"]')
            title = title_el.text.strip() if title_el else None
            link = f"https://{dominio}" + link_el.get('href') if link_el and link_el.get('href') else None
            price = None
            if price_whole:
                try:
                    price = float(re.sub(r"[^\d]", "", price_whole.text))
                except:
                    price = None
            rating = None
            if rating_el and rating_el.text:
                m = re.search(r"([0-9,.]+) out of 5", rating_el.text)
                if not m:
                    m = re.search(r"([0-9,.]+) de 5", rating_el.text)
                if m:
                    rating = float(m.group(1).replace(',', '.'))
            reviews = None
            if reviews_el and reviews_el.get('aria-label'):
                m2 = re.search(r"([\d,\.]+)", reviews_el.get('aria-label'))
                if m2:
                    reviews = int(m2.group(1).replace('.', '').replace(',', ''))
            items.append({
                "title": title, "link": link, "price": price,
                "rating": rating, "reviews": reviews
            })
    except Exception as e:
        logger.debug(f"Scraping falhou para '{keyword}' em {dominio}: {e}")
    return items

def estimate_sales_proxy(item: Dict[str, Any]) -> float:
    # Proxy simples: mais reviews e rating alto -> mais vendas
    reviews = item.get("reviews") or 0
    rating = item.get("rating") or 0.0
    # escala: rating (0-5) * sqrt(reviews) como proxy de demanda
    return float(rating * math.sqrt(reviews))

def compute_competition(items: List[Dict[str, Any]]) -> float:
    if not items:
        return 1.0
    # proporção de itens com reviews > 100 (concorrência mais forte)
    strong = sum(1 for it in items if (it.get("reviews") or 0) >= 100)
    return strong / max(1, len(items))

def expand_keywords_via_trends(idioma: str, geo: str, max_keywords: int) -> List[str]:
    """Usa pytrends para expandir seeds em consultas correlatas com volume real."""
    seeds = SEEDS.get(idioma, [])
    expanded: List[str] = []
    seen = set()
    for seed in seeds:
        try:
            pytrends.build_payload([seed], timeframe='today 12-m', geo=geo)
            rq = pytrends.related_queries()
            if rq and seed in rq and rq[seed].get('top') is not None:
                top_df = rq[seed]['top']
                for _, row in top_df.head(10).iterrows():
                    term = str(row.get('query', '')).strip()
                    if term and term.lower() not in seen:
                        expanded.append(term)
                        seen.add(term.lower())
                        if len(expanded) >= max_keywords:
                            break
        except Exception:
            # se falhar, ignore seed
            pass
        if len(expanded) >= max_keywords:
            break
    return expanded

def process_market(idioma: str, mercado: Dict[str, str]) -> List[Dict[str, Any]]:
    geo = mercado["geo"]
    dominio = mercado["dominio"]
    # Primeiro tenta expandir via Trends para obter termos com volume real
    keywords = expand_keywords_via_trends(idioma, geo, CONFIG["max_keywords"])[:8]
    if not keywords:
        keywords = generate_keywords(idioma, CONFIG["max_keywords"])[:8]
    results = []
    logger.info(f"Mercado {mercado['nome']} ({dominio}) - {idioma} - {len(keywords)} keywords")
    for kw in keywords:
        vol = get_trends_volume(kw, geo)
        items = scrape_amazon_search(kw, dominio, limit=CONFIG["asins_por_keyword"]) 
        vendas_total = sum(estimate_sales_proxy(it) for it in items)
        competencia = compute_competition(items)
        # normalizações
        volume_norm = min(1.0, vol / 100.0)
        vendas_norm = min(1.0, vendas_total / 50.0)  # proxy
        comp_norm = min(1.0, competencia)
        reviews_media = 0.0
        if items:
            reviews_media = sum((it.get("reviews") or 0) for it in items) / len(items)
        reviews_norm = min(1.0, reviews_media / 300.0)
        score_final = (volume_norm * 0.4) + (vendas_norm * 0.3) + ((1 - comp_norm) * 0.2) + ((1 - reviews_norm) * 0.1)
        vendas_semanais = vendas_total  # proxy já em escala semanal aproximada
        if vendas_semanais > 20 and score_final >= 0.6 and competencia <= CONFIG['limite_competicao_maxima']:
            recomendacao = "Publicar título otimizado (SEO) com variações long-tail"
        else:
            recomendacao = "Monitorar nicho; aumentar coleta e refinar keyword"
        results.append({
            "idioma": idioma, "pais": mercado["nome"], "keyword": kw,
            "score_final": round(score_final, 3), "vendas_semanais": round(vendas_semanais, 2),
            "competicao": round(competencia, 3), "volume_trends": round(vol, 2),
            "recomendacao": recomendacao
        })
        time.sleep(0.4)
    return results

def generate_metadata_for_top(nichos: List[Dict[str, Any]]) -> Dict[str, Any]:
    insights = {}
    keywords_otimizadas = {}
    for n in nichos[:10]:
        idioma = n['idioma']
        kw = n['keyword']
        title = f"{kw.title()} — A Practical Guide"
        subtitle = "Estratégias simples, resultados rápidos"
        backend = [w.strip() for w in re.split(r"\s+", kw) if len(w.strip()) > 2][:7]
        categoria = "Kindle eBooks > Mystery, Thriller & Suspense" if 'mystery' in kw.lower() else "Kindle eBooks > Self-Help"
        descricao1 = "Benefícios claros com foco em resultado imediato."
        descricao2 = "Descrição emocional que conecta com o leitor e incentiva ação."
        faixa_preco = "US$ 2.99 – 6.99"
        insights.setdefault(idioma, []).append({
            "keyword": kw, "titulo": title, "subtitulo": subtitle,
            "backend_keywords": backend, "categoria_sugerida": categoria,
            "descricao_curta_beneficio": descricao1,
            "descricao_curta_emocional": descricao2,
            "faixa_preco_ideal": faixa_preco
        })
        keywords_otimizadas.setdefault(idioma, []).append({"keyword": kw, "variacoes": [kw, kw + " 2025", kw + " kindle"]})
    return insights, keywords_otimizadas

def gerar_recomendacoes(nichos_top: List[Dict[str, Any]]) -> str:
    # Agrupar por país e idioma para densidade
    df = pd.DataFrame(nichos_top)
    densidade = df.groupby(['pais']).size().sort_values(ascending=False)
    paises = [p for p in densidade.index[:3]]
    foco = df.sort_values('score_final', ascending=False).iloc[0]
    plano = [
        "Semana 1: publicar 2 títulos curtos por nicho escolhido",
        "Semana 2: otimizar metadados e testar variações de título",
        "Semana 3: lançar versões traduzidas (es/pt) dos melhores",
        "Semana 4: publicar mais 3 títulos na mesma série para tração orgânica"
    ]
    txt = []
    txt.append(f"- Países prioritários: {', '.join(paises)}")
    txt.append(f"- Nicho inicial: \"{foco['keyword']}\" em {foco['pais']} ({foco['idioma']})")
    txt.append("- Estratégia: série de 3-5 títulos curtos com uniformidade de capa e subtítulo keyword-driven.")
    txt.append("- Próximos passos: traduzir para espanhol neutro e português conforme ROI.")
    txt.append("- Plano de 30 dias:")
    for p in plano:
        txt.append(f"  • {p}")
    return "\n".join(txt)

def main():
    out_dir = Path("./relatorio_growth")
    out_dir.mkdir(parents=True, exist_ok=True)
    all_results = []
    # Permitir limitar mercados via variável de ambiente para execução rápida
    limit_env = os.getenv("MARKETS_LIMIT")
    mercados = CONFIG['mercados']
    if limit_env:
        try:
            n = int(limit_env)
            mercados = mercados[:max(1, n)]
            logger.info(f"Executando com limite de {n} marketplaces (via MARKETS_LIMIT)")
        except Exception:
            pass
    for idioma in CONFIG['idiomas_alvo']:
        for mercado in mercados:
            all_results.extend(process_market(idioma, mercado))
    # Ranking
    df = pd.DataFrame(all_results)
    if df.empty:
        logger.error("Nenhum resultado coletado. Verifique conectividade/antibot.")
        return
    df_rank = df.sort_values(['score_final', 'vendas_semanais', 'volume_trends'], ascending=False).head(50)
    # Salvar CSV
    csv_path = out_dir / 'ranking_top_50_nichos.csv'
    df_rank.to_csv(csv_path, index=False)
    logger.info(f"✓ Salvo {csv_path}")
    # Insights e keywords
    insights, keywords_ot = generate_metadata_for_top(df_rank.to_dict(orient='records'))
    with open(out_dir / 'insights_por_idioma.json', 'w', encoding='utf-8') as f:
        json.dump(insights, f, ensure_ascii=False, indent=2)
    with open(out_dir / 'keywords_otimizadas.json', 'w', encoding='utf-8') as f:
        json.dump(keywords_ot, f, ensure_ascii=False, indent=2)
    # Recomendações práticas
    recs = gerar_recomendacoes(df_rank.to_dict(orient='records'))
    with open(out_dir / 'recomendacoes_praticas.txt', 'w', encoding='utf-8') as f:
        f.write(recs)
    logger.info(f"✓ Relatórios gerados em {out_dir}")

if __name__ == '__main__':
    main()