"""
Gerador de PDF Profissional para Pitch Deck - Turma da Aventura
Cria um PDF corporativo com visualizações de dados para apresentação a investidores
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from io import BytesIO
from datetime import datetime
import re

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether
from reportlab.pdfgen import canvas

# Configurações
BASE_DIR = Path(__file__).parent
INTELIGENCIA_DIR = BASE_DIR / "INTELIGENCIA-DE-MERCADO"
OUTPUT_PDF = BASE_DIR / "PITCH-DECK-TURMA-DA-AVENTURA.pdf"
PITCH_MD = BASE_DIR / "PITCH-DECK-TURMA-DA-AVENTURA.md"

# Paleta de cores corporativa
COLORS = {
    'primary': colors.HexColor('#1a365d'),      # Azul escuro corporate
    'secondary': colors.HexColor('#4299e1'),    # Azul médio
    'accent': colors.HexColor('#2d3748'),       # Cinza escuro
    'light': colors.HexColor('#e2e8f0'),        # Cinza claro
    'success': colors.HexColor('#48bb78'),      # Verde
}

# Configurar matplotlib para gráficos profissionais
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 150

# ==============================================================================
# RODAPÉ E CABEÇALHO
# ==============================================================================

class FooterCanvas(canvas.Canvas):
    """Canvas personalizado com rodapé"""

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for page_num, page in enumerate(self.pages, 1):
            self.__dict__.update(page)
            if page_num > 1:  # Pular rodapé da capa
                self.draw_footer(page_num, page_count)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_footer(self, page_num, page_count):
        self.setFont('Helvetica', 9)
        self.setFillColor(colors.HexColor('#718096'))
        text = f"Turma da Aventura - Pitch Deck | Página {page_num} de {page_count} | Janeiro 2026"
        self.drawRightString(A4[0] - 2*cm, 1.5*cm, text)

# ==============================================================================
# CARREGAR DADOS
# ==============================================================================

def load_kdp_data():
    """Carrega dados do Excel KDP"""
    print("[*] Carregando dados KDP...")
    kdp_file = list(INTELIGENCIA_DIR.glob("KDP_Orders-*.xlsx"))[0]
    df_resumo = pd.read_excel(kdp_file, sheet_name='Resumo')
    df_vendas = pd.read_excel(kdp_file, sheet_name='Vendas combinadas')
    print(f"[OK] Dados carregados: {len(df_resumo)} meses, {len(df_vendas)} transacoes")
    return df_resumo, df_vendas

def load_pitch_content():
    """Carrega conteudo do pitch deck Markdown"""
    print("[*] Carregando conteudo do pitch...")
    with open(PITCH_MD, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"[OK] Pitch carregado: {len(content)} caracteres")
    return content

# ==============================================================================
# GERAR VISUALIZAÇÕES
# ==============================================================================

def generate_sales_chart(df_resumo):
    """Gráfico 1: Vendas Mensais (Linha do Tempo)"""
    print("[*] Gerando grafico de vendas mensais...")

    fig, ax = plt.subplots(figsize=(10, 4))

    # Preparar dados
    df_plot = df_resumo.copy()
    df_plot['Total'] = (
        df_plot['Unidades líquidas vendidas (eBook)'] +
        df_plot['Unidades líquidas vendidas (livro com capa comum)']
    )
    df_plot = df_plot.iloc[::-1]  # Ordem cronológica

    # Plot
    ax.plot(range(len(df_plot)), df_plot['Total'],
            marker='o', linewidth=2, markersize=5,
            color='#4299e1', label='Unidades Vendidas')

    # Destacar pico
    max_idx = df_plot['Total'].idxmax()
    max_val = df_plot['Total'].max()
    ax.plot(df_plot.index.get_loc(max_idx), max_val,
            marker='*', markersize=15, color='#48bb78',
            label=f'Pico: {int(max_val)} unidades')

    # Styling
    ax.set_xlabel('Período (2023-2026)', fontsize=10, fontweight='bold')
    ax.set_ylabel('Unidades Vendidas', fontsize=10, fontweight='bold')
    ax.set_title('Crescimento de Vendas Mensais', fontsize=12, fontweight='bold', pad=15)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left', frameon=True)

    # Labels do eixo X
    step = max(1, len(df_plot) // 8)
    ax.set_xticks(range(0, len(df_plot), step))
    ax.set_xticklabels([str(df_plot.iloc[i]['Data'])[:7] for i in range(0, len(df_plot), step)],
                       rotation=45, ha='right', fontsize=8)

    ax.set_facecolor('#f8f9fa')
    fig.patch.set_facecolor('white')
    plt.tight_layout()

    # Salvar como BytesIO
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor='white')
    buf.seek(0)
    plt.close()

    print("[OK] Grafico de vendas gerado")
    return buf

def generate_market_pie_chart(df_vendas):
    """Gráfico 2: Distribuição de Mercados (Pizza)"""
    print("[*] Gerando grafico de distribuicao de mercados...")

    # Agrupar vendas por loja
    vendas_por_loja = df_vendas.groupby('Loja')['Número líquido de unidades vendidas'].sum()

    # Top 4 + Outros
    top_4 = vendas_por_loja.nlargest(4)
    outros = vendas_por_loja.iloc[4:].sum() if len(vendas_por_loja) > 4 else 0

    # Preparar dados
    labels = []
    values = []
    for loja, val in top_4.items():
        nome_curto = loja.replace('Amazon.', '').replace('com.', '').upper()
        if nome_curto == 'COM': nome_curto = 'EUA'
        elif nome_curto == 'BR': nome_curto = 'Brasil'
        elif nome_curto == 'ES': nome_curto = 'Espanha'
        elif nome_curto == 'DE': nome_curto = 'Alemanha'

        pct = (val / vendas_por_loja.sum()) * 100
        labels.append(f'{nome_curto}\n{int(val)} ({pct:.1f}%)')
        values.append(val)

    if outros > 0:
        pct = (outros / vendas_por_loja.sum()) * 100
        labels.append(f'Outros\n{int(outros)} ({pct:.1f}%)')
        values.append(outros)

    # Cores graduais de azul
    colors_chart = ['#1a365d', '#2c5282', '#4299e1', '#63b3ed', '#90cdf4'][:len(values)]

    # Plot
    fig, ax = plt.subplots(figsize=(8, 6))
    wedges, texts, autotexts = ax.pie(
        values,
        labels=labels,
        colors=colors_chart,
        autopct='',
        startangle=90,
        textprops={'fontsize': 9, 'fontweight': 'bold'}
    )

    ax.set_title('Distribuição de Vendas por Mercado',
                 fontsize=12, fontweight='bold', pad=15)

    plt.tight_layout()

    # Salvar
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor='white')
    buf.seek(0)
    plt.close()

    print("[OK] Grafico de pizza gerado")
    return buf

def generate_world_map(df_vendas):
    """Gráfico 3: Mapa Mundial de Presença"""
    print("[*] Gerando mapa mundial...")

    # Vendas por país
    vendas_por_loja = df_vendas.groupby('Loja')['Número líquido de unidades vendidas'].sum()

    # Mapear lojas para países
    pais_map = {
        'Amazon.com': 'EUA',
        'Amazon.com.br': 'Brasil',
        'Amazon.es': 'Espanha',
        'Amazon.de': 'Alemanha',
        'Amazon.co.uk': 'Reino Unido',
        'Amazon.it': 'Itália',
        'Amazon.com.au': 'Austrália',
        'Amazon.se': 'Suécia',
        'Amazon.co.jp': 'Japão',
        'Amazon.fr': 'França',
    }

    paises_data = {}
    for loja, vendas in vendas_por_loja.items():
        if loja in pais_map:
            paises_data[pais_map[loja]] = int(vendas)

    # Criar visualização (bar chart horizontal)
    fig, ax = plt.subplots(figsize=(10, 5))

    paises = list(paises_data.keys())
    valores = list(paises_data.values())

    # Ordenar
    sorted_indices = np.argsort(valores)[::-1]
    paises = [paises[i] for i in sorted_indices]
    valores = [valores[i] for i in sorted_indices]

    # Cores graduais
    max_val = max(valores)
    colors_map = [plt.cm.Blues(0.3 + 0.7 * (v/max_val)) for v in valores]

    # Plot
    bars = ax.barh(paises, valores, color=colors_map, edgecolor='white', linewidth=1.5)

    # Valores nas barras
    for i, (bar, val) in enumerate(zip(bars, valores)):
        ax.text(val + max_val*0.02, i, f'{val}',
                va='center', fontsize=9, fontweight='bold')

    # Styling
    ax.set_xlabel('Unidades Vendidas', fontsize=10, fontweight='bold')
    ax.set_title('Presença Global - 10 Países Ativos', fontsize=12, fontweight='bold', pad=15)
    ax.grid(axis='x', alpha=0.3)
    ax.set_facecolor('#f8f9fa')
    fig.patch.set_facecolor('white')
    ax.invert_yaxis()

    plt.tight_layout()

    # Salvar
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor='white')
    buf.seek(0)
    plt.close()

    print("[OK] Mapa mundial gerado")
    return buf

# ==============================================================================
# PROCESSAR MARKDOWN
# ==============================================================================

def parse_markdown_sections(md_content):
    """Extrai seções do markdown"""
    sections = []
    current_section = None

    for line in md_content.split('\n'):
        if line.startswith('## ') and not line.startswith('###'):
            if current_section:
                sections.append(current_section)
            title = line.replace('## ', '').strip()
            current_section = {'title': title, 'content': []}
        elif current_section is not None:
            if not line.startswith('# ') and line.strip() != '---':
                current_section['content'].append(line)

    if current_section:
        sections.append(current_section)

    return sections

# ==============================================================================
# CRIAR PDF
# ==============================================================================

def build_pdf(sections, chart_sales, chart_pie, chart_map):
    """Cria o PDF com reportlab"""
    print("[*] Construindo PDF...")

    # Criar documento
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        rightMargin=2.5*cm,
        leftMargin=2.5*cm,
        topMargin=2.5*cm,
        bottomMargin=3*cm,
    )

    # Estilos
    styles = getSampleStyleSheet()

    # Estilo customizado - Título da capa
    style_cover_title = ParagraphStyle(
        'CoverTitle',
        parent=styles['Title'],
        fontSize=36,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName='Helvetica-Bold',
    )

    # Estilo - Subtítulo da capa
    style_cover_subtitle = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontSize=16,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=30,
        fontName='Helvetica',
    )

    # Estilo - Seção
    style_section_title = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=COLORS['primary'],
        spaceAfter=15,
        spaceBefore=10,
        fontName='Helvetica-Bold',
        borderPadding=(0, 0, 5, 0),
        borderColor=COLORS['secondary'],
        borderWidth=2,
    )

    # Estilo - Texto normal
    style_body = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY,
        spaceAfter=10,
        fontName='Helvetica',
    )

    # Estilo - Bullet
    style_bullet = ParagraphStyle(
        'Bullet',
        parent=style_body,
        leftIndent=15,
        bulletIndent=5,
    )

    # Elementos do PDF
    story = []

    # ==================
    # CAPA
    # ==================
    # Criar capa com Table (para background azul)
    capa_data = [['']]
    capa_table = Table(capa_data, colWidths=[16*cm], rowHeights=[24*cm])
    capa_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COLORS['primary']),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))

    # Conteúdo da capa
    story.append(Spacer(1, 6*cm))
    story.append(Paragraph("TURMA DA AVENTURA", style_cover_title))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("Pitch Deck - Série de Livros Infantis de Viagem no Tempo", style_cover_subtitle))
    story.append(Spacer(1, 1*cm))

    tagline = ParagraphStyle('Tagline', parent=style_cover_subtitle, fontSize=14, fontName='Helvetica-Oblique')
    story.append(Paragraph('"Magic Tree House encontra Dog Man"', tagline))
    story.append(Spacer(1, 3*cm))

    date_style = ParagraphStyle('Date', parent=style_cover_subtitle, fontSize=12)
    story.append(Paragraph("Janeiro 2026", date_style))

    story.append(PageBreak())

    # ==================
    # CONTEÚDO - SEÇÕES
    # ==================

    for i, sec in enumerate(sections, 1):
        # Título da seção
        title_text = f"{i}. {sec['title']}"
        story.append(Paragraph(title_text, style_section_title))
        story.append(Spacer(1, 0.3*cm))

        # Conteúdo da seção (simplificado)
        content_text = '\n'.join(sec['content'])

        # Processar parágrafos
        for line in content_text.split('\n'):
            if not line.strip():
                continue

            # Pular linhas com tabelas markdown (por enquanto)
            if '|' in line and line.strip().startswith('|'):
                continue

            # Bullets
            if line.strip().startswith('- '):
                bullet_text = line.strip()[2:]
                # Processar bold corretamente
                bullet_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', bullet_text)
                story.append(Paragraph(f"• {bullet_text}", style_bullet))
            else:
                # Processar bold corretamente
                line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)
                if line.strip():
                    story.append(Paragraph(line, style_body))

        # Inserir gráficos nas seções apropriadas
        if "MERCADO: DADOS REAIS" in sec['title'].upper() or "ANÁLISE DE MERCADO" in sec['title'].upper():
            story.append(Spacer(1, 0.5*cm))
            img = Image(chart_sales, width=15*cm, height=6*cm)
            story.append(img)
            caption_style = ParagraphStyle('Caption', parent=style_body, fontSize=8, textColor=colors.grey, alignment=TA_CENTER, fontName='Helvetica-Oblique')
            story.append(Paragraph("Figura 1: Evolução de vendas mensais (dez/2023 - jan/2026)", caption_style))

        if "VALIDAÇÃO DE MERCADO" in sec['title'].upper():
            story.append(Spacer(1, 0.5*cm))
            img = Image(chart_map, width=15*cm, height=7*cm)
            story.append(img)
            caption_style = ParagraphStyle('Caption', parent=style_body, fontSize=8, textColor=colors.grey, alignment=TA_CENTER, fontName='Helvetica-Oblique')
            story.append(Paragraph("Figura 2: Presença em 10 mercados globais", caption_style))

            story.append(Spacer(1, 0.5*cm))
            img = Image(chart_pie, width=12*cm, height=9*cm)
            story.append(img)
            story.append(Paragraph("Figura 3: Distribuição percentual de vendas por mercado", caption_style))

        story.append(Spacer(1, 0.5*cm))
        story.append(PageBreak())

    # ==================
    # ÚLTIMA PÁGINA - CONTATO
    # ==================
    story.append(Paragraph("Contato", style_section_title))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("<b>Autor:</b> Guilherme Miranda de Aguiar", style_body))
    story.append(Paragraph("<b>Email:</b> [contato@exemplo.com]", style_body))
    story.append(Paragraph("<b>Website:</b> [www.turmadaaventura.com]", style_body))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("<b>Materiais Adicionais:</b>", style_body))
    story.append(Paragraph("• Pitch Completo: PITCH-DECK-TURMA-DA-AVENTURA.md", style_bullet))
    story.append(Paragraph("• Validação de Dados: VALIDACAO-DADOS-PITCH.md", style_bullet))
    story.append(Paragraph("• One-Pager: ONE-PAGER-TURMA-DA-AVENTURA.md", style_bullet))

    # Build PDF
    doc.build(story, canvasmaker=FooterCanvas)

    print(f"[OK] PDF gerado com sucesso: {OUTPUT_PDF}")

# ==============================================================================
# MAIN
# ==============================================================================

def main():
    print("=" * 80)
    print("GERADOR DE PITCH DECK PDF - TURMA DA AVENTURA")
    print("=" * 80)
    print()

    # Carregar dados
    df_resumo, df_vendas = load_kdp_data()
    md_content = load_pitch_content()

    # Gerar gráficos
    chart_sales = generate_sales_chart(df_resumo)
    chart_pie = generate_market_pie_chart(df_vendas)
    chart_map = generate_world_map(df_vendas)

    # Processar markdown
    sections = parse_markdown_sections(md_content)
    print(f"[OK] {len(sections)} secoes processadas")

    # Criar PDF
    build_pdf(sections, chart_sales, chart_pie, chart_map)

    print()
    print("=" * 80)
    print("PROCESSO CONCLUIDO COM SUCESSO!")
    print("=" * 80)
    print(f"[PDF] Arquivo salvo em: {OUTPUT_PDF}")
    print(f"[INFO] Tamanho estimado: ~25 paginas A4")
    print(f"[INFO] Estilo: Corporativo/Profissional")
    print(f"[INFO] Graficos incluidos: 3 visualizacoes de dados")
    print()

if __name__ == "__main__":
    main()
