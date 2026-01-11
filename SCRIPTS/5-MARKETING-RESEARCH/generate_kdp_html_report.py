#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera um relatório HTML visual do KDP Growth Intelligence
Lê os arquivos gerados em ./relatorio_growth e compila um HTML com KPIs, tabela e cards.
"""

import os
import json
import pandas as pd
from datetime import datetime
from pathlib import Path


def generate_html():
    base = Path('.')
    out_dir = base / 'relatorio_growth'
    csv_path = out_dir / 'ranking_top_50_nichos.csv'
    insights_path = out_dir / 'insights_por_idioma.json'
    recs_path = out_dir / 'recomendacoes_praticas.txt'

    df = pd.read_csv(csv_path, encoding='utf-8') if csv_path.exists() else pd.DataFrame()
    insights = {}
    if insights_path.exists():
        with open(insights_path, 'r', encoding='utf-8') as f:
            insights = json.load(f)
    recs_text = ''
    if recs_path.exists():
        with open(recs_path, 'r', encoding='utf-8') as f:
            recs_text = f.read()

    total = len(df)
    mercados = df['pais'].nunique() if not df.empty else 0
    idiomas = df['idioma'].nunique() if not df.empty else 0

    top_df = df.sort_values(['score_final', 'vendas_semanais', 'volume_trends'], ascending=False).head(20) if not df.empty else pd.DataFrame()
    pais_counts = df['pais'].value_counts().head(10) if not df.empty else pd.Series([], dtype=int)

    def table_rows():
        rows = []
        if not top_df.empty:
            for _, r in top_df.iterrows():
                rows.append(f"<tr><td>{r['idioma']}</td><td>{r['pais']}</td><td>{r['keyword']}</td><td>{r['score_final']:.3f}</td><td>{r['vendas_semanais']:.2f}</td><td>{r['volume_trends']:.2f}</td><td>{r['competicao']:.2f}</td><td>{r['recomendacao']}</td></tr>")
        else:
            rows.append("<tr><td colspan='8'>Sem dados disponíveis.</td></tr>")
        return "\n".join(rows)

    def country_bars():
        bars = []
        if len(pais_counts) > 0:
            maxv = pais_counts.iloc[0]
            for p, v in pais_counts.items():
                pct = int((v / maxv) * 100) if maxv > 0 else 0
                bars.append(f"<div class='bar-item'><span class='label'>{p}</span><div class='bar'><div class='fill' style='width:{pct}%;'></div></div><span class='val'>{v}</span></div>")
        else:
            bars.append("<p>Nenhum país encontrado.</p>")
        return "\n".join(bars)

    def insight_cards():
        cards = []
        count = 0
        for idioma, lst in insights.items():
            for it in lst[:3]:
                count += 1
                cards.append(
                    f"<div class='card'><div class='card-title'>{it.get('titulo','')}</div><div class='card-sub'>{it.get('subtitulo','')}</div><div class='card-body'><b>Keyword:</b> {it.get('keyword','')}<br/><b>Categoria:</b> {it.get('categoria_sugerida','')}<br/><b>Preço ideal:</b> {it.get('faixa_preco_ideal','')}<br/><b>Backend:</b> {', '.join(it.get('backend_keywords', []))}</div><div class='tag'>{idioma}</div></div>"
                )
                if count >= 8:
                    break
            if count >= 8:
                break
        if not cards:
            cards.append("<p>Sem insights disponíveis.</p>")
        return "\n".join(cards)

    recs_list = ""
    if recs_text:
        recs_lines = [l.strip() for l in recs_text.splitlines() if l.strip()]
        recs_list = "\n".join([f"<li>{l}</li>" for l in recs_lines])

    timestamp = datetime.now().strftime('%d/%m/%Y %H:%M')

    html = f"""
<!DOCTYPE html>
<html lang='pt-BR'>
<head>
<meta charset='utf-8'/>
<title>KDP Growth Intelligence — Relatório Global</title>
<style>
body {{ font-family: Arial, sans-serif; background:#f6f8fa; color:#222; margin:0; }}
.header {{ background:#0d6efd; color:white; padding:20px 30px; }}
.container {{ padding:20px 30px; }}
.h1 {{ font-size:24px; margin:0; }}
.kpi {{ display:flex; gap:20px; margin:20px 0; }}
.kpi .box {{ background:white; padding:15px 20px; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.1); }}
.section {{ margin:30px 0; }}
.table {{ width:100%; border-collapse:collapse; background:white; box-shadow:0 1px 3px rgba(0,0,0,0.1); }}
.table th, .table td {{ border:1px solid #ddd; padding:8px; font-size:13px; }}
.table th {{ background:#f0f3f6; text-align:left; }}
.bar-item {{ display:flex; align-items:center; gap:10px; margin:8px 0; }}
.bar {{ flex:1; height:10px; background:#e9ecef; border-radius:10px; overflow:hidden; }}
.fill {{ height:100%; background:#0d6efd; }}
.cards {{ display:grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap:15px; }}
.card {{ background:white; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.1); padding:12px; position:relative; }}
.card-title {{ font-weight:bold; margin-bottom:6px; }}
.card-sub {{ color:#555; margin-bottom:10px; }}
.card .tag {{ position:absolute; top:10px; right:10px; background:#ffc107; padding:4px 8px; border-radius:6px; font-size:12px; }}
.footer {{ color:#666; font-size:12px; margin-top:30px; }}
</style>
</head>
<body>
<div class='header'>
  <div class='h1'>KDP Growth Intelligence — Relatório Global</div>
  <div>Gerado em {timestamp}</div>
</div>
<div class='container'>
  <div class='kpi'>
    <div class='box'>Total de nichos: <b>{total}</b></div>
    <div class='box'>Mercados cobertos: <b>{mercados}</b></div>
    <div class='box'>Idiomas cobertos: <b>{idiomas}</b></div>
  </div>

  <div class='section'>
    <h3>Top 20 Nichos por Score</h3>
    <table class='table'>
      <thead><tr><th>Idioma</th><th>País</th><th>Keyword</th><th>Score</th><th>Vendas (proxy)</th><th>Volume Trends</th><th>Competição</th><th>Ação</th></tr></thead>
      <tbody>
        {table_rows()}
      </tbody>
    </table>
  </div>

  <div class='section'>
    <h3>Densidade por País (Top 10)</h3>
    {country_bars()}
  </div>

  <div class='section'>
    <h3>Insights de Metadados (até 8 cards)</h3>
    <div class='cards'>
      {insight_cards()}
    </div>
  </div>

  <div class='section'>
    <h3>Plano e Recomendações</h3>
    <ul>
      {recs_list}
    </ul>
  </div>

  <div class='footer'>
    Fonte: Google Trends + Scraping leve Kindle. Este é um MVP; números são proxies.
  </div>
</div>
</body>
</html>
"""

    out_dir.mkdir(parents=True, exist_ok=True)
    html_path = out_dir / 'relatorio_kdp.html'
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ HTML gerado em: {html_path}")
    return str(html_path)


if __name__ == '__main__':
    generate_html()