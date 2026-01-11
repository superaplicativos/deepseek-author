# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**📌 DOCUMENTOS CRÍTICOS:**
- **DIRETRIZES_QUALIDADE_SERIE.md** - Checklist definitiva, especificações visuais, elementos obrigatórios por capítulo, processo de QA
- **DIRETRIZES_VISUAIS_IDENTIDADE.md** - Criação de capas/ilustrações, prompts Gemini, consistência visual 100%, specs Amazon KDP

## 📊 Executive Summary

**Project:** Turma da Aventura - Multiple Series (Adventure Team)
**Type:** Children's book series (ages 8-12)
**Status:** 8 books total - 6 published (Viajantes do Tempo), 2 in QA (Lugares Incríveis 2-3), expanding with multiple series
**Performance:** Sales tripling monthly across all markets
**Markets:** USA, Brazil, Germany, UK, Spain (5 primary markets)
**Languages:** Portuguese (original), English, German, Spanish (simultaneous publication)

**Series Overview:**
- **SÉRIE VIAJANTES DO TEMPO:** Books 1-6 (published) - Focus on historical PERIODS
- **SÉRIE LUGARES INCRÍVEIS:** Books 1-3 (Book 1 on Google Drive, Books 2-3 in QA) - Focus on iconic LOCATIONS
- **Future Series:** Invenções, Mistérios, Ciência (in planning)

**Published & Available:**
- Viajantes do Tempo Books 1-6: Published and selling on Amazon

**Books in QA:**
- Lugares Incríveis Book 2: "Os Ecos de Constantinopla" (The Echoes of Constantinople) - ⚠️ QA in progress
- Lugares Incríveis Book 3: "Os Segredos das Pirâmides" (The Secrets of the Pyramids) - ⚠️ QA in progress

**Key Success Factors:**
- ✅ Epic, intense, extensive books (100+ DOCX pages, 35,000-50,000 words)
- ✅ Spielberg-style storytelling (wonder, adventure, heart, friendship)
- ✅ Market research-driven themes aligned with Amazon bestseller trends
- ✅ Simultaneous multilingual publication strategy
- ✅ Automated translation + GPT-5 QA workflow
- ✅ Fixed character consistency across all books and languages
- ✅ Five-act narrative structure with educational elements

**Current Focus:** Planning Lugares Incríveis Book 4+ and launching new series (Invenções, Mistérios, Ciência) based on market research

**⚠️ IMPORTANTE - Dr. Grimstone por Série:**
- **Viajantes do Tempo (1-6):** Dr. Grimstone OBRIGATÓRIO em todos os livros
- **Lugares Incríveis (1-3):** SEM Dr. Grimstone (vilões específicos aprovados)
- **Lugares Incríveis (4+):** Dr. Grimstone retorna como OBRIGATÓRIO
- Ver DIRETRIZES/ para detalhes de cada série

## Project Overview

This repository manages the **Turma da Aventura** (Adventure Team) children's book brand with **multiple thematic series**. The brand has achieved exceptional commercial success, with sales tripling monthly across US and European markets. Books are published simultaneously in **Portuguese, English, German, and Spanish**.

### Complete Book Catalog

#### SÉRIE VIAJANTES DO TEMPO (Published, Books 1-6)
**Theme:** Time travel through historical PERIODS

1. **Turma da Aventura e a Máquina do Tempo** - Introduction to time travel mechanics
2. **Turma da Aventura e as Pirâmides do Tempo** - Egyptian adventure
3. **Uma Aventura em Roma** - Roman Empire exploration
4. **Mistério no Castelo Medieval** - Medieval mystery
5. **Enigma no Renascimento** - Renaissance period
6. **O Despertar dos Sonhos no Futuro** - Future timeline

**Location:** `LIVROS/SERIE-VIAJANTES-DO-TEMPO/`

#### SÉRIE LUGARES INCRÍVEIS (Books 1-3)
**Theme:** Exploration of iconic historical/mythical LOCATIONS

