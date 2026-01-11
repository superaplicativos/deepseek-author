# 📚 DIRETRIZES DA TURMA DA AVENTURA

**Versão:** 2.0
**Data:** 2026-01-10
**Status:** DOCUMENTO MESTRE DE TODAS AS SÉRIES

---

## 🎯 PROPÓSITO DESTA PASTA

Esta pasta centraliza **TODAS as diretrizes** das diferentes séries da Turma da Aventura em arquivos `.txt` simples que podem ser:
- ✅ Copiados e colados em qualquer IDE (Trae, Antigravity, Claude Code, etc.)
- ✅ Usados como referência rápida durante a escrita
- ✅ Compartilhados com colaboradores
- ✅ Integrados em prompts de IA

**Por que arquivos .txt?**
- Formato universal compatível com todas as ferramentas
- Fácil de copiar/colar path completo
- Não requer software especial para abrir
- Ideal para prompts e integrações

---

## 📁 ÍNDICE DE DIRETRIZES DISPONÍVEIS

### DIRETRIZES UNIVERSAIS (Aplicam-se a TODAS as séries)

| Arquivo | Caminho | Descrição |
|---------|---------|-----------|
| **PERSONAGENS-FIXOS.txt** | `D:\TRAE-PROJETOS\livro1\BIZANTINO\DIRETRIZES\PERSONAGENS-FIXOS.txt` | Especificações visuais e de personalidade dos 6 personagens + Jimmy Hendrix + Dr. Grimstone |
| **ESTILO-SPIELBERG.txt** | `D:\TRAE-PROJETOS\livro1\BIZANTINO\DIRETRIZES\ESTILO-SPIELBERG.txt` | Princípios de narrativa cinematográfica tipo Spielberg |
| **ESTRUTURA-NARRATIVA.txt** | `D:\TRAE-PROJETOS\livro1\BIZANTINO\DIRETRIZES\ESTRUTURA-NARRATIVA.txt` | Estrutura obrigatória de 5 atos com percentuais |

### DIRETRIZES ESPECÍFICAS POR SÉRIE

| Série | Arquivo | Caminho | Status |
|-------|---------|---------|--------|
| **VIAJANTES DO TEMPO** | `SERIE-VIAJANTES-DO-TEMPO.txt` | `D:\TRAE-PROJETOS\livro1\BIZANTINO\DIRETRIZES\SERIE-VIAJANTES-DO-TEMPO.txt` | ✅ 6 livros publicados |
| **LUGARES INCRÍVEIS** | `SERIE-LUGARES-INCRIVEIS.txt` | `D:\TRAE-PROJETOS\livro1\BIZANTINO\DIRETRIZES\SERIE-LUGARES-INCRIVEIS.txt` | ⚠️ 3 livros (1 Google Drive, 2 em QA) |
| **INVENÇÕES** | `SERIE-INVENCOES.txt` | `D:\TRAE-PROJETOS\livro1\BIZANTINO\DIRETRIZES\SERIE-INVENCOES.txt` | 📝 Planejamento |
| **MISTÉRIOS** | `SERIE-MISTERIOS.txt` | `D:\TRAE-PROJETOS\livro1\BIZANTINO\DIRETRIZES\SERIE-MISTERIOS.txt` | 📝 Planejamento |
| **CIÊNCIA** | `SERIE-CIENCIA.txt` | `D:\TRAE-PROJETOS\livro1\BIZANTINO\DIRETRIZES\SERIE-CIENCIA.txt` | 📝 Planejamento |

---

## 🚀 COMO USAR EM DIFERENTES IDEs

### 📌 Trae IDE

```
1. Abrir Trae
2. Ir em Settings → Custom Prompts
3. Adicionar novo prompt:
   Nome: "Turma da Aventura - [Nome da Série]"
   Conteúdo: Copiar e colar conteúdo do arquivo .txt desejado
4. Ativar o prompt antes de começar a escrever
```

### 📌 Antigravity IDE

```
1. Abrir Antigravity
2. Menu → Preferences → AI Guidelines
3. Click "Import from file"
4. Selecionar: D:\TRAE-PROJETOS\livro1\BIZANTINO\DIRETRIZES\[arquivo].txt
5. Salvar configuração
```

### 📌 Claude Code

```
1. Ao iniciar conversa, usar comando:
   "Por favor, siga as diretrizes em: D:\TRAE-PROJETOS\livro1\BIZANTINO\DIRETRIZES\[arquivo].txt"

2. Ou copiar conteúdo do arquivo diretamente na conversa:
   "Aqui estão as diretrizes para esta série:
   [colar conteúdo do .txt]"
```

