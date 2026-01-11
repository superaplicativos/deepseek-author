#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agrega as 1000 palavras-chave mais buscadas agora (global) usando Google Suggest.
Foco em termos de livros (seeds locais por idioma) e filtro por tokens de livro.

Saída: relatorio_growth/top_1000_global_keywords.csv
Campos: keyword, hits, langs_count, langs, seeds_count, example_lang
"""

import time
import csv
from pathlib import Path
from typing import Dict, List
import requests

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/118.0 Safari/537.36"
)

LANGS = ["en", "es", "pt", "fr", "it", "de", "nl", "sv", "pl", "tr", "ar", "ja"]

# Tokens que caracterizam consultas de livros por idioma
BOOK_TOKENS_BY_LANG = {
    "en": ["book", "novel", "coloring book", "activity book", "word search", "cookbook", "journal", "workbook", "children book", "manga", "graphic novel"],
    "es": ["libro", "novela", "libro para", "libro de", "sopa de letras", "libro de cocina", "diario", "cuaderno"],
    "pt": ["livro", "romance", "livro de", "caça-palavras", "livro de receitas", "diário", "caderno"],
    "fr": ["livre", "roman", "livre de", "mots mêlés", "livre de cuisine", "journal", "cahier"],
    "it": ["libro", "libri", "romanzo", "libro di", "cruciverba", "sudoku", "libro di cucina", "diario", "quaderno"],
    "de": ["buch", "bücher", "roman", "malbuch", "aktivitätsbuch", "wortsuche", "kochbuch", "tagebuch", "arbeitsbuch"],
    "nl": ["boek", "boeken", "kleurboek", "activiteitenboek", "woordzoeker", "kookboek", "dagboek", "werkboek"],
    "sv": ["bok", "böcker", "målarbok", "aktivitetsbok", "korsord", "kokbok", "dagbok", "arbetsbok"],
    "pl": ["książka", "książki", "kolorowanka", "książka aktywności", "krzyżówka", "książka kucharska", "dziennik", "zeszyt"],
    "tr": ["kitap", "kitaplar", "boyama kitabı", "aktivite kitabı", "bulmaca", "yemek kitabı", "günlük", "çalışma kitabı"],
    "ar": ["كتاب", "رواية", "كتاب تلوين", "كتاب نشاط", "كلمات متقاطعة", "كتاب طبخ", "مفكرة"],
    "ja": ["本", "小説", "塗り絵", "アクティビティブック", "クロスワード", "料理本", "日記", "ワークブック", "漫画"]
}

# Seeds restritas a tokens de livro para evitar ruído
SEEDS_BY_LANG = {
    "en": ["book ", "books ", "novel ", "coloring book ", "activity book ", "word search ", "cookbook ", "journal ", "workbook "],
    "es": ["libro ", "libros ", "novela ", "libro para ", "libro de ", "sopa de letras ", "libro de cocina ", "diario ", "cuaderno "],
    "pt": ["livro ", "livros ", "romance ", "livro de ", "caça-palavras ", "livro de receitas ", "diário ", "caderno "],
    "fr": ["livre ", "livres ", "roman ", "livre de ", "mots mêlés ", "livre de cuisine ", "journal ", "cahier "],
    "it": ["libro ", "libri ", "romanzo ", "libro di ", "cruciverba ", "libro di cucina ", "diario ", "quaderno "],
    "de": ["buch ", "bücher ", "roman ", "malbuch ", "aktivitätsbuch ", "wortsuche ", "kochbuch ", "tagebuch ", "arbeitsbuch "],
    "nl": ["boek ", "boeken ", "kleurboek ", "activiteitenboek ", "woordzoeker ", "kookboek ", "dagboek ", "werkboek "],
    "sv": ["bok ", "böcker ", "målarbok ", "aktivitetsbok ", "korsord ", "kokbok ", "dagbok ", "arbetsbok "],
    "pl": ["książka ", "książki ", "kolorowanka ", "książka aktywności ", "krzyżówka ", "książka kucharska ", "dziennik ", "zeszyt "],
    "tr": ["kitap ", "kitaplar ", "boyama kitabı ", "aktivite kitabı ", "bulmaca ", "yemek kitabı ", "günlük ", "çalışma kitabı "],
    "ar": ["كتاب ", "رواية ", "كتاب تلوين ", "كتاب نشاط ", "كلمات متقاطعة ", "كتاب طبخ ", "مفكرة "],
    "ja": ["本 ", "小説 ", "塗り絵 ", "アクティビティブック ", "クロスワード ", "料理本 ", "日記 ", "ワークブック ", "漫画 "]
}

EXPANSIONS = ["a","e","i","o","u","s","t","r","n","m","1","2","3"]
NEGATIVE_TERMS = {"michael jackson","premier league","reigns","numerals","imdb","netflix","song","album","release date"}


def google_suggest(prefix: str, hl: str) -> List[str]:
    url = "https://suggestqueries.google.com/complete/search"
    params = {"client": "firefox", "q": prefix, "hl": hl}
    headers = {"User-Agent": UA, "Accept": "application/json"}
    try:
        r = requests.get(url, params=params, headers=headers, timeout=10)
        r.raise_for_status()
        data = r.json()
        if isinstance(data, list) and len(data) >= 2 and isinstance(data[1], list):
            return [s for s in data[1] if isinstance(s, str)]
    except Exception:
        return []
    return []


def is_booky(s: str, hl: str) -> bool:
    s_low = s.lower()
    for tok in BOOK_TOKENS_BY_LANG.get(hl, []):
        if tok in s_low:
            return True
    return False


def is_negative(s: str) -> bool:
    s_low = s.lower()
    for neg in NEGATIVE_TERMS:
        if neg in s_low:
            return True
    return False


def collect_top_1000() -> List[Dict]:
    counts: Dict[str, Dict] = {}
    for hl in LANGS:
        seeds = SEEDS_BY_LANG.get(hl, [])
        for seed in seeds:
            sugs = google_suggest(seed, hl)
            for s in sugs:
                if len(s) <= len(seed):
                    continue
                if not is_booky(s, hl) or is_negative(s):
                    continue
                key = s.lower().strip()
                entry = counts.get(key)
                if not entry:
                    counts[key] = {"keyword": s, "hits": 1, "langs": {hl}, "seeds": {seed}, "example_lang": hl}
                else:
                    entry["hits"] += 1
                    entry["langs"].add(hl)
                    entry["seeds"].add(seed)
            time.sleep(0.05)
            for ex in EXPANSIONS:
                sugs2 = google_suggest(seed + ex, hl)
                for s in sugs2:
                    if len(s) <= len(seed):
                        continue
                    if not is_booky(s, hl) or is_negative(s):
                        continue
                    key = s.lower().strip()
                    entry = counts.get(key)
                    if not entry:
                        counts[key] = {"keyword": s, "hits": 1, "langs": {hl}, "seeds": {seed}, "example_lang": hl}
                    else:
                        entry["hits"] += 1
                        entry["langs"].add(hl)
                        entry["seeds"].add(seed)
                time.sleep(0.05)
    rows = []
    for k, v in counts.items():
        rows.append({
            "keyword": v["keyword"],
            "hits": v["hits"],
            "langs_count": len(v["langs"]),
            "langs": ",".join(sorted(list(v["langs"]))),
            "seeds_count": len(v["seeds"]),
            "example_lang": v["example_lang"],
        })
    rows.sort(key=lambda x: (x["hits"], x["langs_count"], x["seeds_count"], x["keyword"]), reverse=True)
    return rows[:1000]


def save_csv(rows: List[Dict]) -> str:
    out_dir = Path("relatorio_growth")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "top_1000_global_keywords.csv"
    with open(out_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["keyword","hits","langs_count","langs","seeds_count","example_lang"])
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return str(out_csv)


def main():
    rows = collect_top_1000()
    path = save_csv(rows)
    print(f"✅ CSV salvo em: {path}")
    print(f"Total linhas: {len(rows)}")


if __name__ == "__main__":
    main()