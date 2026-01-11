# 🤖 SCRIPTS - Automação de Produção

Scripts Python organizados por função para automação completa do workflow de produção dos livros.

## Estrutura

```
SCRIPTS/
├── 1-MANUSCRITO/           # Criação e formatação de manuscritos
├── 2-TRADUCAO/             # Tradução automática (CRÍTICO)
├── 3-FORMATACAO-KDP/       # Formatação para Amazon KDP
├── 4-ANALISE/              # Análise e inspeção de arquivos
├── 5-MARKETING-RESEARCH/   # Pesquisa de mercado e SEO
└── 6-GERACAO-IMAGENS/      # Geração de prompts para IA
```

## 📁 1-MANUSCRITO/

### create_docx.py
Converte manuscrito TXT do Livro 7 (Constantinopla) para DOCX formatado.
```bash
python SCRIPTS/1-MANUSCRITO/create_docx.py
```

### create_docx_egito.py
Converte manuscrito TXT do Livro 8 (Pirâmides) para DOCX formatado.
```bash
python SCRIPTS/1-MANUSCRITO/create_docx_egito.py
```

### generate_prompts.py
Gera prompts de IA para ilustrações baseados no manuscrito.
```bash
python SCRIPTS/1-MANUSCRITO/generate_prompts.py
```

---

## 📁 2-TRADUCAO/ (CRÍTICO!)

### tradutor_docx_GRATUITO.py ⭐ PRINCIPAL
Tradutor DOCX 100% gratuito usando Google Translate. Preserva TODA formatação e imagens.
```bash
python SCRIPTS/2-TRADUCAO/tradutor_docx_GRATUITO.py meu_livro.docx es
```
Idiomas suportados: `en`, `es`, `de`, `fr`, `it`, `nl`, `ru`, `zh-cn`, `ja`, `ko`

### qa_traducao_docx.py
QA automático pós-tradução: Remove espaços antes de pontuação, conta palavras, detecta resquícios de português.
```bash
python SCRIPTS/2-TRADUCAO/qa_traducao_docx.py livro-ES-GRATUITO.docx
```

### qa_fix_punctuation_docx.py
Correção de pontuação em DOCX traduzidos.
```bash
python SCRIPTS/2-TRADUCAO/qa_fix_punctuation_docx.py arquivo.docx
```

### qa_pontuacao_leve.py
Correção leve de pontuação.
```bash
python SCRIPTS/2-TRADUCAO/qa_pontuacao_leve.py arquivo.docx
```

### verificar_traducao.py
Verificação completa de traduções.
```bash
python SCRIPTS/2-TRADUCAO/verificar_traducao.py arquivo-traduzido.docx
```

**📘 Veja também:** `DOCS/DIRETRIZ_TRADUCAO_DOCX.md` para workflow completo de tradução.

---

## 📁 3-FORMATACAO-KDP/

### conversor_amazon_kdp.py
Converte DOCX para formato Amazon KDP.
```bash
python SCRIPTS/3-FORMATACAO-KDP/conversor_amazon_kdp.py arquivo.docx
```

### conversor_epub_kdp_DEFINITIVO.py
Conversor EPUB definitivo para KDP.
```bash
python SCRIPTS/3-FORMATACAO-KDP/conversor_epub_kdp_DEFINITIVO.py arquivo.docx
```

### conversor_epub_kdp_espanhol.py
Conversor EPUB específico para espanhol.
```bash
python SCRIPTS/3-FORMATACAO-KDP/conversor_epub_kdp_espanhol.py arquivo-ES.docx
```

### ajuste_kdp_6x9.py
Ajusta formatação para tamanho 6x9 polegadas (padrão Amazon).
```bash
python SCRIPTS/3-FORMATACAO-KDP/ajuste_kdp_6x9.py arquivo.docx
```

### otimizador_espacamento_kindle.py
Otimiza espaçamento para leitura em Kindle.
```bash
python SCRIPTS/3-FORMATACAO-KDP/otimizador_espacamento_kindle.py arquivo.docx
```

---

## 📁 4-ANALISE/

### analisar_docx.py
Análise geral de arquivos DOCX (estrutura, estilos, imagens).
```bash
python SCRIPTS/4-ANALISE/analisar_docx.py arquivo.docx
```

### analisar_livro3.py
Análise específica do Livro 3.
```bash
python SCRIPTS/4-ANALISE/analisar_livro3.py
```

