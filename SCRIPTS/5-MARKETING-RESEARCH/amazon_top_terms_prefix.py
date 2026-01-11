#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Coletor de Top 10 global de termos para um prefixo específico na busca da Amazon.
- Consulta o endpoint de sugestões (/search/suggestions) em múltiplos marketplaces
  com os aliases de livros (stripbooks) e Kindle (digital-text).
- Agrega sugestões por frequência e número de mercados em que aparecem.
- Não usa Google Trends; é um ranking puramente baseado em presença de sugestão.

Uso:
  python amazon_top_terms_prefix.py --prefix "book of" --top 10

Saída:
  - Imprime o Top N global no console
  - Salva CSV em relatorio_growth/top_terms_prefix_<slug>.csv
"""

import argparse
import re
import time
import csv
from pathlib import Path
from typing import Dict, List

import requests

MARKETS = [
    {"country":"Estados Unidos","domain":"www.amazon.com","lang":"en_US"},
    {"country":"Reino Unido","domain":"www.amazon.co.uk","lang":"en_US"},
    {"country":"Alemanha","domain":"www.amazon.de","lang":"de_DE"},
    {"country":"França","domain":"www.amazon.fr","lang":"fr_FR"},
    {"country":"Itália","domain":"www.amazon.it","lang":"it_IT"},
    {"country":"Espanha","domain":"www.amazon.es","lang":"es_ES"},
    {"country":"Países Baixos","domain":"www.amazon.nl","lang":"nl_NL"},
    {"country":"Bélgica","domain":"www.amazon.be","lang":"nl_NL"},
    {"country":"Suécia","domain":"www.amazon.se","lang":"sv_SE"},
    {"country":"Polônia","domain":"www.amazon.pl","lang":"pl_PL"},
    {"country":"Turquia","domain":"www.amazon.com.tr","lang":"tr_TR"},
    {"country":"Emirados Árabes","domain":"www.amazon.ae","lang":"ar_AE"},
    {"country":"Arábia Saudita","domain":"www.amazon.sa","lang":"ar_SA"},
    {"country":"Egito","domain":"www.amazon.eg","lang":"ar_EG"},
    {"country":"Japão","domain":"www.amazon.co.jp","lang":"ja_JP"},
    {"country":"Índia","domain":"www.amazon.in","lang":"en_IN"},
    {"country":"Austrália","domain":"www.amazon.com.au","lang":"en_AU"},
    {"country":"Singapura","domain":"www.amazon.sg","lang":"en_SG"},
    {"country":"Canadá","domain":"www.amazon.ca","lang":"en_CA"},
    {"country":"México","domain":"www.amazon.com.mx","lang":"es_MX"},
    {"country":"Brasil","domain":"www.amazon.com.br","lang":"pt_BR"},
]

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


def fetch_suggestions(domain: str, prefix: str, alias: str, accept_lang: str = None) -> List[str]:
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
    if accept_lang:
        headers["Accept-Language"] = accept_lang.replace("_", "-")
    try:
        r = SESSION.get(url, params=params, headers=headers, timeout=10)
        r.raise_for_status()
        data = r.json()
        suggestions = [s.get("value", "").strip() for s in data.get("suggestions", [])]
        if suggestions:
            return [s for s in suggestions if s]
    except Exception:
        pass
    # fallback: endpoint de completion
    base = domain.replace("www.", "")
    url2 = f"https://completion.{base}/api/2017/suggestions"
    headers2 = {
        "Referer": f"https://{domain}/s?k={prefix}&i={alias}",
        "Accept": "application/json",
    }
    if accept_lang:
        headers2["Accept-Language"] = accept_lang.replace("_", "-")
    try:
        r2 = SESSION.get(url2, params=params, headers=headers2, timeout=10)
        r2.raise_for_status()
        data2 = r2.json()
        return [s.get("value", "").strip() for s in data2.get("suggestions", []) if s.get("value")]
    except Exception:
        return []


def slugify(text: str) -> str:
    return re.sub(r"\W+", "_", text.strip().lower()).strip("_")


def aggregate_global(prefix: str, top_n: int = 10) -> List[Dict]:
    counts: Dict[str, Dict] = {}
    aliases = ["stripbooks", "digital-text"]

    for mk in MARKETS:
        dom = mk["domain"]
        acc_lang = mk.get("lang")
        for al in aliases:
            sugs = fetch_suggestions(dom, prefix, al, accept_lang=acc_lang)
            for s in sugs:
                key = s.lower()
                entry = counts.get(key)
                if not entry:
                    counts[key] = {
                        "keyword": s,
                        "hits": 1,
                        "markets": {dom},
                        "aliases": {al},
                    }
                else:
                    entry["hits"] += 1
                    entry["markets"].add(dom)
                    entry["aliases"].add(al)
            time.sleep(0.1)

    rows = []
    for k, v in counts.items():
        rows.append({
            "keyword": v["keyword"],
            "hits": v["hits"],
            "market_count": len(v["markets"]),
            "aliases": ",".join(sorted(list(v["aliases"]))),
        })

    rows.sort(key=lambda x: (x["hits"], x["market_count"], x["keyword"]), reverse=True)
    return rows[:top_n]


def save_csv(prefix: str, rows: List[Dict]) -> str:
    out_dir = Path("relatorio_growth")
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify(prefix)
    out_csv = out_dir / f"top_terms_prefix_{slug}.csv"
    with open(out_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["keyword","hits","market_count","aliases"])
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return str(out_csv)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prefix", required=True, help="Prefixo de busca, por ex.: 'book of'")
    ap.add_argument("--top", type=int, default=10, help="Top N global")
    args = ap.parse_args()

    rows = aggregate_global(args.prefix, args.top)
    out_csv = save_csv(args.prefix, rows)

    print(f"\nTop {args.top} globais para prefixo: {args.prefix}\n")
    for i, r in enumerate(rows, 1):
        print(f"{i}. {r['keyword']} — hits: {r['hits']}, mercados: {r['market_count']}, aliases: {r['aliases']}")
    print(f"\n✅ CSV salvo em: {out_csv}")


if __name__ == "__main__":
    main()