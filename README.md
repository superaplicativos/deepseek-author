# 📚 Turma da Aventura - Books Production Automation

<div align="center">

> **A children's book series with 18 published titles across 4 languages and 5 markets**
>
> This repository contains the complete automation infrastructure for producing "Turma da Aventura" (Adventure Team) books.

[![Books Published](https://img.shields.io/badge/Books%20Published-18-success)](#-published-books-overview)
[![Languages](https://img.shields.io/badge/Languages-4-blue)](#-quick-start)
[![Series](https://img.shields.io/badge/Series-4-orange)](#-published-books-overview)
[![Markets](https://img.shields.io/badge/Markets-5-green)](#-business-metrics)

</div>

---

## 🎯 What This Project Is

**Turma da Aventura** is a multi-series children's book brand creating epic Spielberg-style adventures for kids aged 7-12. This repository is the **production automation system** that powers the entire operation.

### Current Status (January 2026)
- ✅ **18 books published** on Amazon KDP
- 📚 **4 active series**: Lugares Incríveis, Viajantes do Tempo, Valores e Emoções, Standalone
- 🌍 **5 markets**: USA, Brazil, Germany, UK, Spain
- 🗣️ **4 languages**: Portuguese, English, German, Spanish
- 📝 **2 books in production**: Lugares Incríveis #3 (Pirâmides)

> **Note**: This repository is for **AUTOMATION AND PRODUCTION**. Most books are already published on Amazon KDP but not stored here - we store the tools and infrastructure used to create them.

---

## 📖 Published Books Overview

### Series Breakdown

| Series | Books | Languages | Status |
|--------|-------|-----------|--------|
| **🏛️ Lugares Incríveis** (Incredible Places) | 2 | PT, EN | ✅ Published |
| **🕐 Viajantes do Tempo** (Time Travelers) | 6 | PT, EN, ES, DE | ✅ Published |
| **❤️ Valores e Emoções** (Values & Emotions) | 8 | PT, EN | ✅ Published |
| **📕 Standalone Adventures** | 2 | PT, EN | ✅ Published |
| **TOTAL** | **18** | **4 languages** | **30+ editions** |

### 🏛️ SÉRIE LUGARES INCRÍVEIS (Incredible Places)
Epic adventures in iconic historical and mythical **LOCATIONS**.

1. **O Segredo de Atlântida** / The Secret of Atlantis (Sept 2025)
2. **Os Ecos de Constantinopla** / The Echoes of Constantinople (Jan 2026)
3. **Os Segredos das Pirâmides** *(in production)*

### 🕐 SÉRIE VIAJANTES DO TEMPO (Time Travelers)
Time travel adventures through historical **PERIODS**.

1. **A Máquina do Tempo** / The Time Machine (Jul 2025) - 4 languages
2. **As Pirâmides do Tempo** / The Pyramids of Time (Jul-Nov 2025) - 4 languages
3. **Uma Aventura em Roma** / An Adventure in Rome (Jul-Nov 2025) - 4 languages
4. **Mistério no Castelo Medieval** / Mystery in the Medieval Castle (Sept-Nov 2025) - 4 languages
5. **Enigma no Renascimento** / Enigma in the Renaissance (Sept-Nov 2025) - 4 languages
6. **O Despertar dos Sonhos no Futuro** / The Awakening of Dreams in the Future (Oct-Nov 2025) - 4 languages

**Note**: Dr. Grimstone (villain) is **MANDATORY** in all Time Travelers books.

### ❤️ SÉRIE VALORES E EMOÇÕES (Values & Emotions)
Books teaching emotional intelligence, values, and life skills.

1-8. Various titles focused on: Creativity, Overcoming Fears, Self-esteem, Anger Management, Problem Solving, Obedience, Patience, Emotions

### 📕 STANDALONE BOOKS
Individual adventure stories outside the main series.

1. **O Enigma do Explorador Perdido** / The Riddle of the Lost Explorer (Jan 2025)
2. **Viagem no Tempo: A Missão...** / Time Travel: The Mission... (Sept 2024 - Jan 2025)

For complete list of all published books, see [todoslivros.txt](todoslivros.txt).

---

## 🛠️ Repository Structure

This repo is organized for **production automation**, not book storage:

```
BIZANTINO/
│
├── 📁 DIRETRIZES/                  # Writing guidelines (CRITICAL for quality)
│   ├── PERSONAGENS-FIXOS.txt       # Character specs (NEVER change)
│   ├── ESTILO-SPIELBERG.txt        # Storytelling principles
│   ├── ESTRUTURA-NARRATIVA.txt     # 5-act structure
│   ├── SERIE-VIAJANTES-DO-TEMPO.txt
│   ├── SERIE-LUGARES-INCRIVEIS.txt
│   ├── SERIE-INVENCOES.txt         # (future series)
│   ├── SERIE-MISTERIOS.txt         # (future series)
│   └── SERIE-CIENCIA.txt           # (future series)
│
├── 📁 LIVROS/                      # Books organized by series
│   ├── SERIE-VIAJANTES-DO-TEMPO/   # 6 books (published)
│   ├── SERIE-LUGARES-INCRIVEIS/    # 2 books published + 1 in production
│   ├── SERIE-INVENCOES/            # (future)
│   ├── SERIE-MISTERIOS/            # (future)
│   └── SERIE-CIENCIA/              # (future)
│
├── 📁 SCRIPTS/                     # Automation tools
│   ├── 1-MANUSCRITO/               # Manuscript → DOCX conversion
│   ├── 2-TRADUCAO/                 # Automated translation
│   ├── 3-FORMATACAO-KDP/           # Amazon KDP formatting
│   ├── 4-ANALISE/                  # Analysis tools
│   ├── 5-MARKETING-RESEARCH/       # Market research
│   └── 6-GERACAO-IMAGENS/          # Image generation prompts
│
├── 📁 INTELIGENCIA-DE-MERCADO/     # Market research tools
│   └── pesquisa_novas_series.py    # Research for new series
│
├── 📁 DOCS/                        # Documentation
│   ├── CLAUDE.md                   # Complete project guide for AI
│   ├── DIRETRIZES_QUALIDADE_SERIE.md  # Quality standards
│   └── DIRETRIZES_VISUAIS_IDENTIDADE.md  # Visual identity
│
└── 📁 PERSONAGENS-CHROMAKEY/       # Character assets
```

---

## 🚀 Quick Start

### Prerequisites

```bash
pip install python-docx pandas openpyxl deep-translator requests ebooklib lxml beautifulsoup4
```

### 1. Generate Book DOCX from Manuscript

**For Pirâmides (currently in production):**
```bash
cd SCRIPTS/1-MANUSCRITO
python create_docx_egito.py
```

Generates DOCX in: `LIVROS/SERIE-LUGARES-INCRIVEIS/LIVRO-03-PIRAMIDES/PT/`

**For other books:**
```bash
python create_docx_generic.py [book_path]
```

### 2. Translate to Multiple Languages

```bash
cd SCRIPTS/2-TRADUCAO

# Translate to English
python tradutor_docx_GRATUITO.py livro.docx en

# Translate to Spanish
python tradutor_docx_GRATUITO.py livro.docx es

# Translate to German
python tradutor_docx_GRATUITO.py livro.docx de
```

### 3. Market Research for New Series

```bash
cd INTELIGENCIA-DE-MERCADO

# Research for planned series
python pesquisa_novas_series.py invencoes  # Inventions
python pesquisa_novas_series.py misterios  # Mysteries
python pesquisa_novas_series.py ciencia    # Science

# All at once
python pesquisa_novas_series.py all
```

### 4. Using DIRETRIZES (Guidelines)

When writing a new book in any IDE, reference the guidelines:

```
Follow these guidelines:
D:\path\DIRETRIZES\PERSONAGENS-FIXOS.txt
D:\path\DIRETRIZES\ESTILO-SPIELBERG.txt
D:\path\DIRETRIZES\ESTRUTURA-NARRATIVA.txt
D:\path\DIRETRIZES\SERIE-[NOME].txt
```

**CRITICAL**: Copy the guideline file path and paste into your AI assistant context before writing.

---

## 👥 Core Characters

**The Adventure Team** - 6 characters + AI + dog (FIXED in ALL books)

| Character | Age | Role | Visual Marker |
|-----------|-----|------|---------------|
| **Will** | 9 | Leader, tech-savvy | Smartphone with Íris AI |
| **Mia** | 8 | Inventor | Tool belt with gadgets |
| **Leo** | 10 | Athletic protector | Green shirt, backpack |
| **Sophie** | 8 | Detective | Yellow dress, notebook |
| **Max** | 7 | Comic relief | Red shirt, animal lover |
| **Íris** | AI | Assistant | Holographic AI |
| **Jimmy Hendrix** | - | Mascot | Border Collie (brown/white) |

**Recurring Villain:**
- **Dr. Grimstone** - Wants to "end children's imagination"
  - Viajantes do Tempo: ✅ **MANDATORY** in all books
  - Lugares Incríveis: ❌ Not in books 1-3 (series-specific villains)
  - Future series: TBD

> **⚠️ CRITICAL**: Character specs are FIXED. See [DIRETRIZES/PERSONAGENS-FIXOS.txt](DIRETRIZES/PERSONAGENS-FIXOS.txt)

---

## 📋 Guidelines System

All books follow **strict quality standards** defined in `DIRETRIZES/`:

### Common Guidelines (All Series)
- **PERSONAGENS-FIXOS.txt** - Character specifications (NEVER change)
- **ESTILO-SPIELBERG.txt** - Storytelling principles
- **ESTRUTURA-NARRATIVA.txt** - Mandatory 5-act structure

### Series-Specific Guidelines
- **SERIE-VIAJANTES-DO-TEMPO.txt** - Time travel rules, historical accuracy
- **SERIE-LUGARES-INCRIVEIS.txt** - Iconic locations, cultural sensitivity
- **SERIE-INVENCOES.txt** - STEM focus, inventions timeline *(future)*
- **SERIE-MISTERIOS.txt** - Investigation methods, critical thinking *(future)*
- **SERIE-CIENCIA.txt** - Scientific method, discoveries *(future)*

### Quality Requirements
- **Length**: 35,000-50,000 words per book
- **Pages**: 100+ pages in DOCX format
- **Chapters**: 10-15 chapters
- **Age Target**: 7-12 years (varies by series)

---

## 📊 Business Metrics

### Publication Statistics
- **Total unique titles**: 18 books
- **Total publications** (including translations): 30+ editions
- **Markets covered**: 5 countries (USA, Brazil, Germany, UK, Spain)
- **Languages**: Portuguese, English, Spanish, German
- **Age range**: 7-12 years (varies by series)
- **Average book length**: 35,000-50,000 words

### Publication Timeline
- **2024**: 1 book (Time Travel standalone)
- **Early 2025**: 8 books (Valores series)
- **Jul-Nov 2025**: 6 books (Viajantes series, 4 languages each)
- **Sept 2025**: 1 book (Atlântida)
- **Jan 2026**: 1 book (Constantinopla)
- **2026 Q1**: Pirâmides (in production)

### Publication Strategy

| Market | Amazon Store | Language | Status |
|--------|--------------|----------|--------|
| 🇺🇸 USA | amazon.com | English | ✅ 18 books |
| 🇧🇷 Brazil | amazon.com.br | Portuguese | ✅ 18 books |
| 🇩🇪 Germany | amazon.de | German | ✅ 6 books |
| 🇬🇧 UK | amazon.co.uk | English | ✅ 18 books |
| 🇪🇸 Spain | amazon.es | Spanish | ✅ 6 books |

**Strategy**: Simultaneous publication in multiple languages to maximize reach.

---

## 🎬 Storytelling Philosophy

### Spielberg-Style Adventure

Inspired by **Steven Spielberg's adventure films** (E.T., Indiana Jones, Jurassic Park):

| Principle | Description |
|-----------|-------------|
| ✨ **Sense of Wonder** | Evoke childlike discovery and awe |
| 🦸 **Children as Heroes** | Kids solve problems with intelligence & heart |
| 🎭 **Epic Yet Accessible** | Grand adventures at child's eye level |
| 🎪 **Mix of Tones** | Blend humor, emotion, and action |
| 🎥 **Cinematic Storytelling** | Write scenes like film sequences |
| ❤️ **Heart and Friendship** | Teamwork conquers all challenges |

### Mandatory 5-Act Structure

| Act | Percentage | Purpose |
|-----|------------|---------|
| 1. Introdução | 15-20% | Hook, mystery, conflict introduction |
| 2. Exploração | 30-35% | Investigation, teamwork, tension |
| 3. Conflito Principal | 20-25% | Peak tension, villain appearance |
| 4. Resolução Criativa | 15-20% | Solution through teamwork |
| 5. Encerramento | 10-15% | Lesson learned, satisfaction |

See [DIRETRIZES/ESTRUTURA-NARRATIVA.txt](DIRETRIZES/ESTRUTURA-NARRATIVA.txt) for complete details.

---

## 🔮 Planned Series (2026+)

Based on market research and Amazon SEO analysis:

### 🔧 SÉRIE INVENÇÕES (Inventions) - PLANNED
**Theme**: World-changing inventions | **Focus**: STEM education
- The Wheel, Printing Press, Light Bulb, Airplane, Internet, Vaccines, etc.
- **Guidelines**: [DIRETRIZES/SERIE-INVENCOES.txt](DIRETRIZES/SERIE-INVENCOES.txt)
- **Market Research**: High demand in USA and Germany

### 🔍 SÉRIE MISTÉRIOS (Mysteries) - PLANNED
**Theme**: Unsolved historical mysteries | **Focus**: Critical thinking
- Stonehenge, Bermuda Triangle, Nazca Lines, Atlantis myths, etc.
- **Guidelines**: [DIRETRIZES/SERIE-MISTERIOS.txt](DIRETRIZES/SERIE-MISTERIOS.txt)
- **Market Research**: Strong engagement in UK and USA

### ⚗️ SÉRIE CIÊNCIA (Science) - PLANNED
**Theme**: Scientific discoveries | **Focus**: Scientific method
- Gravity, DNA, Evolution, Radioactivity, Big Bang, etc.
- **Guidelines**: [DIRETRIZES/SERIE-CIENCIA.txt](DIRETRIZES/SERIE-CIENCIA.txt)
- **Market Research**: Educational market opportunity

Use `python pesquisa_novas_series.py [serie]` to run detailed market analysis.

---

## 🤝 Contributing

This is a **private repository**. For internal team members:

### Development Workflow
1. **Follow the guidelines** in `DIRETRIZES/` for your series
2. **Use the automation scripts** in `SCRIPTS/` for all operations
3. **Document everything** - update DOCS if you add features
4. **Test before committing** - verify DOCX generation works
5. **Never commit directly to main** - use feature branches

### Writing a New Book
1. Read the series-specific guideline in `DIRETRIZES/SERIE-[NAME].txt`
2. Read the common guidelines (PERSONAGENS-FIXOS, ESTILO-SPIELBERG, ESTRUTURA-NARRATIVA)
3. Create manuscript in `LIVROS/SERIE-[NAME]/LIVRO-XX-[TITLE]/PT/manuscrito.txt`
4. Generate DOCX using scripts in `SCRIPTS/1-MANUSCRITO/`
5. Translate using scripts in `SCRIPTS/2-TRADUCAO/`
6. Format for KDP using scripts in `SCRIPTS/3-FORMATACAO-KDP/`

---

## 📄 Documentation

| File | Purpose |
|------|---------|
| [DOCS/CLAUDE.md](DOCS/CLAUDE.md) | Complete project guide for AI assistants |
| [DOCS/DIRETRIZES_QUALIDADE_SERIE.md](DOCS/DIRETRIZES_QUALIDADE_SERIE.md) | Quality standards and best practices |
| [DOCS/DIRETRIZES_VISUAIS_IDENTIDADE.md](DOCS/DIRETRIZES_VISUAIS_IDENTIDADE.md) | Visual identity guidelines |
| [DIRETRIZES/README.md](DIRETRIZES/README.md) | Guidelines index |
| [todoslivros.txt](todoslivros.txt) | Complete list of ALL published books on Amazon KDP |

---

## 🛠️ Dependencies

### Python Requirements

```bash
pip install python-docx pandas openpyxl deep-translator requests ebooklib lxml beautifulsoup4
```

### External Tools
- **LibreOffice Writer** - EPUB export for Amazon KDP
- **Gemini (Google AI Studio)** - Illustration generation
- **Amazon KDP** - Publishing platform

---

## 🎯 Roadmap

### ✅ Completed (2025-2026)
- ✅ Published 18 books across 4 series
- ✅ Created automation infrastructure
- ✅ Established 4-language publication strategy
- ✅ Organized series-based structure
- ✅ Created centralized DIRETRIZES system

### 🔄 In Progress (2026 Q1)
- 🔄 Finalize Lugares Incríveis Book 3 (Pirâmides)
- 🔄 Publish Pirâmides on Amazon (4 languages, 5 markets)

### 📝 Planned (2026 Q2-Q4)
- 📝 Conduct market research for new series (Invenções, Mistérios, Ciência)
- 📝 Select first new series to launch based on market data
- 📝 Write and publish Lugares Incríveis Book 4
- 📝 Expand to new series based on market demand

---

## 📝 What This Repository IS and ISN'T

### ✅ THIS REPOSITORY IS:
- **Automation tools** for creating new books efficiently
- **Guidelines** for maintaining quality and consistency across all series
- **Scripts** for translation, formatting, and market research
- **Production environment** for books currently being written
- **Documentation** of the entire production process and best practices

### ❌ THIS REPOSITORY IS NOT:
- A complete archive of all published books (most are on Amazon KDP)
- The only place where books exist (manuscripts may be in Google Drive)
- A backup of all book versions (backups are elsewhere)

**Why?** Most books were created before this automation system existed. This repo was created to **streamline future production** and ensure consistency going forward.

---

## 📞 Contact

**Project Owner**: Guilherme Miranda de Aguiar
**Repository**: Private - https://github.com/superaplicativos/books-company
**Published Books**: Available on Amazon (USA, Brazil, Germany, UK, Spain)

---

## 📄 License

**© 2024-2026 Turma da Aventura**
All rights reserved.

**Proprietary** - Characters, stories, and brand are protected intellectual property.

---

<div align="center">

**Turma da Aventura - Adventure Team**
*18 books published • 4 languages • 5 markets • Growing every month*

---

**Last Update**: 2026-01-11
**Version**: 4.0 (GitHub Production Version)

---

Made with ❤️ for children • Sold on Amazon worldwide

🤖 *This README was crafted with Claude Code*

</div>