### verificar_traducoes_livro3.py
Verificação de traduções do Livro 3.
```bash
python SCRIPTS/4-ANALISE/verificar_traducoes_livro3.py
```

### inspecionar_imagens.py
Inspeção de imagens em arquivos DOCX.
```bash
python SCRIPTS/4-ANALISE/inspecionar_imagens.py arquivo.docx
```

### corrigir_imagens_docx.py
Correção de problemas com imagens em DOCX.
```bash
python SCRIPTS/4-ANALISE/corrigir_imagens_docx.py arquivo.docx
```

---

## 📁 5-MARKETING-RESEARCH/

### amazon_keyword_mapper.py
Mapeamento de keywords da Amazon por categoria.
```bash
python SCRIPTS/5-MARKETING-RESEARCH/amazon_keyword_mapper.py
```

### amazon_top_terms_prefix.py
Análise de termos top da Amazon com prefixos.
```bash
python SCRIPTS/5-MARKETING-RESEARCH/amazon_top_terms_prefix.py
```

### global_top_1000_keywords.py
Pesquisa de top 1000 keywords globais para livros infantis.
```bash
python SCRIPTS/5-MARKETING-RESEARCH/global_top_1000_keywords.py
```

### kdp_growth_intelligence.py
Inteligência de crescimento KDP (tendências, competidores).
```bash
python SCRIPTS/5-MARKETING-RESEARCH/kdp_growth_intelligence.py
```

### generate_kdp_html_report.py
Gera relatórios HTML de análise KDP.
```bash
python SCRIPTS/5-MARKETING-RESEARCH/generate_kdp_html_report.py
```

### generate_keywords_html_report.py
Gera relatórios HTML de análise de keywords.
```bash
python SCRIPTS/5-MARKETING-RESEARCH/generate_keywords_html_report.py
```

---

## 📁 6-GERACAO-IMAGENS/

### gerar_imagens_livro6.py
Gera prompts de IA para imagens do Livro 6.
```bash
python SCRIPTS/6-GERACAO-IMAGENS/gerar_imagens_livro6.py
```

---

## Workflow Completo (Novo Livro)

### 1. Criar Manuscrito
```bash
# Escrever manuscrito em TXT
# Converter para DOCX
python SCRIPTS/1-MANUSCRITO/create_docx.py
```

### 2. Traduzir (4 idiomas)
```bash
# Português → Inglês
python SCRIPTS/2-TRADUCAO/tradutor_docx_GRATUITO.py livro.docx en

# Português → Espanhol
python SCRIPTS/2-TRADUCAO/tradutor_docx_GRATUITO.py livro.docx es

# Português → Alemão
python SCRIPTS/2-TRADUCAO/tradutor_docx_GRATUITO.py livro.docx de
```

### 3. QA Automático
```bash
# Para cada tradução
python SCRIPTS/2-TRADUCAO/qa_traducao_docx.py livro-EN-GRATUITO.docx
python SCRIPTS/2-TRADUCAO/qa_traducao_docx.py livro-ES-GRATUITO.docx
python SCRIPTS/2-TRADUCAO/qa_traducao_docx.py livro-DE-GRATUITO.docx
```

### 4. Formatação KDP
```bash
# Ajustar para 6x9
python SCRIPTS/3-FORMATACAO-KDP/ajuste_kdp_6x9.py livro-EN.docx

# Converter para EPUB
python SCRIPTS/3-FORMATACAO-KDP/conversor_epub_kdp_DEFINITIVO.py livro-EN.docx
```

### 5. Publicação Simultânea
- Upload em amazon.com.br (PT)
- Upload em amazon.com (EN)
- Upload em amazon.de (DE)
- Upload em amazon.es (ES)

---

## Dependências

Instale as dependências necessárias:
```bash
pip install python-docx deep-translator requests ebooklib lxml beautifulsoup4
```

---

## Notas Importantes

- ⚠️ **SEMPRE** teste scripts em cópias de arquivos antes de aplicar em originais
- ⚠️ **SEMPRE** faça backup antes de conversões e traduções
- ⚠️ LibreOffice é necessário para exportação final de EPUB (veja `DOCS/DIRETRIZ_TRADUCAO_DOCX.md`)
- ⚠️ Google Translate gratuito pode ter limite de requisições - adicione delays se necessário