### 📌 GPT-4 / GPT-5 / Claude via API

```python
# Python example
with open("D:/TRAE-PROJETOS/livro1/BIZANTINO/DIRETRIZES/SERIE-VIAJANTES-DO-TEMPO.txt", "r", encoding="utf-8") as f:
    guidelines = f.read()

prompt = f"""
{guidelines}

Agora escreva o próximo capítulo seguindo essas diretrizes...
"""
```

### 📌 Gemini (Google AI Studio)

```
1. Abrir Google AI Studio
2. Criar novo Chat
3. System Instructions:
   Copiar e colar conteúdo do arquivo .txt desejado
4. Começar conversa para escrita do livro
```

---

## 📖 ESTRUTURA DAS SÉRIES

### 🕰️ SÉRIE: VIAJANTES DO TEMPO
**Tema:** Viagens através de diferentes períodos históricos
**Livros:** 1-6 (Publicados)
**Diretriz:** `SERIE-VIAJANTES-DO-TEMPO.txt`
**Pasta:** `LIVROS/SERIE-VIAJANTES-DO-TEMPO/`

**Livros da Série:**
1. A Máquina do Tempo
2. Pirâmides do Tempo
3. Roma
4. Castelo Medieval
5. Renascimento
6. Futuro

---

### 🌍 SÉRIE: LUGARES INCRÍVEIS
**Tema:** Exploração de localizações históricas/míticas extraordinárias
**Livros:** 3 planejados (1 no Google Drive, 2 em QA)
**Diretriz:** `SERIE-LUGARES-INCRIVEIS.txt`
**Pasta:** `LIVROS/SERIE-LUGARES-INCRIVEIS/`

**Livros da Série:**
1. Atlântida (Google Drive - pendente importação)
2. Constantinopla (em QA)
3. Pirâmides (em QA)

**⚠️ NOTA IMPORTANTE:** Livros 2 e 3 foram escritos ANTES da reorganização e estão marcados incorretamente nos manuscritos como "Livros 7 e 8 da série Viajantes do Tempo". Essa informação será corrigida nos metadados.

---

### 🔧 SÉRIE: INVENÇÕES
**Tema:** Grandes invenções que mudaram a humanidade
**Status:** Planejamento (baseado em análise de mercado SEO)
**Diretriz:** `SERIE-INVENCOES.txt`
**Pasta:** `LIVROS/SERIE-INVENCOES/`

**Foco:** STEM educacional forte, palavras-chave otimizadas para Amazon

---

### 🔍 SÉRIE: MISTÉRIOS
**Tema:** Mistérios históricos e enigmas a serem resolvidos
**Status:** Planejamento (baseado em análise de mercado SEO)
**Diretriz:** `SERIE-MISTERIOS.txt`
**Pasta:** `LIVROS/SERIE-MISTERIOS/`

**Foco:** Investigação, Sophie (detetive) em destaque

---

### 🔬 SÉRIE: CIÊNCIA
**Tema:** Descobertas científicas que revolucionaram o mundo
**Status:** Planejamento (baseado em análise de mercado SEO)
**Diretriz:** `SERIE-CIENCIA.txt`
**Pasta:** `LIVROS/SERIE-CIENCIA/`

**Foco:** Educacional científico, Mia (inventora) em destaque

---

## 🎨 WORKFLOW DE ESCRITA RECOMENDADO

### ANTES DE COMEÇAR A ESCREVER UM NOVO LIVRO:

1. **Escolher a Série**
   - Decidir qual série (Viajantes do Tempo, Lugares Incríveis, Invenções, etc.)

2. **Ler TODAS as diretrizes aplicáveis:**
   ```
   ✅ PERSONAGENS-FIXOS.txt (SEMPRE)
   ✅ ESTILO-SPIELBERG.txt (SEMPRE)
   ✅ ESTRUTURA-NARRATIVA.txt (SEMPRE)
   ✅ SERIE-[nome-da-serie].txt (específica da série escolhida)
   ```

3. **Análise de Mercado (para livros novos):**
   - Verificar trends Amazon nos 5 mercados
   - Analisar palavras-chave (SEO)
   - Usar deep research do Gemini
   - Documentar insights em `INTELIGENCIA-DE-MERCADO/`