1. **Atlântida** (The Lost City of Atlantis)
   - Status: ⚠️ **On Google Drive - needs import to repository**
   - Theme: Lost civilization, advanced technology
   - Location: To be imported to `LIVROS/SERIE-LUGARES-INCRIVEIS/LIVRO-01-ATLANTIDA/`

2. **Os Ecos de Constantinopla** (The Echoes of Constantinople)
   - Byzantine Empire, 537 CE
   - Hagia Sophia cathedral construction
   - Atlantean crystal technology integration
   - New character: Theodora (street orphan guardian through centuries)
   - ~35,000 words, 10 chapters
   - Status: ⚠️ **QA in progress - NOT YET PUBLISHED**
   - Location: `LIVROS/SERIE-LUGARES-INCRIVEIS/LIVRO-02-CONSTANTINOPLA/PT/`

3. **Os Segredos das Pirâmides** (The Secrets of the Pyramids)
   - Ancient Egypt, 2560 BCE, Great Pyramid of Giza
   - Pyramid mysteries and Atlantean technology
   - New characters: Nadia (guardian), Khenti, O Primeiro (ancient consciousness)
   - ~35,000 words, 10 chapters
   - Status: ⚠️ **QA in progress - NOT YET PUBLISHED**
   - Location: `LIVROS/SERIE-LUGARES-INCRIVEIS/LIVRO-03-PIRAMIDES/PT/`

#### FUTURE SERIES (In Planning)
**Location:** `LIVROS/SERIE-[NAME]/`

- **SÉRIE INVENÇÕES:** Great inventions that changed humanity (wheel, printing press, electricity, etc.)
- **SÉRIE MISTÉRIOS:** Unsolved historical mysteries (Stonehenge, Bermuda Triangle, Nazca Lines, etc.)
- **SÉRIE CIÊNCIA:** Scientific discoveries (gravity, DNA, evolution, radioactivity, etc.)

See `DIRETRIZES/` folder for complete guidelines for each series.

**Target Audience:** Children aged 8-12 years

## Repository Structure

