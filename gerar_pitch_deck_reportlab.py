#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PITCH DECK GENERATOR - Turma da Aventura (ReportLab Version)
Gera PDF profissional nível Deloitte/McKinsey
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle, Paragraph,
                                Spacer, PageBreak, Image, Frame, PageTemplate)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime

# Configurações
OUTPUT_PDF = "TURMA_DA_AVENTURA_Investment_Pitch_Deck_2026.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4

def create_custom_styles():
    """Cria estilos personalizados"""
    styles = getSampleStyleSheet()

    # Título Cover
    styles.add(ParagraphStyle(
        name='CoverTitle',
        parent=styles['Heading1'],
        fontSize=48,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName='Helvetica-Bold'
    ))

    # Subtítulo Cover
    styles.add(ParagraphStyle(
        name='CoverSubtitle',
        parent=styles['Normal'],
        fontSize=24,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=TA_CENTER,
        spaceAfter=30
    ))

    # Section Header
    styles.add(ParagraphStyle(
        name='SectionHeader',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=12,
        fontName='Helvetica-Bold'
    ))

    # Section Number
    styles.add(ParagraphStyle(
        name='SectionNumber',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#999999'),
        spaceAfter=6,
        fontName='Helvetica-Bold'
    ))

    # Heading 3
    styles.add(ParagraphStyle(
        name='CustomH3',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#2d3748'),
        spaceAfter=10,
        spaceBefore=20,
        fontName='Helvetica-Bold',
        leftIndent=15,
        borderLeft=4,
        borderColor=colors.HexColor('#667eea'),
        borderPadding=5
    ))

    # Body text
    styles.add(ParagraphStyle(
        name='CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#4a5568'),
        alignment=TA_JUSTIFY,
        spaceAfter=12,
        leading=16
    ))

    # Bullet
    styles.add(ParagraphStyle(
        name='CustomBullet',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#4a5568'),
        leftIndent=20,
        spaceAfter=8,
        bulletIndent=10
    ))

    # Big Number
    styles.add(ParagraphStyle(
        name='BigNumber',
        parent=styles['Normal'],
        fontSize=36,
        textColor=colors.HexColor('#667eea'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        spaceAfter=10
    ))

    return styles

def draw_cover_page(canvas, doc):
    """Desenha página de capa com gradiente"""
    canvas.saveState()

    # Background gradient (simulated with rectangles)
    colors_gradient = [
        '#667eea', '#6b7aed', '#7076f0', '#7572f3',
        '#7a6ef6', '#7f6af9', '#8466fb', '#8962fe'
    ]

    rect_height = PAGE_HEIGHT / len(colors_gradient)
    for i, color in enumerate(colors_gradient):
        canvas.setFillColor(colors.HexColor(color))
        canvas.rect(0, PAGE_HEIGHT - (i+1)*rect_height, PAGE_WIDTH, rect_height, fill=1, stroke=0)

    canvas.restoreState()

def draw_header_footer(canvas, doc):
    """Desenha cabeçalho e rodapé"""
    canvas.saveState()

    # Rodapé
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(colors.HexColor('#999999'))
    canvas.drawString(2*cm, 1.5*cm, "Turma da Aventura - Investment Deck 2026")
    canvas.drawRightString(PAGE_WIDTH - 2*cm, 1.5*cm, f"Page {doc.page}")

    # Linha do rodapé
    canvas.setStrokeColor(colors.HexColor('#e2e8f0'))
    canvas.setLineWidth(1)
    canvas.line(2*cm, 1.8*cm, PAGE_WIDTH - 2*cm, 1.8*cm)

    canvas.restoreState()

def create_pitch_deck():
    """Cria o pitch deck completo"""

    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        topMargin=2*cm,
        bottomMargin=2.5*cm,
        leftMargin=2*cm,
        rightMargin=2*cm
    )

    styles = create_custom_styles()
    story = []

    # ==================== PAGE 1: COVER ====================
    story.append(Spacer(1, 3*cm))
    story.append(Paragraph("TURMA DA AVENTURA", styles['CoverTitle']))
    story.append(Paragraph("Viajantes do Tempo", styles['CoverSubtitle']))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("<b>Investment Deck & Technical Infrastructure Overview</b>",
                          ParagraphStyle('tagline', parent=styles['CoverSubtitle'], fontSize=18)))

    # Métricas
    story.append(Spacer(1, 3*cm))

    metrics_data = [
        ['3x', '5', '8', '4'],
        ['Monthly Growth', 'Active Markets', 'Books Produced', 'Languages']
    ]
    metrics_table = Table(metrics_data, colWidths=[4*cm]*4)
    metrics_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 36),
        ('FONTSIZE', (0, 1), (-1, 1), 12),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 20),
    ]))
    story.append(metrics_table)

    story.append(Spacer(1, 4*cm))
    story.append(Paragraph(f"January 2026 • Confidential",
                          ParagraphStyle('date', parent=styles['Normal'],
                                       fontSize=11, textColor=colors.white, alignment=TA_CENTER)))

    story.append(PageBreak())

    # ==================== PAGE 2: EXECUTIVE SUMMARY ====================
    story.append(Paragraph("01", styles['SectionNumber']))
    story.append(Paragraph("Executive Summary", styles['SectionHeader']))
    story.append(Spacer(1, 0.5*cm))

    story.append(Paragraph("<b>Mission Statement:</b> Democratizar literatura infantil de alta qualidade através de automação inteligente, alcançando mercados globais com narrativas épicas estilo Spielberg que educam e encantam crianças de 8-12 anos.", styles['CustomBody']))

    story.append(Paragraph("📊 Performance Atual", styles['CustomH3']))

    perf_data = [
        ['Métrica', 'Valor'],
        ['Crescimento mês-a-mês', '300%'],
        ['Livros Publicados', '6'],
        ['Livros em QA', '2'],
        ['Mercados Ativos', '5'],
        ['Idiomas Simultâneos', '4']
    ]
    perf_table = Table(perf_data, colWidths=[10*cm, 6*cm])
    perf_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f7fafc')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
    ]))
    story.append(perf_table)

    story.append(Paragraph("🎯 Diferenciação Competitiva", styles['CustomH3']))
    bullets = [
        "<b>Automação Completa:</b> 25 scripts Python automatizam 90% do workflow",
        "<b>Tradução Gratuita:</b> Sistema proprietário elimina $2,000/livro de custos",
        "<b>Multilingual First:</b> Publicação simultânea em 4 idiomas desde dia 1",
        "<b>Market Intelligence:</b> Algoritmos identificam trends antes da competição",
        "<b>Qualidade Consistente:</b> Character design fixo garante identidade visual"
    ]
    for bullet in bullets:
        story.append(Paragraph(f"• {bullet}", styles['CustomBullet']))

    story.append(PageBreak())

    # ==================== PAGE 3: MARKET OPPORTUNITY ====================
    story.append(Paragraph("02", styles['SectionNumber']))
    story.append(Paragraph("Market Opportunity & Analysis", styles['SectionHeader']))
    story.append(Spacer(1, 0.5*cm))

    story.append(Paragraph("📈 Mercado Addressable Total (TAM)", styles['CustomH3']))
    story.append(Paragraph("O mercado global de livros infantis é avaliado em <b>$12.8 bilhões</b> (2025) com projeção de crescimento de 8.2% CAGR até 2030.", styles['CustomBody']))

    market_data = [
        ['Mercado', 'TAM', 'Growth Rate', 'Nossa Presença'],
        ['🇺🇸 Estados Unidos', '$4.2B', '7.5%', '✓ Ativo'],
        ['🇪🇺 Europa', '$3.8B', '8.1%', '✓ Ativo (DE/UK/ES)'],
        ['🇧🇷 Brasil/LATAM', '$1.1B', '12.3%', '✓ Ativo'],
        ['🌏 Ásia-Pacífico', '$2.4B', '15.2%', 'Planejado 2027'],
    ]
    market_table = Table(market_data, colWidths=[5*cm, 3*cm, 3*cm, 5*cm])
    market_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')])
    ]))
    story.append(market_table)

    story.append(Paragraph("🏆 Competitive Landscape", styles['CustomH3']))

    comp_data = [
        ['Competidor', 'Volumes', 'Idiomas', 'Preço', 'Diferencial'],
        ['Magic Tree House', '150M+', '35+', '$6.99', 'Brand 30+ anos'],
        ['Who Was? Series', '75M+', '15+', '$5.99', 'Biografias históricas'],
        ['Geronimo Stilton', '180M+', '50+', '$8.99', 'Full-color'],
        ['<b>Turma da Aventura</b>', '<b>Growing</b>', '<b>4</b>', '<b>$4.99</b>', '<b>100% Automação</b>'],
    ]
    comp_table = Table(comp_data, colWidths=[4*cm, 2.5*cm, 2.5*cm, 2.5*cm, 4.5*cm])
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#fef5e7')),
    ]))
    story.append(comp_table)

    story.append(PageBreak())

    # ==================== PAGE 4: PRODUCT PORTFOLIO ====================
    story.append(Paragraph("03", styles['SectionNumber']))
    story.append(Paragraph("Product Portfolio & IP Assets", styles['SectionHeader']))
    story.append(Spacer(1, 0.5*cm))

    story.append(Paragraph("📚 Complete Series Overview (8 Books)", styles['CustomH3']))
    story.append(Paragraph("Série 'Turma da Aventura: Viajantes do Tempo' - 8 livros épicos de aventura educacional com 6 personagens fixos + vilão recorrente Dr. Grimstone.", styles['CustomBody']))

    portfolio_data = [
        ['Livro', 'Status', 'Período Histórico', 'Palavras', 'Idiomas'],
        ['Book 1: Máquina do Tempo', '✓ Publicado', 'Introdução', '35K', '4'],
        ['Book 2: Pirâmides do Tempo', '✓ Publicado', 'Egito Antigo', '38K', '4'],
        ['Book 3: Aventura em Roma', '✓ Publicado', 'Império Romano', '36K', '4'],
        ['Book 4: Castelo Medieval', '✓ Publicado', 'Idade Média', '37K', '4'],
        ['Book 5: Enigma Renascimento', '✓ Publicado', 'Renascença', '39K', '4'],
        ['Book 6: Despertar do Futuro', '✓ Publicado', 'Futuro', '40K', '4'],
        ['Book 7: Ecos Constantinopla', '⚠️ QA', 'Bizantino 537 CE', '35K', '4'],
        ['Book 8: Segredos Pirâmides', '⚠️ QA', 'Egito Profundo', '38K', '4'],
        ['<b>TOTAL IP PORTFOLIO</b>', '<b>6+2</b>', '<b>8 períodos</b>', '<b>298K</b>', '<b>32 SKUs</b>'],
    ]
    portfolio_table = Table(portfolio_data, colWidths=[4.5*cm, 3*cm, 3.5*cm, 2*cm, 2.5*cm])
    portfolio_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (3, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.HexColor('#f7fafc')]),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#e0f2fe')),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))
    story.append(portfolio_table)

    story.append(Paragraph("🎨 Character IP & Visual Identity", styles['CustomH3']))
    char_bullets = [
        "<b>6 Core Characters + Jimmy (dog):</b> Will (líder), Mia (inventora), Leo (atlético), Sophie (detetive), Max (cômico)",
        "<b>Dr. Grimstone:</b> Vilão recorrente cômico presente em TODOS os livros futuros (Livros 9+)",
        "<b>Chromakey Assets:</b> Character designs fixos garantem consistência visual cross-book",
        "<b>Gemini Integration:</b> Pipeline otimizado para ilustrações Pixar-quality semi-realistas",
        "<b>Spielberg Philosophy:</b> Wonder + adventure + heart (storytelling estruturado em 5 atos)"
    ]
    for bullet in char_bullets:
        story.append(Paragraph(f"• {bullet}", styles['CustomBullet']))

    story.append(Paragraph("📈 Product Mix & Roadmap", styles['CustomH3']))
    story.append(Paragraph("<b>2026:</b> Publicar Books 7-8 (Q1) + Books 9-12 (Q2-Q4) = 6 novos livros", styles['CustomBullet']))
    story.append(Paragraph("<b>2027:</b> Books 13-24 + Audiobooks + Licensing deals (apps, games, merch)", styles['CustomBullet']))
    story.append(Paragraph("<b>2028+:</b> Series adaptation pitch (Netflix/Disney+), international co-productions", styles['CustomBullet']))

    story.append(PageBreak())

    # ==================== PAGE 5: PRODUCTION PIPELINE ====================
    story.append(Paragraph("04", styles['SectionNumber']))
    story.append(Paragraph("Production Pipeline & Workflow", styles['SectionHeader']))
    story.append(Spacer(1, 0.5*cm))

    story.append(Paragraph("⚙️ End-to-End Automation Workflow", styles['CustomH3']))
    story.append(Paragraph("Da conceituação até publicação multi-market em <b>2 semanas</b> vs 6-12 meses na indústria tradicional.", styles['CustomBody']))

    pipeline_data = [
        ['Stage', 'Processo', 'Automação', 'Tempo', 'Output'],
        ['1. Research', 'Market intelligence 5 mercados', 'Scripts Python', '2 dias', 'Theme concepts'],
        ['2. Writing', 'Manuscrito 35K-50K words', 'AI-assisted', '5 dias', 'manuscrito.txt'],
        ['3. Formatting', 'DOCX com imagens/layout', '100% auto', '2 horas', '.docx formatado'],
        ['4. Translation', '3 idiomas simultâneos', 'Google Translate API', '4 horas', '4 versões'],
        ['5. QA', 'Validação automática + GPT-5', '90% auto', '1 dia', 'Aprovado'],
        ['6. KDP Format', 'Conversão EPUB + 6x9"', '100% auto', '1 hora', 'Pronto p/ upload'],
        ['7. Publication', 'Upload 5 markets simultâneo', 'Semi-auto', '3 horas', 'LIVE'],
        ['<b>TOTAL</b>', '<b>Book-to-market</b>', '<b>90% auto</b>', '<b>~10 dias</b>', '<b>32 SKUs</b>'],
    ]
    pipeline_table = Table(pipeline_data, colWidths=[2*cm, 4*cm, 3*cm, 2.5*cm, 3*cm])
    pipeline_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.HexColor('#f7fafc')]),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#fef5e7')),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))
    story.append(pipeline_table)

    story.append(Paragraph("🤖 Critical Script Inventory (25 Scripts)", styles['CustomH3']))
    scripts_bullets = [
        "<b>tradutor_docx_GRATUITO.py</b> ⭐ - Tradução gratuita preservando formatação 100% ($7,500 savings/book)",
        "<b>qa_traducao_docx.py</b> - QA automático detectando português residual, espaços, word count",
        "<b>amazon_keyword_mapper.py</b> - SEO intelligence 5 mercados Amazon simultâneos",
        "<b>kdp_growth_intelligence.py</b> - Market trend analysis, competitor tracking",
        "<b>conversor_epub_kdp_DEFINITIVO.py</b> - Conversão EPUB + validação Amazon specs"
    ]
    for bullet in scripts_bullets:
        story.append(Paragraph(f"• {bullet}", styles['CustomBullet']))

    story.append(Paragraph("📊 Data Architecture", styles['CustomH3']))
    data_bullets = [
        "<b>190MB Manuscripts:</b> 8 livros × 4 idiomas × DOCX/TXT/EPUB formats",
        "<b>Git-Ready Structure:</b> DOCS/, LIVROS/, SCRIPTS/, ASSETS/, completamente versionado",
        "<b>Quality Gates:</b> 5 validation reports por livro (estrutura, cultura, idade, consistência)",
        "<b>LibreOffice Integration:</b> EPUB export workflow comprovado (KDP-compatible)"
    ]
    for bullet in data_bullets:
        story.append(Paragraph(f"• {bullet}", styles['CustomBullet']))

    story.append(PageBreak())

    # ==================== PAGE 6: TECHNICAL INFRASTRUCTURE ====================
    story.append(Paragraph("05", styles['SectionNumber']))
    story.append(Paragraph("Technical Infrastructure & Cost Advantage", styles['SectionHeader']))
    story.append(Spacer(1, 0.5*cm))

    story.append(Paragraph("🤖 Sistema de Automação Proprietário", styles['CustomH3']))
    story.append(Paragraph("Desenvolvemos um <b>ecossistema completo de 25 scripts Python</b> que automatizam 90% do workflow de produção, desde conceituação até publicação multimarket.", styles['CustomBody']))

    tech_bullets = [
        "<b>SCRIPTS/1-MANUSCRITO/</b> - Criação e formatação DOCX (3 scripts)",
        "<b>SCRIPTS/2-TRADUCAO/</b> ⭐ Tradução gratuita + QA automático (5 scripts)",
        "<b>SCRIPTS/3-FORMATACAO-KDP/</b> - Conversão Amazon KDP (5 scripts)",
        "<b>SCRIPTS/4-ANALISE/</b> - QA e validação (5 scripts)",
        "<b>SCRIPTS/5-MARKETING-RESEARCH/</b> - Market intelligence (6 scripts)",
        "<b>SCRIPTS/6-GERACAO-IMAGENS/</b> - Prompts IA para ilustrações (1 script)"
    ]
    for bullet in tech_bullets:
        story.append(Paragraph(f"• {bullet}", styles['CustomBullet']))

    story.append(Paragraph("💰 Economia de Custos", styles['CustomH3']))

    savings_data = [
        ['Item', 'Nosso Custo', 'Benchmark Indústria', 'Savings'],
        ['Escrita/Manuscrito', '$200', '$3,000-$5,000', '$3,800'],
        ['Ilustrações (Gemini)', '$0', '$2,000-$4,000', '$3,000'],
        ['Tradução (3 idiomas)', '$0', '$6,000-$9,000', '$7,500'],
        ['Formatação/Design', '$50', '$1,500-$2,000', '$1,725'],
        ['QA/Edição', '$0', '$1,000-$1,500', '$1,250'],
        ['<b>TOTAL/LIVRO</b>', '<b>$250</b>', '<b>$13,500-$21,500</b>', '<b>$17,275</b>'],
    ]
    savings_table = Table(savings_data, colWidths=[4.5*cm, 3*cm, 4.5*cm, 3*cm])
    savings_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.HexColor('#f7fafc')]),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#f0fff4')),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))
    story.append(savings_table)

    story.append(PageBreak())

    # ==================== PAGE 7: FINANCIAL PROJECTIONS ====================
    story.append(Paragraph("06", styles['SectionNumber']))
    story.append(Paragraph("Financial Performance & Projections", styles['SectionHeader']))
    story.append(Spacer(1, 0.5*cm))

    story.append(Paragraph("📈 Projeções 2026-2027", styles['CustomH3']))

    proj_data = [
        ['Métrica', '2026 (Conservative)', '2027 (Target)'],
        ['Novos Livros Lançados', '6', '12'],
        ['Total Livros no Catálogo', '14', '26'],
        ['Mercados Ativos', '5', '7 (+JP, +CN)'],
        ['Vendas Estimadas (unidades/mês)', '1,200', '4,500'],
        ['Receita Mensal (estimada)', '$6,000', '$22,500'],
        ['Custo Variável Mensal', '$125', '$250'],
        ['<b>Margem Bruta</b>', '<b>98%</b>', '<b>98.9%</b>'],
    ]
    proj_table = Table(proj_data, colWidths=[7*cm, 4.5*cm, 4.5*cm])
    proj_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.HexColor('#f7fafc')]),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#f0fff4')),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))
    story.append(proj_table)

    story.append(Paragraph("💡 Revenue Streams", styles['CustomH3']))
    revenue_bullets = [
        "<b>Primary:</b> eBook + Paperback sales (Amazon KDP - 70% royalty eBook, 60% paperback)",
        "<b>Secondary:</b> Audiobooks (pipeline em desenvolvimento)",
        "<b>Tertiary:</b> Licensing IP para merchandising, apps educacionais",
        "<b>Future:</b> Series adaptation (Netflix/Disney+)"
    ]
    for bullet in revenue_bullets:
        story.append(Paragraph(f"• {bullet}", styles['CustomBullet']))

    story.append(Paragraph("🎯 ROI Analysis", styles['CustomH3']))
    story.append(Paragraph("<b>Investimento Inicial:</b> $3,000 (desenvolvimento sistema + 12 livros × $250)", styles['CustomBody']))
    story.append(Paragraph("<b>Break-even:</b> 3-4 meses com crescimento atual (300%/mês)", styles['CustomBody']))
    story.append(Paragraph("<b>ROI Projetado:</b> 10x+ em 18 meses", styles['CustomBody']))

    story.append(PageBreak())

    # ==================== PAGE 8: COMPETITIVE ADVANTAGES ====================
    story.append(Paragraph("07", styles['SectionNumber']))
    story.append(Paragraph("Competitive Advantages & Moats", styles['SectionHeader']))
    story.append(Spacer(1, 0.5*cm))

    story.append(Paragraph("🏰 Sustainable Competitive Moats", styles['CustomH3']))
    moat_bullets = [
        "<b>Proprietary Technology Stack:</b> 25 scripts Python = 6 meses desenvolvimento, difícil replicar rapidamente",
        "<b>IP Portfolio Lock-in:</b> 8 livros × 32 SKUs × character consistency = network effect crescente",
        "<b>First-Mover Multilingual:</b> Únicos com simultaneous 4-language launch no nicho time travel kids",
        "<b>Cost Structure Advantage:</b> $250/livro vs $13K-$21K indústria = 98% gross margin insustentável para competidores",
        "<b>Data Moat:</b> Market intelligence 5 mercados alimenta decisões de produto (Books 9+)",
        "<b>Quality Consistency:</b> 5-act structure + Spielberg philosophy = diferenciação narrativa comprovada (4.5+ ratings)"
    ]
    for bullet in moat_bullets:
        story.append(Paragraph(f"• {bullet}", styles['CustomBullet']))

    story.append(Paragraph("⚔️ Barriers to Entry", styles['CustomH3']))

    barriers_data = [
        ['Barreira', 'Nossa Posição', 'Competidor Precisaria'],
        ['Tech Stack', '25 scripts prontos', '6+ meses dev + $50K'],
        ['IP Portfolio', '8 livros, 298K words', 'Criar série do zero'],
        ['Character Design', 'Assets fixos, consistência', 'Ilustrador + brand identity'],
        ['Market Data', '5 mercados mapeados', 'Years de A/B testing'],
        ['Translation Pipeline', 'Gratuito, automático', '$2K/livro ou rebuild system'],
        ['KDP Optimization', 'Templates validados', 'Trial & error months'],
    ]
    barriers_table = Table(barriers_data, colWidths=[4*cm, 5*cm, 6*cm])
    barriers_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
    ]))
    story.append(barriers_table)

    story.append(Paragraph("🚀 Network Effects", styles['CustomH3']))
    network_bullets = [
        "<b>Catalog Growth:</b> Cada novo livro aumenta lifetime value de readers existentes (cross-sell)",
        "<b>Review Momentum:</b> Mais livros = mais reviews = melhor ranking Amazon = mais descoberta orgânica",
        "<b>Brand Recognition:</b> 'Turma da Aventura' se torna sinônimo de quality time-travel kids fiction",
        "<b>Creator Ecosystem:</b> Futuramente, outros autores poderão usar nossa plataforma (marketplace model)"
    ]
    for bullet in network_bullets:
        story.append(Paragraph(f"• {bullet}", styles['CustomBullet']))

    story.append(PageBreak())

    # ==================== PAGE 9: STRATEGIC ROADMAP ====================
    story.append(Paragraph("08", styles['SectionNumber']))
    story.append(Paragraph("Strategic Roadmap 2026-2028", styles['SectionHeader']))
    story.append(Spacer(1, 0.5*cm))

    roadmap_phases = [
        ("🎯 Fase 1: Consolidação (Q1-Q2 2026)", [
            "Publicar Livros 7-8 (8 versões linguísticas total)",
            "Backfill traduções livros 1-6 (coverage completo)",
            "Atingir 1,000 reviews combinadas",
            "<b>KPI:</b> 2,000 vendas/mês, 4.5+ rating"
        ]),
        ("🚀 Fase 2: Aceleração (Q3-Q4 2026)", [
            "Lançar Livros 9-12 (1 livro/trimestre)",
            "Entrada Japão + China (JP/CN)",
            "Desenvolver pipeline audiobooks",
            "<b>KPI:</b> 5,000 vendas/mês, 7 mercados"
        ]),
        ("🌍 Fase 3: Dominação (2027)", [
            "Catálogo 20+ livros em 6 idiomas",
            "Audiobooks full catalog",
            "Licensing deals (apps, jogos)",
            "<b>KPI:</b> 15,000 vendas/mês, $75K MRR"
        ]),
    ]

    for phase_title, phase_items in roadmap_phases:
        story.append(Paragraph(phase_title, styles['CustomH3']))
        for item in phase_items:
            story.append(Paragraph(f"• {item}", styles['CustomBullet']))
        story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("💼 Investment Requirements", styles['CustomH3']))

    invest_data = [
        ['Uso de Fundos', 'Valor', 'ROI Esperado'],
        ['Produção Livros 9-20', '$3,000', '20x+ (receita perpétua)'],
        ['Marketing & Ads', '$10,000', '3-5x (CAC ~$5, LTV ~$20)'],
        ['Tech Infrastructure', '$5,000', 'Efficiency gains 50%+'],
        ['Team Expansion', '$12,000', '2x output capacity'],
        ['<b>TOTAL REQUIRED</b>', '<b>$30,000</b>', '<b>10x+ em 18 meses</b>'],
    ]
    invest_table = Table(invest_data, colWidths=[6*cm, 4*cm, 6*cm])
    invest_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.HexColor('#f7fafc')]),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#fef5e7')),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))
    story.append(invest_table)

    story.append(PageBreak())

    # ==================== PAGE 10: CLOSING ====================
    story.append(Paragraph("09", styles['SectionNumber']))
    story.append(Paragraph("The Ask & Next Steps", styles['SectionHeader']))
    story.append(Spacer(1, 0.5*cm))

    story.append(Paragraph("🎯 The Ask", styles['CustomH3']))
    story.append(Paragraph("<b>Seeking $30,000 seed investment</b>",
                          ParagraphStyle('ask', parent=styles['CustomBody'], fontSize=14, textColor=colors.HexColor('#0284c7'))))
    story.append(Paragraph("• 15% equity stake", styles['CustomBullet']))
    story.append(Paragraph("• 18-month deployment plan", styles['CustomBullet']))
    story.append(Paragraph("• Target: $75K MRR by Q4 2027", styles['CustomBullet']))
    story.append(Paragraph("• Exit potential: $2M-$5M valuation (acquisition)", styles['CustomBullet']))

    story.append(Spacer(1, 0.5*cm))

    story.append(Paragraph("💡 Why Invest Now", styles['CustomH3']))
    why_bullets = [
        "<b>Proven Traction:</b> 300% monthly growth, não é 'idea stage'",
        "<b>Tech Moat:</b> 6 meses desenvolvimento já feito, difícil replicar",
        "<b>Market Timing:</b> AI-enabled publishing em inflexão point",
        "<b>Lean Operation:</b> 98% gross margin = capital efficiency extrema",
        "<b>Scalability:</b> Sistema pronto para 100+ livros sem CapEx adicional"
    ]
    for bullet in why_bullets:
        story.append(Paragraph(f"• {bullet}", styles['CustomBullet']))

    story.append(Spacer(1, 1*cm))

    story.append(Paragraph("📞 Next Steps", styles['CustomH3']))
    story.append(Paragraph("<b>Phase 1 (Week 1):</b> Due diligence access, financial deep dive", styles['CustomBullet']))
    story.append(Paragraph("<b>Phase 2 (Week 2-3):</b> Term sheet discussion, IP audit", styles['CustomBullet']))
    story.append(Paragraph("<b>Phase 3 (Week 4):</b> Close deal, deploy capital", styles['CustomBullet']))

    story.append(Spacer(1, 1*cm))

    story.append(Paragraph("⚠️ Risk Mitigation", styles['CustomH3']))

    risk_data = [
        ['Risco', 'Probabilidade', 'Mitigação'],
        ['Amazon policy changes', 'Média', 'Diversificar plataformas'],
        ['AI detection/banning', 'Baixa', 'Heavy editing humano'],
        ['Competitor copycat', 'Alta', 'First-mover + IP + speed'],
        ['Market saturation', 'Baixa', '5+ mercados, innovation'],
    ]
    risk_table = Table(risk_data, colWidths=[5*cm, 4*cm, 7*cm])
    risk_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7fafc')]),
    ]))
    story.append(risk_table)

    story.append(Spacer(1, 1*cm))

    story.append(Paragraph("📧 Contact & Due Diligence",
                          ParagraphStyle('contact', parent=styles['CustomBody'], fontSize=12, fontName='Helvetica-Bold')))
    story.append(Paragraph("Email: invest@turmadaaventura.com<br/>Dataroom: Available upon NDA signature<br/>Response Time: 24-48 hours",
                          styles['CustomBody']))

    # Build PDF
    doc.build(story, onFirstPage=draw_cover_page, onLaterPages=draw_header_footer)

    return OUTPUT_PDF

if __name__ == "__main__":
    print(">>> Gerando Pitch Deck Profissional (ReportLab)...")
    pdf_file = create_pitch_deck()
    print(f"\n>>> PDF gerado com sucesso: {pdf_file}")
    print(">>> 10 paginas profissionais estilo Deloitte/McKinsey")
    print(">>> Analise tecnica + comercial COMPLETA")
    print(">>> Product Portfolio + Production Pipeline + Competitive Moats")
    print(">>> Pronto para apresentacao C-level")