4. **Criar Outline:**
   - Seguir estrutura de 5 atos (ESTRUTURA-NARRATIVA.txt)
   - Garantir participação de TODOS os personagens
   - Planejar aparições do Dr. Grimstone (se aplicável)

5. **Escrever:**
   - Manter diretrizes abertas em janela lateral
   - Consultar PERSONAGENS-FIXOS.txt regularmente
   - Verificar consistência a cada capítulo

6. **Validação:**
   - Gerar 6 relatórios obrigatórios (ver DOCS/DIRETRIZES_QUALIDADE_SERIE.md)
   - Corrigir problemas encontrados
   - QA final antes de publicação

---

## ⚙️ INTEGRAÇÃO COM SCRIPTS EXISTENTES

### Scripts Python que usam as diretrizes:

| Script | Localização | Função |
|--------|-------------|--------|
| `create_docx.py` | Raiz do projeto | Gera DOCX do manuscrito (Livro 7) |
| `create_docx_egito.py` | Raiz do projeto | Gera DOCX do manuscrito (Livro 8) |
| `generate_prompts.py` | Raiz do projeto | Gera prompts AI para criação de conteúdo |

**NOTA:** Após reorganização, esses scripts serão atualizados para refletir nova estrutura de pastas.

---

## 📊 ANÁLISE DE MERCADO E SEO

### Ferramentas e Processos:

1. **Amazon Keyword Research:**
   - Mercados: USA, Brasil, Alemanha, UK, Espanha
   - Categorias: Children's Books, Adventure, Time Travel, Historical Fiction
   - Scripts em: `INTELIGENCIA-DE-MERCADO/`

2. **Gemini Deep Research:**
   - Templates de prompts disponíveis em cada SERIE-*.txt
   - Documentar resultados para referência futura

3. **Competitor Analysis:**
   - Magic Tree House, Who Was?, I Survived, etc.
   - Identificar gaps e oportunidades

### Onde documentar insights:
```
INTELIGENCIA-DE-MERCADO/
├── analise_serie_viajantes.md
├── analise_serie_lugares_incriveis.md
├── analise_serie_invencoes.md
├── analise_serie_misterios.md
└── analise_serie_ciencia.md
```

---

## 🔄 VERSIONAMENTO E ATUALIZAÇÕES

### Quando atualizar as diretrizes:

- ✅ **Após publicação de cada livro:** Incorporar lições aprendidas
- ✅ **Trimestralmente:** Revisar com base em performance de vendas
- ✅ **Quando houver mudanças de personagens:** Atualizar PERSONAGENS-FIXOS.txt
- ✅ **Após análise de mercado:** Atualizar SERIE-*.txt com novos insights

### Histórico de Versões:

- **v2.0 (2026-01-10):** Reorganização completa por séries, criação da pasta DIRETRIZES/
- **v1.0 (2026-01-01):** Diretrizes originais em DOCS/DIRETRIZES_QUALIDADE_SERIE.md

---

## 📞 SUPORTE E DÚVIDAS

### Documentação Adicional:

- **Qualidade Geral:** `DOCS/DIRETRIZES_QUALIDADE_SERIE.md`
- **Identidade Visual:** `DOCS/DIRETRIZES_VISUAIS_IDENTIDADE.md`
- **Epic Book Writer Agent:** `DOCS/epic-book-writer.md`
- **Claude Code Guide:** `DOCS/CLAUDE.md`

### Hierarquia de Documentos:

1. **DIRETRIZES/** (esta pasta) → Referência rápida, uso diário
2. **DOCS/** → Documentação detalhada, processos completos
3. **Planos aprovados** → `.claude/plans/` (Claude Code)

---

## ✅ CHECKLIST DE CONFORMIDADE

Antes de finalizar qualquer manuscrito, confirmar:

- [ ] Leu PERSONAGENS-FIXOS.txt e todos os personagens estão corretos
- [ ] Leu ESTILO-SPIELBERG.txt e narrativa segue princípios
- [ ] Leu ESTRUTURA-NARRATIVA.txt e 5 atos estão balanceados
- [ ] Leu SERIE-[específica].txt e tema está alinhado
- [ ] Dr. Grimstone aparece (se obrigatório para a série/livro)
- [ ] Análise de mercado/SEO foi feita (para livros novos)
- [ ] 6 relatórios de validação gerados e aprovados

---

**Última Atualização:** 2026-01-10
**Próxima Revisão:** Após publicação do próximo livro de cada série