```
BIZANTINO/
├── DIRETRIZES/                              # ⭐ CENTRAL GUIDELINES FOLDER
│   ├── README.md                            # Index of all guidelines
│   ├── PERSONAGENS-FIXOS.txt                # Fixed character specifications (ALL series)
│   ├── ESTILO-SPIELBERG.txt                 # Spielberg principles (ALL series)
│   ├── ESTRUTURA-NARRATIVA.txt              # 5-act structure (ALL series)
│   ├── SERIE-VIAJANTES-DO-TEMPO.txt         # Viajantes do Tempo series guidelines
│   ├── SERIE-LUGARES-INCRIVEIS.txt          # Lugares Incríveis series guidelines
│   ├── SERIE-INVENCOES.txt                  # Invenções series guidelines (future)
│   ├── SERIE-MISTERIOS.txt                  # Mistérios series guidelines (future)
│   └── SERIE-CIENCIA.txt                    # Ciência series guidelines (future)
│
├── LIVROS/                                  # ⭐ ALL BOOKS ORGANIZED BY SERIES
│   ├── SERIE-VIAJANTES-DO-TEMPO/
│   │   ├── README.md                        # Series overview
│   │   ├── LIVRO-01-MAQUINA-DO-TEMPO/       # Book 1
│   │   ├── LIVRO-02-PIRAMIDES-DO-TEMPO/     # Book 2
│   │   ├── LIVRO-03-ROMA/                   # Book 3
│   │   ├── LIVRO-04-CASTELO-MEDIEVAL/       # Book 4
│   │   ├── LIVRO-05-RENASCIMENTO/           # Book 5
│   │   └── LIVRO-06-FUTURO/                 # Book 6
│   │
│   ├── SERIE-LUGARES-INCRIVEIS/
│   │   ├── README.md                        # Series overview
│   │   ├── LIVRO-01-ATLANTIDA/              # Book 1 (on Google Drive - placeholder)
│   │   ├── LIVRO-02-CONSTANTINOPLA/         # Book 2 (QA in progress)
│   │   │   ├── PT/                          # Portuguese version
│   │   │   │   ├── manuscrito.txt           # Original manuscript
│   │   │   │   └── Turma_da_Aventura_Os_Ecos_de_Constantinopla.docx
│   │   │   ├── EN/                          # English translation (when ready)
│   │   │   ├── DE/                          # German translation (when ready)
│   │   │   ├── ES/                          # Spanish translation (when ready)
│   │   │   └── ERRATA-REORGANIZACAO.md      # Metadata correction documentation
│   │   └── LIVRO-03-PIRAMIDES/              # Book 3 (QA in progress)
│   │       ├── PT/                          # Portuguese version
│   │       │   ├── manuscrito_egito.txt     # Original manuscript
│   │       │   └── Turma_da_Aventura_Os_Segredos_das_Piramides.docx
│   │       ├── EN/                          # English translation (when ready)
│   │       ├── DE/                          # German translation (when ready)
│   │       ├── ES/                          # Spanish translation (when ready)
│   │       └── ERRATA-REORGANIZACAO.md      # Metadata correction documentation
│   │
│   ├── SERIE-INVENCOES/                     # Future series (structure ready)
│   │   └── README.md
│   ├── SERIE-MISTERIOS/                     # Future series (structure ready)
│   │   └── README.md
│   └── SERIE-CIENCIA/                       # Future series (structure ready)
│       └── README.md
│
├── DOCS/                                    # Documentation
│   ├── CLAUDE.md                            # This file - project overview
│   ├── DIRETRIZES_QUALIDADE_SERIE.md        # Quality standards checklist
│   ├── DIRETRIZES_VISUAIS_IDENTIDADE.md     # Visual identity guidelines
│   └── epic-book-writer.md                  # Epic book writer agent instructions
│
├── SCRIPTS/                                 # Automation scripts
│   ├── 1-MANUSCRITO/
│   │   ├── create_docx.py                   # Convert Constantinopla to DOCX
│   │   ├── create_docx_egito.py             # Convert Pirâmides to DOCX
│   │   └── generate_prompts.py              # Generate AI prompts
│   └── aplicar_otimizacoes.ps1              # PowerShell optimization
│
├── INTELIGENCIA-DE-MERCADO/                 # Market research tools
├── PERSONAGENS-CHROMAKEY/                   # Character assets for illustrations
└── .serena/project.yml                      # Serena AI configuration
```

