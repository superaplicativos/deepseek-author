#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera um relatório visual em HTML para os Top 1000 keywords globais
focados em livros (coletados via Google Suggest), com KPIs, filtros e gráficos.

Entrada: relatorio_growth/top_1000_global_keywords.csv
Saída:  relatorio_growth/relatorio_keywords.html
"""

import csv
import json
from pathlib import Path
from collections import Counter

IN_CSV = Path("relatorio_growth/top_1000_global_keywords.csv")
OUT_HTML = Path("relatorio_growth/relatorio_keywords.html")


def load_rows():
    rows = []
    with open(IN_CSV, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            # normaliza tipos
            row["hits"] = int(row.get("hits", 0))
            row["langs_count"] = int(row.get("langs_count", 0))
            row["seeds_count"] = int(row.get("seeds_count", 0))
            row["langs"] = row.get("langs", "").strip()
            row["keyword"] = row.get("keyword", "").strip()
            row["example_lang"] = row.get("example_lang", "").strip()
            rows.append(row)
    return rows


def compute_stats(rows):
    # distribuição de idiomas
    lang_counter = Counter()
    for r in rows:
        langs = [l.strip() for l in r["langs"].split(",") if l.strip()]
        lang_counter.update(langs)
    total_keywords = len(rows)
    unique_langs = len(lang_counter)
    top_lang, top_lang_count = (None, 0)
    if lang_counter:
        top_lang, top_lang_count = lang_counter.most_common(1)[0]
    avg_hits = round(sum(r["hits"] for r in rows) / max(total_keywords, 1), 2)
    return {
        "total_keywords": total_keywords,
        "unique_langs": unique_langs,
        "top_lang": top_lang or "-",
        "top_lang_count": top_lang_count,
        "avg_hits": avg_hits,
        "lang_counts": dict(lang_counter),
    }


def top_n(rows, n=50):
    rows_sorted = sorted(
        rows,
        key=lambda x: (x["hits"], x["langs_count"], x["seeds_count"], x["keyword"]),
        reverse=True,
    )
    return rows_sorted[:n]


def make_html(rows, stats):
    rows_json = json.dumps(rows, ensure_ascii=False)
    lang_counts = stats["lang_counts"]
    langs = list(lang_counts.keys())
    counts = [lang_counts[l] for l in langs]
    top50 = top_n(rows, 50)

    top50_html_rows = "\n".join(
        f"<tr><td>{r['keyword']}</td><td>{r['hits']}</td><td>{r['langs']}</td><td>{r['seeds_count']}</td><td>{r['example_lang']}</td></tr>"
        for r in top50
    )

    lang_options = "".join(f"<option value='{l}'>{l}</option>" for l in langs)

    html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Relatório Global de Palavras-Chave (Livros) • Top 1000</title>
  <link rel="preconnect" href="https://cdn.jsdelivr.net" />
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 0; background: #0f172a; color: #e2e8f0; }}
    header {{ padding: 16px 24px; background: #111827; border-bottom: 1px solid #1f2937; }}
    h1 {{ margin: 0; font-size: 20px; }}
    .container {{ padding: 24px; }}
    .kpis {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 16px; margin-bottom: 24px; }}
    .card {{ background: #111827; border: 1px solid #1f2937; border-radius: 12px; padding: 16px; }}
    .card h3 {{ margin: 0 0 8px 0; font-size: 14px; color: #93c5fd; }}
    .card .value {{ font-size: 24px; font-weight: bold; color: #e5e7eb; }}
    .flex {{ display: flex; gap: 16px; align-items: center; margin-bottom: 16px; flex-wrap: wrap; }}
    .flex label {{ font-size: 14px; color: #9ca3af; }}
    input[type="text"], select {{ background: #0b1220; color: #e5e7eb; border: 1px solid #1f2937; border-radius: 8px; padding: 8px 10px; }}
    table {{ width: 100%; border-collapse: collapse; margin-top: 12px; }}
    th, td {{ border-bottom: 1px solid #1f2937; padding: 10px; text-align: left; }}
    th {{ color: #93c5fd; font-size: 13px; text-transform: uppercase; letter-spacing: 0.05em; }}
    tr:hover {{ background: #0b1220; }}
    .section {{ margin-top: 28px; }}
    .muted {{ color: #9ca3af; font-size: 12px; }}
    .badge {{ display: inline-block; background: #1f2937; color: #e5e7eb; border-radius: 999px; padding: 4px 10px; margin-right: 8px; font-size: 12px; }}
    canvas {{ background: #0b1220; border: 1px solid #1f2937; border-radius: 12px; padding: 12px; }}
  </style>
</head>
<body>
  <header>
    <h1>Relatório Global de Palavras-Chave (Livros) • Top 1000</h1>
    <div class="muted">Fonte: Google Suggest multi-idioma • Filtros de termos de livro ativos</div>
  </header>
  <div class="container">
    <div class="kpis">
      <div class="card"><h3>Total de Keywords</h3><div class="value">{stats['total_keywords']}</div></div>
      <div class="card"><h3>Idiomas Únicos</h3><div class="value">{stats['unique_langs']}</div></div>
      <div class="card"><h3>Idioma com Mais Ocorrências</h3><div class="value">{stats['top_lang']}</div></div>
      <div class="card"><h3>Ocorrências do Top Idioma</h3><div class="value">{stats['top_lang_count']}</div></div>
      <div class="card"><h3>Média de Hits</h3><div class="value">{stats['avg_hits']}</div></div>
    </div>

    <div class="section">
      <h2>Distribuição por Idioma</h2>
      <p class="muted">Quantas keywords aparecem com sugestões em cada idioma.</p>
      <canvas id="langChart" height="120"></canvas>
    </div>

    <div class="section">
      <h2>Top 50 por Hits</h2>
      <p class="muted">Ordenado por hits, depois número de idiomas e seeds.</p>
      <table>
        <thead>
          <tr>
            <th>Keyword</th>
            <th>Hits</th>
            <th>Idiomas</th>
            <th>Seeds</th>
            <th>Idioma Exemplo</th>
          </tr>
        </thead>
        <tbody>
          {top50_html_rows}
        </tbody>
      </table>
    </div>

    <div class="section">
      <h2>Explorar (Filtro)</h2>
      <div class="flex">
        <label for="langFilter">Idioma:</label>
        <select id="langFilter"><option value="">Todos</option>{lang_options}</select>
        <label for="searchInput">Busca:</label>
        <input type="text" id="searchInput" placeholder="Digite parte da keyword" />
      </div>
      <div id="resultsInfo" class="muted"></div>
      <table>
        <thead>
          <tr>
            <th>Keyword</th>
            <th>Hits</th>
            <th>Idiomas</th>
            <th>Seeds</th>
            <th>Idioma Exemplo</th>
          </tr>
        </thead>
        <tbody id="resultsBody"></tbody>
      </table>
    </div>

    <div class="section">
      <span class="badge">Fonte: Google Suggest</span>
      <span class="badge">Filtro: tokens de livro por idioma</span>
      <span class="badge">Atualizado automaticamente do CSV</span>
    </div>
  </div>

  <script>
    const rows = {json.dumps(rows, ensure_ascii=False)};
    const langLabels = {json.dumps(langs, ensure_ascii=False)};
    const langCounts = {json.dumps(counts, ensure_ascii=False)};

    // Gráfico por idioma
    const ctx = document.getElementById('langChart').getContext('2d');
    new Chart(ctx, {{
      type: 'bar',
      data: {{
        labels: langLabels,
        datasets: [{{
          label: 'Ocorrências por idioma',
          data: langCounts,
          backgroundColor: '#3b82f6',
          borderColor: '#60a5fa',
          borderWidth: 1
        }}]
      }},
      options: {{
        scales: {{
          x: {{ ticks: {{ color: '#e5e7eb' }} }},
          y: {{ ticks: {{ color: '#e5e7eb' }} }}
        }},
        plugins: {{ legend: {{ labels: {{ color: '#e5e7eb' }} }} }}
      }}
    }});

    // Lista com filtros
    const langFilter = document.getElementById('langFilter');
    const searchInput = document.getElementById('searchInput');
    const resultsBody = document.getElementById('resultsBody');
    const resultsInfo = document.getElementById('resultsInfo');

    function renderList() {{
      const lang = langFilter.value.trim();
      const q = searchInput.value.trim().toLowerCase();
      let filtered = rows.slice();
      if (lang) {{
        filtered = filtered.filter(r => (r.langs || '').split(',').map(s => s.trim()).includes(lang));
      }}
      if (q) {{
        filtered = filtered.filter(r => (r.keyword || '').toLowerCase().includes(q));
      }}
      filtered.sort((a, b) => {{
        // mesma ordenação usada no Top 50
        const kA = [a.hits, a.langs_count, a.seeds_count, a.keyword];
        const kB = [b.hits, b.langs_count, b.seeds_count, b.keyword];
        for (let i = 0; i < 4; i++) {{
          if (kA[i] < kB[i]) return 1;
          if (kA[i] > kB[i]) return -1;
        }}
        return 0;
      }});
      resultsInfo.textContent = 'Resultados: ' + filtered.length;
      resultsBody.innerHTML = filtered.slice(0, 200).map(r => (
        '<tr><td>' + r.keyword + '</td><td>' + r.hits + '</td><td>' + r.langs + '</td><td>' + r.seeds_count + '</td><td>' + r.example_lang + '</td></tr>'
      )).join('');
    }}

    langFilter.addEventListener('change', renderList);
    searchInput.addEventListener('input', renderList);
    renderList();
  </script>
</body>
</html>
"""
    return html


def main():
    rows = load_rows()
    stats = compute_stats(rows)
    html = make_html(rows, stats)
    OUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"✅ Relatório HTML salvo em: {OUT_HTML}")


if __name__ == "__main__":
    main()