**Key Organization Principles:**
- **DIRETRIZES/**: Centralized .txt guidelines for any IDE (Trae, Antigravity, Claude Code)
- **LIVROS/**: Books organized by series, then by book number, then by language
- **DOCS/**: Project documentation and quality standards
- **SCRIPTS/**: Automation tools for DOCX generation, translations, etc.

## Common Commands

### Generate DOCX from Manuscript

**For Book 7 (Constantinopla):**
```bash
python create_docx.py
```

**For Book 8 (Pirâmides):**
```bash
python create_docx_egito.py
```

Both scripts:
- Read UTF-8 encoded TXT manuscripts
- Generate professionally formatted DOCX with:
  - Cover page with series branding
  - Credits page
  - Table of contents
  - Chapter formatting with visual separators
  - Back cover with synopsis
- Support image insertion (looks for `images/chapter_X_topic_Y.png`)
- Output to repository root directory

### Generate AI Prompts
```bash
python generate_prompts.py
```

### Apply Optimizations (PowerShell)
```powershell
.\aplicar_otimizacoes.ps1
```

## Core Architecture

### Epic Book Writer Agent

This repository includes a specialized AI agent (`epic-book-writer.md`) for creating long-form narrative content. The agent is invoked via the Task tool with `subagent_type: epic-book-writer`.

**Agent capabilities:**
- Create epic, multi-chapter adventure stories (30,000-40,000 words)
- Maintain strict character consistency across series
- Follow five-act narrative structure (Introduction → Exploration → Main Conflict → Creative Resolution → Conclusion)
- Age-appropriate content adaptation (4-12 years, with focus on 8-12 for this series)
- Educational elements woven into entertainment
- Historical/cultural accuracy validation

### Fixed Character Profiles (NEVER MODIFY)

**CRITICAL:** These profiles must remain EXACTLY the same across all books, translations, and illustrations. Visual consistency is essential for series identity.

**Core Team:**
1. **Will (Wilian)** - 9 years, leader
   - Clothing: Dark blue t-shirt with digital print, jeans, sneakers
   - Props: ALWAYS has smartphone with holographic AI assistant Íris
   - Hair: Short, straight light brown hair
   - Expression: Intelligent, determined

2. **Mia** - 8 years, inventor
   - Clothing: Purple t-shirt with tech icons, jean shorts, purple sneakers
   - Props: Tool belt with wrench, tape measure, gadgets (always visible)
   - Hair: Red hair in two side buns
   - Expression: Expressive, enthusiastic

3. **Leo** - 10 years, athletic protector
   - Clothing: Dark green t-shirt, khaki shorts, adventure backpack
   - Hair: Short messy blonde hair, athletic build
   - Secret fear: Total darkness
   - Expression: Confident, protective, ready to act

4. **Sophie** - 8 years, detective
   - Clothing: Yellow dress with magnifying glass and clue prints
   - Props: Small notebook (always in hands)
   - Hair: Dark brown straight hair in side ponytail
   - Expression: Curious, investigative

5. **Max** - 7 years, comic relief, animal lover
   - Clothing: Red t-shirt with animal print, beige pants
   - Props: Often holding stuffed animal or small creature
   - Hair: Light brown mushroom-cut hair
   - Expression: Smiling, making funny faces

6. **Jimmy Hendrix** - Brown and white Border Collie (NOT caramel colored!)
   - Physical: Expressive intelligent eyes, dense fur, alert ears
   - Personality: Super smart, playful, brave, loyal
   - Role: Mascot and crucial team member who finds important clues

**Recurring Villain (Series-Specific Rules):**
- **Dr. Grimstone** - Eccentric scientist who wants to "end children's imagination"
  - Goal: Transform everything into numbers and logic without creativity
  - Inventions: Creates crazy devices that ALWAYS fail hilariously
  - Tone: Comedic, never scary or genuinely threatening
  - **Sidekick:** Morty - black crow who always complains about work
  - **Catchphrase:** "Imaginar é perda de tempo! O futuro é a lógica pura!"

**Dr. Grimstone Appearance Rules by Series:**
- **Viajantes do Tempo (Books 1-6):** MANDATORY in all books
- **Lugares Incríveis (Books 1-3):** NOT present - series-specific villains instead
- **Lugares Incríveis (Books 4+):** Dr. Grimstone returns as MANDATORY
- **Future Series:** See individual series guidelines in DIRETRIZES/

### Storytelling Philosophy: Spielberg Style (NEVER FORGET)

**CRITICAL:** The series embodies the narrative and visual spirit of Steven Spielberg's adventure films.

**Core Spielberg Principles:**
1. **Sense of Wonder** - Evoke childlike wonder and discovery in every story
2. **Children as Heroes** - Kids solve problems adults can't, using intelligence and heart
3. **Epic Yet Accessible** - Grand adventures told at child's eye level
4. **Mix of Tones** - Seamlessly blend humor, emotion, and action
5. **Cinematic Storytelling** - Write scenes like film sequences with visual dynamism
6. **Heart and Friendship** - Friendship and teamwork conquer all challenges

**Spielberg Film References:**
- E.T. - Childhood wonder, friendship, heart
- Indiana Jones - Adventure, humor, intelligence over brute force
- Jurassic Park - Awe and discovery
- The Goonies - Kids on epic adventure with humor
- Back to the Future - Time travel, friendship, consequences

**Visual Style for Illustrations:**
- **Art Style:** Pixar-quality semi-realistic animation
- **Influences:** Pixar films + premium children's graphic novels + European illustrated books
- **Colors:** Vibrant, rich colors with expressive detail
- **Lighting:** Cinematic lighting with soft depth of field
- **Quality:** Luxury cartoon feel, living expressive faces

### Narrative Structure (Mandatory)

Every book follows this five-act structure:

1. **Introdução** (15-20%): Hook, mystery setup, conflict introduction
2. **Exploração** (30-35%): Investigation, teamwork, tension building
3. **Conflito Principal** (20-25%): Peak tension, villain appearance
4. **Resolução Criativa** (15-20%): Solution through teamwork and unique skills
5. **Encerramento** (10-15%): Lesson learned, emotional satisfaction, series hook

### Book Length Requirements

**CRITICAL - EPIC, INTENSE, EXTENSIVE BOOKS:**

The series demands EPIC stories that are substantial and immersive:

- **Minimum Target:** 100+ pages in standard DOCX format (Google Docs compatible)
- **Word Count:** 35,000-50,000 words per book
- **Chapters:** 10-15 chapters minimum
- **Chapter Length:** 3,000-4,000 words per chapter
- **Total Pages:** Aim for 100-150 DOCX pages with standard formatting

**Intensity Requirements:**
- Epic scope with high stakes appropriate for age group
- Intense emotional moments (fear, joy, triumph, friendship)
- Fast-paced action balanced with character development
- Multiple plot threads that interweave
- Cliffhangers at chapter ends
- Spielberg-level adventure intensity

**Extensive Worldbuilding:**
- Rich historical/location details
- Vivid sensory descriptions
- Complex mysteries requiring multiple chapters to unravel
- Character arcs that develop throughout the book
- Educational content deeply integrated (not superficial)

**Quality Over Padding:**
- Length comes from rich storytelling, NOT filler
- Every scene advances plot or develops characters
- Subplots add depth and complexity
- Descriptions are vivid but purposeful
- Dialogue reveals character and advances story

### Manuscript Format

Manuscripts use specific formatting conventions:
- **Chapter headers:** `CAPÍTULO X: [Title]`
- **Section separators:** `---` for topics within chapters
- **Visual separators:** `═══════════════` for major sections
- **Scene breaks:** `***`
- **Dialogue:** Em dashes `—` for spoken lines
- **Encoding:** UTF-8 with special character support

### DOCX Generation Pipeline

The `create_docx.py` and `create_docx_egito.py` scripts follow this pipeline:

1. **Read manuscript** from TXT file (UTF-8)
2. **Parse structure** using regex patterns for chapters
3. **Generate document sections:**
   - Cover page (series title, book title, book number)
   - Credits page (metadata, age range, connections to other books)
   - Table of contents (auto-generated from chapter titles)
   - Chapters (with formatting, optional images, separators)
   - Back cover (synopsis, next book teaser)
4. **Apply formatting:**
   - Times New Roman 12pt base font
   - 1-inch margins
   - Center-aligned titles with colored text
   - 1.5 line spacing for paragraphs
   - 0.5-inch first-line indent
5. **Save DOCX** to repository root

**Image integration:** Scripts check for `images/chapter_{num}_topic_{num}.png` and insert if available.

## Quality Standards

### Writing Requirements
- Natural dialogue (children speak like children, not adults)
- Each character has distinct speech patterns and contributions
- Show-don't-tell sensory descriptions
- Age-appropriate vocabulary (2000-4000 words for 12-year-olds)
- Balance action with quieter character moments
- Educational elements subtly integrated
- No genuine danger, violence, or frightening content
- Collaborative resolutions (never one hero alone)

### Historical/Cultural Accuracy
Books 7-8 require validation:
- **Book 7 (Constantinopla):** Byzantine Empire 537 CE accuracy
- **Book 8 (Pirâmides):** Ancient Egypt historical authenticity
- Cultural sensitivity in portrayal of historical figures
- Accurate architectural and technological details
- Age-appropriate historical context

### Validation Reports
Before finalization, generate validation reports:
- `VALIDACAO_ESTRUTURA_NARRATIVA.md` - Five-act structure verification
- `VALIDACAO_CULTURAL_HISTORICA_[BOOK].md` - Historical accuracy check
- `REVISAO_IDADE_APROPRIACAO.md` - Age-appropriateness review
- `RELATORIO_CONSISTENCIA_[BOOK].md` - Character/plot consistency
- `POLIMENTO_FINAL_[BOOK].md` - Final polish notes

## Translation Workflow

Books are translated into:
- **English** (primary international market)
- **German** (European market)
- **Spanish** (Latin America + Spain)

Maintain:
- Character name consistency
- Cultural context appropriateness
- Age-level vocabulary in target language
- Humor translation (not literal but equivalent impact)

## Series Continuity

### Established Canon (Books 1-6)
- Time travel mechanics via time machine
- Historical period visits (Ancient Egypt, Rome, Medieval, Renaissance, Future)
- Recurring villain Dr. Grimstone
- Educational + entertainment balance
- Team-based problem solving

### Books 7-8 Continuation
- Maintain character ages and personalities
- Reference previous adventures when relevant
- Consistent time travel rules
- Escalating complexity appropriate for growing readers
- Setup for potential Book 9+

### Character Development Arc
Across the series, characters should show subtle growth:
- Will's leadership maturation
- Mia's invention sophistication
- Leo confronting his fear of darkness
- Sophie's deductive skills sharpening
- Max's comic timing with heart

## Critical Rules

**NEVER:**
- Change character ages, appearances, or core personalities
- Make Dr. Grimstone genuinely threatening or successful
- Write down to children or be condescending
- Include violence, genuine peril, or frightening content
- Make Jimmy Hendrix a background character
- Describe Jimmy as caramel-colored (brown and white only)
- Let one character solve everything alone
- End with heavy-handed moral lessons

**ALWAYS:**
- Respect age group cognitive abilities
- Give each character meaningful participation
- Make Dr. Grimstone's failures comedic (when he appears)
- Include teamwork in resolutions
- Maintain character consistency across series
- Balance education with entertainment
- Ensure historical/cultural accuracy
- Generate validation reports before finalization

## Using DIRETRIZES (Guidelines System)

### Overview

The `DIRETRIZES/` folder contains centralized .txt guidelines designed to work across any IDE (Trae, Antigravity, Claude Code, etc.). This system was created to ensure consistency when writing new books.

### Structure

**Universal Guidelines (Apply to ALL series):**
- `PERSONAGENS-FIXOS.txt` - Fixed character specifications (NEVER modify)
- `ESTILO-SPIELBERG.txt` - Spielberg storytelling principles
- `ESTRUTURA-NARRATIVA.txt` - Mandatory 5-act structure

**Series-Specific Guidelines:**
- `SERIE-VIAJANTES-DO-TEMPO.txt` - Time Travelers series (Books 1-6)
- `SERIE-LUGARES-INCRIVEIS.txt` - Incredible Places series (Books 1-3+)
- `SERIE-INVENCOES.txt` - Inventions series (future)
- `SERIE-MISTERIOS.txt` - Mysteries series (future)
- `SERIE-CIENCIA.txt` - Science series (future)

### How to Use

When creating a new book, provide the AI with the appropriate guideline paths:

```
"Follow these guidelines:
D:\TRAE-PROJETOS\livro1\BIZANTINO\DIRETRIZES\PERSONAGENS-FIXOS.txt
D:\TRAE-PROJETOS\livro1\BIZANTINO\DIRETRIZES\ESTILO-SPIELBERG.txt
D:\TRAE-PROJETOS\livro1\BIZANTINO\DIRETRIZES\ESTRUTURA-NARRATIVA.txt
D:\TRAE-PROJETOS\livro1\BIZANTINO\DIRETRIZES\SERIE-LUGARES-INCRIVEIS.txt"
```

The .txt format ensures compatibility across different AI tools and IDEs.

### Series Selection Guide

- **Viajantes do Tempo:** Focus on historical PERIODS (e.g., "Medieval Times", "Ancient Rome")
- **Lugares Incríveis:** Focus on iconic LOCATIONS (e.g., "Machu Picchu", "Great Wall of China")
- **Invenções:** Focus on world-changing inventions (e.g., "The Wheel", "Printing Press")
- **Mistérios:** Focus on unsolved mysteries (e.g., "Stonehenge", "Bermuda Triangle")
- **Ciência:** Focus on scientific discoveries (e.g., "Theory of Gravity", "DNA Discovery")

## Epic Book Writer Usage

### Creating New Books with Market Research

**STEP 1: Market Research Phase**

First, research trending themes across all 5 target markets:

```python
# Use Task tool with epic-book-writer agent for market research
Task(
    subagent_type="epic-book-writer",
    description="Research market trends for Book 9+",
    prompt="""Conduct deep research on Amazon bestsellers for children's adventure books (8-12 years) in our 5 target markets:

    1. United States (amazon.com)
    2. Brazil (amazon.com.br)
    3. Germany (amazon.de)
    4. United Kingdom (amazon.co.uk)
    5. Spain (amazon.es)

    Research focus:
    - Top-selling themes in children's adventure/time travel fiction
    - Trending historical periods
    - Popular educational topics (STEM, history, ecology, space, etc.)
    - Fantasy/sci-fi elements that resonate across markets
    - Current cultural events or anniversaries (2026+)
    - Competitor series analysis (Magic Tree House, Who Was?, etc.)
    - Market gaps Turma da Aventura can fill

    Deliverable:
    - 3-5 book concept proposals aligned with market trends
    - Justification with data from all 5 markets
    - Cultural compatibility analysis
    - Recommended theme with rationale
    """
)
```

**STEP 2: Manuscript Creation Phase**

After selecting theme based on research:

```python
# Use Task tool with epic-book-writer agent for manuscript creation
Task(
    subagent_type="epic-book-writer",
    description="Create Book 9 manuscript",
    prompt="""Create the next book in the Turma da Aventura: Viajantes do Tempo series.

    **Market Research Context:**
    [Include selected theme and market justification from research phase]

    **Book Specifications:**
    - Age: 12 years (8-12 range)
    - Setting: [Historical period/location based on market research]
    - Theme: [Core theme/conflict aligned with trending topics]
    - Length: 35,000-50,000 words (100+ DOCX pages minimum)
    - Chapters: 10-15 chapters (3,000-4,000 words each)

    **Series Requirements:**
    - Five-act structure (15-20%, 30-35%, 20-25%, 15-20%, 10-15%)
    - All 6 core characters + Jimmy Hendrix participate meaningfully
    - Dr. Grimstone appears as comedic antagonist (MANDATORY)
    - Spielberg-style storytelling (wonder, adventure, heart)
    - Historical/scientific accuracy for [period/topic]
    - Connection to previous books in series
    - Setup hook for next adventure

    **Translation Considerations:**
    - Write for simultaneous publication in Portuguese, English, German, Spanish
    - Use clear, culturally accessible language
    - Avoid region-specific slang or cultural references
    - Universal humor that works cross-culturally
    - Educational content that applies universally

    **Quality Standards:**
    - Epic, intense, extensive narrative
    - Rich worldbuilding and sensory descriptions
    - Character growth and emotional depth
    - Multiple interconnected plot threads
    - Cliffhangers at chapter ends
    - Quality storytelling, no filler content
    """
)
```

## Development Workflow

### Phase 0: Market Research (MANDATORY)

**Before creating any new book**, conduct deep research on Amazon bestsellers in 5 target markets:

1. **United States** (amazon.com) - Primary international market
2. **Brazil** (amazon.com.br) - Portuguese native market
3. **Germany** (amazon.de) - European powerhouse
4. **United Kingdom** (amazon.co.uk) - English-speaking European market
5. **Spain** (amazon.es) - Spanish-speaking market

**Research Focus:**
- Top-selling children's book themes (8-12 age group)
- Trending historical periods and scientific topics
- Fantasy/sci-fi elements that resonate across markets
- Cultural events or anniversaries to leverage
- Competitor analysis and market gaps
- Universal themes vs. market-specific preferences

**Research Output:**
- 3-5 book concepts aligned with market trends
- Justification with data from all 5 target markets
- Cultural compatibility analysis
- Theme selection recommendation

### Phase 1: Concept Development
- Define historical period, educational themes, character arcs
- Ensure alignment with market research findings
- Verify cultural appropriateness for all 5 target markets

### Phase 2: Manuscript Creation
- Use epic-book-writer agent or manual writing
- Write with translation in mind (clear, culturally accessible language)
- Aim for 35,000-50,000 words (100+ DOCX pages)
- Follow five-act structure with Spielberg storytelling principles

### Phase 3: Validation Phase
Generate all validation reports:
1. `VALIDACAO_ESTRUTURA_NARRATIVA.md` - Five-act structure verification
2. `VALIDACAO_CULTURAL_HISTORICA_[BOOK].md` - Historical accuracy
3. `REVISAO_IDADE_APROPRIACAO.md` - Age-appropriateness review
4. `RELATORIO_CONSISTENCIA_[BOOK].md` - Character/plot consistency
5. `POLIMENTO_FINAL_[BOOK].md` - Final polish notes
6. `MANUSCRITO_FINAL_INFO.md` - Summary documentation

### Phase 4: Revision
- Address all validation findings
- Ensure cultural sensitivity for all markets
- Verify historical/scientific accuracy

### Phase 5: Final Manuscript
- Create `*_MANUSCRITO_FINAL.txt` in UTF-8
- Verify 100+ page target when converted to DOCX
- Confirm all quality checkpoints passed

### Phase 6: DOCX Generation
- Run `create_docx_*.py` (for Books 7-8) or create new script
- Verify formatting, chapter structure, visual elements
- Confirm Google Docs compatibility

### Phase 7: Translation & QA

**Automated Translation:**
- Use existing translation tools (in other directories)
- Translate to English, German, Spanish simultaneously
- Preserve character names, formatting, structural elements

**GPT-5 QA Process:**
- Automated QA review using GPT-5 API
- Translation accuracy verification
- Cultural appropriateness checks
- Consistency verification across languages
- Glossary compliance check

**Final Review:**
- Human review of all translations
- Market-specific cultural sensitivity check
- Final approval before publication

### Phase 8: Simultaneous Multilingual Publication

**Publishing Strategy:**
ALL books are published in ALL 4 languages SIMULTANEOUSLY to maximize market reach and sales momentum.

**Amazon KDP Upload:**
1. **Portuguese** → amazon.com.br (Brazil)
2. **English** → amazon.com (USA) + amazon.co.uk (UK)
3. **German** → amazon.de (Germany)
4. **Spanish** → amazon.es (Spain) + Latin America markets

**Publication Checklist:**
- [ ] All 4 language versions QA-approved
- [ ] Covers designed for each market
- [ ] Metadata optimized for each Amazon region
- [ ] Keywords researched for each language/market
- [ ] Pricing strategy defined for each region
- [ ] Series continuity verified across all versions

## Success Metrics

Current series performance:
- **Sales trajectory:** Tripling monthly
- **Markets:** USA, Europe (Germany, Spain, others)
- **Ratings:** 4.5-5.0 stars average
- **Languages:** 4 (Portuguese, English, German, Spanish)

Maintain quality standards that have driven this success across Books 7-8.
