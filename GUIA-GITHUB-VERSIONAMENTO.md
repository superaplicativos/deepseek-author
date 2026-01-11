# 🚀 Guia Completo: GitHub Privado para Projeto Bizantino

**Objetivo**: Configurar controle de versionamento empresarial para toda a infraestrutura (livros, sistemas, automação) de forma organizada, segura e escalável.

---

## 📋 Índice

1. [Visão Geral da Estratégia](#visão-geral)
2. [Estrutura de Repositórios Recomendada](#estrutura-repositórios)
3. [Passo a Passo: Configuração Inicial](#configuração-inicial)
4. [Organização de Arquivos Sensíveis](#arquivos-sensíveis)
5. [Workflow de Versionamento](#workflow)
6. [Proteção e Segurança](#segurança)
7. [Colaboração e Escalabilidade](#colaboração)
8. [Backup e Redundância](#backup)
9. [GitIgnore Estratégico](#gitignore)
10. [Comandos Essenciais](#comandos)

---

## 🎯 Visão Geral da Estratégia {#visão-geral}

### **Contexto do Projeto**
- **331 vendas**, 24.823 páginas KENP, validação de mercado comprovada
- **28 títulos publicados** (6 livros × 4 idiomas + 2 em QA)
- **Automação de 95%** do processo editorial
- **Pipeline de $10-25/livro** vs $5.000 da concorrência
- **Busca de investimento** comparável a Spines ($16M)

### **Necessidades Empresariais**
✅ Versionamento de código (25+ scripts Python críticos)  
✅ Controle de manuscritos e traduções  
✅ Documentação técnica centralizada  
✅ Histórico de mudanças auditável  
✅ Colaboração segura (equipe futura)  
✅ Backup automatizado  
✅ Preparação para due diligence de investidores  

### **Estratégia Recomendada: Multi-Repositório**

```
GitHub Organization: trae-projetos (ou nome da empresa)
│
├── bizantino-core (PRIVADO) ⭐ PRINCIPAL
│   ├── Sistemas de automação
│   ├── Documentação técnica
│   ├── Scripts críticos
│   └── Configurações
│
├── bizantino-livros (PRIVADO)
│   ├── Manuscritos originais
│   ├── Traduções
│   └── Validações
│
├── bizantino-assets (PRIVADO)
│   ├── Personagens chromakey (NUNCA MODIFICAR)
│   ├── Capas por idioma
│   └── Imagens internas
│
├── bizantino-investidores (PRIVADO)
│   ├── Pitch decks
│   ├── One-pagers
│   └── Dados KDP
│
└── bizantino-inteligencia (PRIVADO)
    ├── Pesquisa de mercado
    ├── Keywords research
    └── Analytics KDP
```

**Vantagens desta abordagem:**
- ✅ Separação clara de responsabilidades
- ✅ Controle granular de acesso
- ✅ Clonagem rápida apenas do necessário
- ✅ Histórico Git mais limpo
- ✅ Melhoria na performance (repos menores)

---

## 🗂️ Estrutura de Repositórios Detalhada {#estrutura-repositórios}

### **1. bizantino-core** (Repositório Principal)

```
bizantino-core/
├── README.md                              # Overview completo do projeto
├── MAPEAMENTO_COMPLETO_PROJETO.md
├── MIGRACAO_COMPLETA.md
│
├── .github/
│   ├── workflows/                         # CI/CD (futuro)
│   └── ISSUE_TEMPLATE/                    # Templates para issues
│
├── docs/
│   ├── CLAUDE.md                          # Guia master para IA
│   ├── DIRETRIZES_QUALIDADE_SERIE.md
│   ├── DIRETRIZES_VISUAIS_IDENTIDADE.md
│   ├── epic-book-writer.md
│   └── workflows/                         # Workflows de produção
│
├── scripts/
│   ├── 1-MANUSCRITO/
│   ├── 2-TRADUCAO/                        # CRÍTICO
│   ├── 3-FORMATACAO-KDP/
│   ├── 4-ANALISE/
│   ├── 5-MARKETING-RESEARCH/
│   ├── 6-GERACAO-IMAGENS/
│   └── requirements.txt                   # Dependências Python
│
├── config/
│   ├── .gitignore
│   ├── .editorconfig
│   └── project-settings.yml
│
├── CHANGELOG.md                           # Histórico de versões
├── LICENSE                                # Licença (proprietária)
└── CONTRIBUTING.md                        # Guia para colaboradores
```

**Comandos de setup:**
```bash
cd d:\TRAE-PROJETOS\livro1\BIZANTINO
git init
git add docs/ scripts/ *.md .gitignore
git commit -m "feat: Initial commit - Core automation system v1.0"
git branch -M main
git remote add origin https://github.com/trae-projetos/bizantino-core.git
git push -u origin main
```

---

### **2. bizantino-livros** (Conteúdo Editorial)

```
bizantino-livros/
├── README.md
├── SERIE-VIAJANTES-DO-TEMPO/
│   ├── LIVRO-01-MAQUINA-DO-TEMPO/
│   │   ├── PT/
│   │   │   ├── manuscrito.txt
│   │   │   └── Turma_da_Aventura_Maquina_do_Tempo.docx
│   │   ├── EN/
│   │   ├── ES/
│   │   └── DE/
│   ├── LIVRO-02-PIRAMIDES/
│   ├── ...
│   ├── LIVRO-07-CONSTANTINOPLA/
│   └── LIVRO-08-PIRAMIDES/
│       └── VALIDACOES/                    # 8 relatórios MD
│
├── SERIE-CIENCIA/
├── SERIE-INVENCOES/
├── SERIE-LUGARES-INCRIVEIS/
└── SERIE-MISTERIOS/
```

**Estratégia de commits:**
```bash
# Commit estruturado por livro
git commit -m "feat(livro-07): Adiciona manuscrito Constantinopla (35k palavras)"
git commit -m "feat(livro-07): Adiciona traduções EN, ES, DE"
git commit -m "docs(livro-08): QA completo - 8 relatórios de validação"
```

---

### **3. bizantino-assets** (Recursos Visuais)

```
bizantino-assets/
├── README.md
├── PERSONAGENS-CHROMAKEY/                 # ⚠️ NUNCA MODIFICAR
│   ├── WILL.jpg
│   ├── MIA.jpg
│   ├── LEO.jpg
│   ├── SOPHIE.jpg
│   ├── MAX.jpg
│   ├── JIMMY.jpg
│   ├── GRIMSTONE.jpg
│   └── TURMATODA.fw.png
│
├── CAPAS/
│   ├── LIVRO-01/
│   │   ├── PT-capa.png
│   │   ├── EN-cover.png
│   │   ├── ES-portada.png
│   │   └── DE-umschlag.png
│   └── ...
│
├── IMAGENS-INTERNAS/
│   └── LIVRO-06-FUTURO/
│       └── capitulo-XX/
│
└── PROMPTS-GEMINI/
    ├── personagens-specs.md
    └── templates-capa.md
```

**Uso de Git LFS (Large File Storage):**
```bash
# Instalar Git LFS
git lfs install

# Rastrear arquivos grandes
git lfs track "*.jpg"
git lfs track "*.png"
git lfs track "*.psd"
git lfs track "*.docx"

# Commit do .gitattributes
git add .gitattributes
git commit -m "chore: Configure Git LFS for binary assets"
```

---

### **4. bizantino-investidores** (Materiais de Fundraising)

```
bizantino-investidores/
├── README.md
├── pitch-decks/
│   ├── PITCH-DECK-TECH-AUTOMATION.pdf
│   ├── PITCH-DECK-TURMA-DA-AVENTURA.pdf
│   └── sources/                           # .pptx, .key, etc.
│
├── one-pagers/
│   ├── ONE-PAGER-INVESTIDORES-SPINES.md
│   └── ONE-PAGER-TURMA-DA-AVENTURA.md
│
├── financials/
│   ├── VALIDACAO-DADOS-PITCH.md
│   └── projections/
│       └── scenario-analysis.xlsx
│
├── messaging/
│   ├── EMAIL-INVESTIDORES-RESUMO.md
│   ├── MENSAGEM-INVESTIDORES-SPINES-CLONE.md
│   └── TALKING-POINTS-PITCH-INVESTIDOR.md
│
└── guides/
    ├── GUIA-USO-MATERIAIS-INVESTIDORES.md
    └── README-MATERIAIS-INVESTIDORES.md
```

**Proteção extra:**
```bash
# Repositório com senha adicional
git config credential.helper store

# Branch protegida
# Configurar no GitHub: Settings > Branches > Add rule "main"
# ✓ Require pull request reviews before merging
# ✓ Require status checks to pass
```

---

### **5. bizantino-inteligencia** (Market Intelligence)

```
bizantino-inteligencia/
├── README.md
├── amazon-kdp/
│   ├── KDP_Orders-*.xlsx                  # ⚠️ DADOS REAIS
│   ├── KDP_Royalties_Estimator-*.xlsx
│   └── reports/
│       ├── monthly-2024-12.md
│       └── monthly-2025-01.md
│
├── research/
│   ├── deep-research-gemini.txt
│   ├── gemini-deep.txt
│   └── competitor-analysis/
│
├── keywords/
│   ├── global-top-1000.csv
│   ├── amazon-top-terms-by-market.csv
│   └── trending-themes-2026.md
│
└── scripts/
    ├── amazon_keyword_mapper.py
    ├── kdp_growth_intelligence.py
    └── generate_kdp_html_report.py
```

---

## ⚙️ Configuração Inicial Passo a Passo {#configuração-inicial}

### **Etapa 1: Criar Organização GitHub**

1. **Login no GitHub** → https://github.com
2. **Criar Organization:**
   - Clicar no `+` (canto superior direito) → "New organization"
   - Nome sugerido: `trae-projetos` ou `bizantino-publishing`
   - Plan: **Free** (privacidade incluída)
   - Email da empresa
3. **Configurar Settings:**
   - Member privileges: "Members cannot create public repositories"
   - Default repository permission: "None"

### **Etapa 2: Instalar Git (se necessário)**

```powershell
# Verificar se Git está instalado
git --version

# Se não estiver, baixar de:
# https://git-scm.com/download/win

# Configurar identidade
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@empresa.com"

# Configurar editor padrão
git config --global core.editor "code --wait"  # VSCode
```

### **Etapa 3: Criar .gitignore Master**

```bash
# Criar arquivo na raiz do projeto
cd d:\TRAE-PROJETOS\livro1\BIZANTINO
```

Conteúdo do `.gitignore` (ver seção [GitIgnore Estratégico](#gitignore))

### **Etapa 4: Inicializar Primeiro Repositório (bizantino-core)**

```powershell
# Navegue para a pasta do projeto
cd d:\TRAE-PROJETOS\livro1\BIZANTINO

# Inicializar Git
git init

# Adicionar arquivos do core (sem livros/assets grandes)
git add docs/
git add scripts/
git add *.md
git add .gitignore

# Primeiro commit
git commit -m "feat: Initial commit - Bizantino Core v1.0

- Sistema de automação completo (25+ scripts)
- Documentação técnica (CLAUDE.md, DIRETRIZES)
- Pipeline de tradução gratuita (tradutor_docx_GRATUITO.py)
- Workflows de validação (6 relatórios MD)
- Inteligência de mercado (research scripts)

Status: 6 livros publicados, 331 vendas, $811 receita
Tecnologia: Claude AI + Python + Amazon KDP
"

# Criar repositório no GitHub (via web)
# GitHub.com > Organization > New repository
# Nome: bizantino-core
# Privacidade: PRIVATE
# NÃO inicializar com README (já temos)

# Conectar local ao remoto
git branch -M main
git remote add origin https://github.com/trae-projetos/bizantino-core.git

# Push inicial
git push -u origin main
```

### **Etapa 5: Criar Demais Repositórios**

Repetir processo para:
- `bizantino-livros`
- `bizantino-assets` (com Git LFS)
- `bizantino-investidores`
- `bizantino-inteligencia`

---

## 🔒 Organização de Arquivos Sensíveis {#arquivos-sensíveis}

### **Dados que NÃO devem ir para Git:**

```
❌ Senhas e API keys
❌ Tokens de acesso (Amazon KDP, Google)
❌ Dados pessoais de clientes
❌ Credenciais de pagamento
❌ Arquivos Excel com PII (Personally Identifiable Information)
```

### **Solução: Arquivo .env + .gitignore**

Criar `d:\TRAE-PROJETOS\livro1\BIZANTINO\.env`:

```env
# Amazon KDP Credentials
KDP_EMAIL=seuemail@exemplo.com
KDP_PASSWORD=SUA_SENHA_AQUI

# Google API (se usar futuramente)
GOOGLE_API_KEY=sua-chave-aqui

# FormSpree (sites)
FORMSPREE_FORM_ID=xayvpqwe

# Analytics
GOOGLE_ANALYTICS_ID=G-XXXXXXXXXX
```

No `.gitignore`:
```
.env
.env.local
.env.*.local
secrets/
credentials/
```

**Compartilhamento seguro:**
- Use **1Password** ou **Bitwarden** (gerenciadores de senha) para compartilhar com equipe
- Ou crie `.env.example` (sem valores reais):

```env
# .env.example - Template de configuração
KDP_EMAIL=seu-email-kdp@exemplo.com
KDP_PASSWORD=sua-senha-segura
GOOGLE_API_KEY=sua-chave-google-api
```

---

## 🔄 Workflow de Versionamento {#workflow}

### **Estratégia de Branches**

```
main (produção)
│
├── develop (desenvolvimento)
│   │
│   ├── feature/livro-09-vikings
│   ├── feature/traducao-frances
│   ├── fix/qa-piramides
│   └── docs/update-diretrizes
│
└── release/v1.1.0
```

### **Convenção de Commits (Conventional Commits)**

```bash
# Formato: <tipo>(escopo): <descrição>

# Tipos:
feat:     # Nova funcionalidade
fix:      # Correção de bug
docs:     # Mudanças na documentação
style:    # Formatação (não afeta código)
refactor: # Refatoração
test:     # Adicionar testes
chore:    # Tarefas de manutenção

# Exemplos práticos:
git commit -m "feat(livro-09): Adiciona manuscrito Vikings (42k palavras)"
git commit -m "fix(traducao): Corrige pontuação em tradutor_docx_GRATUITO.py"
git commit -m "docs(diretrizes): Atualiza CLAUDE.md com specs Livro 9+"
git commit -m "chore(deps): Atualiza python-docx para v0.8.11"
```

### **Workflow Diário Recomendado**

```bash
# 1. Começar o dia - Atualizar repo local
git pull origin main

# 2. Criar branch para nova tarefa
git checkout -b feature/livro-10-outline

# 3. Fazer mudanças, adicionar arquivos
git add docs/LIVRO-10-OUTLINE.md

# 4. Commit com mensagem clara
git commit -m "docs(livro-10): Cria outline inicial - Revolução Industrial"

# 5. Push para GitHub
git push origin feature/livro-10-outline

# 6. Criar Pull Request no GitHub (via web)
# Revisar mudanças → Aprovar → Merge to main

# 7. Deletar branch local (após merge)
git branch -d feature/livro-10-outline
```

---

## 🛡️ Proteção e Segurança {#segurança}

### **1. Configuração de Acesso**

**No GitHub Organization:**
- Settings → Member privileges
- Base permissions: **Read**
- Permissões por repositório:
  - `bizantino-core`: Apenas admin
  - `bizantino-livros`: Equipe editorial (write)
  - `bizantino-investidores`: Apenas founder + CFO

### **2. Branch Protection Rules**

No GitHub: Settings > Branches > Add rule

```
Branch name pattern: main

✓ Require pull request reviews before merging
  - Required approving reviews: 1
✓ Require status checks to pass before merging
✓ Require branches to be up to date before merging
✓ Include administrators
```

### **3. Two-Factor Authentication (2FA)**

⚠️ **OBRIGATÓRIO para contas com acesso aos repos**

1. GitHub → Settings → Password and authentication
2. Enable two-factor authentication
3. Use app authenticator (Google Authenticator, Authy)

### **4. Audit Log**

- GitHub Organization → Settings → Audit log
- Monitorar:
  - Quem acessou o quê
  - Mudanças em configurações
  - Downloads de código

---

## 👥 Colaboração e Escalabilidade {#colaboração}

### **Estrutura de Equipe Futura**

```
Owner/Founder (você)
│
├── Technical Lead
│   ├── Desenvolvedor Python (scripts)
│   └── DevOps (CI/CD, automação)
│
├── Editorial Lead
│   ├── Editor(a) PT
│   ├── Tradutor(a) EN/ES/DE
│   └── QA Specialist
│
├── Design Lead
│   ├── Ilustrador(a) (capas)
│   └── Designer gráfico
│
└── Business/Finance
    ├── CFO (dados investidores)
    └── Marketing (pesquisa mercado)
```

**Permissões por repo:**

| Repo | Owner | Tech | Editorial | Design | Finance |
|------|-------|------|-----------|--------|---------|
| bizantino-core | Admin | Write | Read | Read | Read |
| bizantino-livros | Admin | Read | Write | Read | None |
| bizantino-assets | Admin | Read | Read | Write | None |
| bizantino-investidores | Admin | Read | None | None | Read |
| bizantino-inteligencia | Admin | Write | Read | None | Read |

### **Onboarding de Novo Colaborador**

```bash
# 1. Adicionar à Organization no GitHub
# Organization → People → Invite member

# 2. Atribuir a um time
# Organization → Teams → Create team "Editorial"

# 3. Novo colaborador clona repositório
git clone https://github.com/trae-projetos/bizantino-livros.git
cd bizantino-livros

# 4. Instalar dependências (se applicable)
pip install -r requirements.txt

# 5. Configurar identidade local
git config user.name "Nome Colaborador"
git config user.email "email@empresa.com"

# 6. Ler documentação obrigatória
# docs/CLAUDE.md
# docs/DIRETRIZES_QUALIDADE_SERIE.md
```

---

## 💾 Backup e Redundância {#backup}

### **Estratégia Multi-Camada**

```
Layer 1: GitHub (Cloud Primary)
  └─ Push diário para main

Layer 2: Backup Local
  └─ D:\TRAE-PROJETOS\livro1\BIZANTINO
  └─ C:\Users\xberi\Documents\trae_projects\154 (backup antigo)

Layer 3: Cloud Backup (Adicional)
  └─ Google Drive / Dropbox / OneDrive
      └─ Sincronização automática

Layer 4: External Backup
  └─ HD Externo (semanal/mensal)
```

### **Automação de Backup (Script PowerShell)**

Criar `d:\TRAE-PROJETOS\livro1\BIZANTINO\backup-to-cloud.ps1`:

```powershell
# Backup automático para Google Drive
$sourceDir = "D:\TRAE-PROJETOS\livro1\BIZANTINO"
$backupDir = "C:\Users\xberi\Google Drive\Backups\BIZANTINO-$(Get-Date -Format 'yyyy-MM-dd')"

# Criar pasta com data
New-Item -ItemType Directory -Path $backupDir -Force

# Copiar tudo exceto .git (economizar espaço)
robocopy $sourceDir $backupDir /MIR /XD .git /R:3 /W:5 /LOG:"$backupDir\backup-log.txt"

Write-Host "✅ Backup concluído: $backupDir"
```

**Agendar no Windows Task Scheduler:**
```
Trigger: Diariamente às 23:00
Action: powershell.exe -File "D:\TRAE-PROJETOS\livro1\BIZANTINO\backup-to-cloud.ps1"
```

---

## 🚫 GitIgnore Estratégico {#gitignore}

Criar `d:\TRAE-PROJETOS\livro1\BIZANTINO\.gitignore`:

```gitignore
# ================================================================================
# BIZANTINO - GitIgnore Master
# ================================================================================

# -------------------------
# 1. CREDENCIAIS E SECRETS
# -------------------------
.env
.env.local
.env.*.local
secrets/
credentials/
kdp-credentials.txt
api-keys.txt

# -------------------------
# 2. PYTHON
# -------------------------
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Ambientes virtuais
venv/
env/
ENV/
env.bak/
venv.bak/

# -------------------------
# 3. ARQUIVOS TEMPORÁRIOS
# -------------------------
temp_*
tmp/
*.tmp
~$*
.~lock.*

# -------------------------
# 4. SISTEMA OPERACIONAL
# -------------------------
# Windows
Thumbs.db
ehthumbs.db
Desktop.ini
$RECYCLE.BIN/
*.cab
*.msi
*.msix
*.msm
*.msp
*.lnk

# macOS
.DS_Store
.AppleDouble
.LSOverride
Icon
._*
.Spotlight-V100
.Trashes

# -------------------------
# 5. IDEs E EDITORES
# -------------------------
# VSCode
.vscode/
*.code-workspace

# PyCharm
.idea/
*.iml
*.iws

# Sublime
*.sublime-project
*.sublime-workspace

# -------------------------
# 6. ARQUIVOS GRANDES/BINÁRIOS
# -------------------------
# (Usar Git LFS para estes)
# *.pdf
# *.docx
# *.xlsx

# Mas ignorar versões "rascunho"
*-RASCUNHO.pdf
*-DRAFT.docx
*-TEMP.xlsx

# -------------------------
# 7. ARQUIVOS DE LOG
# -------------------------
*.log
logs/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# -------------------------
# 8. OUTPUTS DE SCRIPTS
# -------------------------
output/
generated/
*.output.txt
*-OUTPUT.md

# -------------------------
# 9. ARQUIVOS ESPECÍFICOS DO PROJETO
# -------------------------
# Backups locais (já temos no GitHub)
ARQUIVADOS/backup-*

# Versões antigas
*-OLD.*
*-ANTIGO.*
CERTOOOOOOOOOOOOOO.docx
FINALAAAAAA.docx

# Arquivos de teste
test_*.txt
teste-*.py

# -------------------------
# 10. DADOS SENSÍVEIS KDP
# -------------------------
# (Git LFS para versões controladas)
# Mas ignorar downloads diretos:
KDP_Orders-*.csv
KDP_Sales-*.csv
personal-data.xlsx

# -------------------------
# FIM
# -------------------------
```

---

## 📝 Comandos Essenciais Git {#comandos}

### **Comandos Básicos Diários**

```bash
# Ver status dos arquivos
git status

# Adicionar arquivo específico
git add caminho/para/arquivo.py

# Adicionar todos os arquivos modificados
git add .

# Commit com mensagem
git commit -m "sua mensagem aqui"

# Push para GitHub
git push origin main

# Pull (baixar) mudanças do GitHub
git pull origin main

# Ver histórico de commits
git log --oneline --graph --all

# Ver diferenças antes de commitar
git diff
```

### **Trabalhando com Branches**

```bash
# Criar nova branch
git checkout -b feature/nova-funcionalidade

# Trocar de branch
git checkout main

# Listar branches
git branch -a

# Mergear branch (estando em main)
git merge feature/nova-funcionalidade

# Deletar branch local
git branch -d feature/nova-funcionalidade

# Deletar branch remota
git push origin --delete feature/nova-funcionalidade
```

### **Desfazer Mudanças**

```bash
# Desfazer mudanças em arquivo (antes de add)
git checkout -- arquivo.py

# Remover arquivo do stage (após add, antes de commit)
git reset HEAD arquivo.py

# Desfazer último commit (mantém mudanças)
git reset --soft HEAD~1

# Desfazer último commit (DESCARTA mudanças) ⚠️
git reset --hard HEAD~1

# Reverter commit específico (cria novo commit)
git revert abc1234
```

### **Comandos Avançados**

```bash
# Ver quem modificou cada linha de um arquivo
git blame arquivo.py

# Procurar em todo histórico
git log --all --grep="palavra-chave"

# Ver mudanças em arquivo específico
git log -p -- caminho/arquivo.py

# Stash (guardar mudanças temporariamente)
git stash
git stash pop

# Cherry-pick (aplicar commit específico)
git cherry-pick abc1234

# Rebase (reorganizar commits)
git rebase -i HEAD~3
```

---

## 🎬 Script de Inicialização Completa

Criar `d:\TRAE-PROJETOS\livro1\BIZANTINO\setup-github.ps1`:

```powershell
# ================================================================================
# BIZANTINO - Setup GitHub Completo
# ================================================================================

Write-Host "🚀 Iniciando setup do GitHub para Projeto Bizantino..." -ForegroundColor Cyan

# -------------------------
# 1. VERIFICAR REQUISITOS
# -------------------------
Write-Host "`n📋 Verificando requisitos..." -ForegroundColor Yellow

# Verificar Git
if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Git não instalado. Baixe em: https://git-scm.com/download/win" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Git instalado: $(git --version)" -ForegroundColor Green

# Verificar configuração Git
$gitUser = git config --global user.name
$gitEmail = git config --global user.email

if (!$gitUser -or !$gitEmail) {
    Write-Host "⚠️  Configurar identidade Git:" -ForegroundColor Yellow
    $nome = Read-Host "Digite seu nome"
    $email = Read-Host "Digite seu email"
    
    git config --global user.name $nome
    git config --global user.email $email
    Write-Host "✅ Identidade configurada" -ForegroundColor Green
}

# -------------------------
# 2. CRIAR .GITIGNORE
# -------------------------
Write-Host "`n📄 Criando .gitignore..." -ForegroundColor Yellow

$gitignoreContent = @"
# BIZANTINO - GitIgnore Master
__pycache__/
*.py[cod]
.env
.env.local
temp_*
*.tmp
~$*
.DS_Store
Thumbs.db
.vscode/
*.log
ARQUIVADOS/backup-*
*-OLD.*
"@

$gitignoreContent | Out-File -FilePath ".gitignore" -Encoding UTF8
Write-Host "✅ .gitignore criado" -ForegroundColor Green

# -------------------------
# 3. INICIALIZAR REPOSITÓRIO
# -------------------------
Write-Host "`n🔧 Inicializando repositório Git..." -ForegroundColor Yellow

if (Test-Path ".git") {
    Write-Host "⚠️  Repositório Git já existe" -ForegroundColor Yellow
} else {
    git init
    git branch -M main
    Write-Host "✅ Repositório iniciado" -ForegroundColor Green
}

# -------------------------
# 4. PRIMEIRO COMMIT
# -------------------------
Write-Host "`n💾 Preparando primeiro commit..." -ForegroundColor Yellow

git add docs/
git add scripts/
git add *.md
git add .gitignore

$commitMessage = @"
feat: Initial commit - Bizantino Core v1.0

- Sistema de automação completo (25+ scripts Python)
- Documentação técnica (CLAUDE.md, DIRETRIZES)
- Pipeline de tradução gratuita
- Workflows de validação
- Inteligência de mercado

Status: 6 livros publicados, 331 vendas
Tecnologia: Claude AI + Python + Amazon KDP
"@

git commit -m $commitMessage
Write-Host "✅ Primeiro commit realizado" -ForegroundColor Green

# -------------------------
# 5. INSTRUÇÕES FINAIS
# -------------------------
Write-Host "`n" -NoNewline
Write-Host "=" * 80 -ForegroundColor Cyan
Write-Host "✨ PRÓXIMOS PASSOS:" -ForegroundColor Cyan
Write-Host "=" * 80 -ForegroundColor Cyan

Write-Host @"

1️⃣  Criar repositório no GitHub:
   → https://github.com/organizations/trae-projetos/repositories/new
   Nome: bizantino-core
   Privacidade: ✓ Private
   NÃO inicializar com README

2️⃣  Conectar repositório local ao GitHub:
   git remote add origin https://github.com/trae-projetos/bizantino-core.git
   git push -u origin main

3️⃣  Autenticação (primeira vez):
   Será solicitado usuário/senha GitHub
   Use Personal Access Token (não senha):
   → https://github.com/settings/tokens/new
   Scopes: repo (full control)

4️⃣  Repetir processo para outros repositórios:
   - bizantino-livros
   - bizantino-assets (com Git LFS)
   - bizantino-investidores
   - bizantino-inteligencia

📚 Documentação completa: GUIA-GITHUB-VERSIONAMENTO.md

"@

Write-Host "=" * 80 -ForegroundColor Cyan
Write-Host "✅ Setup concluído!" -ForegroundColor Green
```

---

## 🔐 Configuração de Personal Access Token

### **Como Criar Token no GitHub**

1. **Login GitHub** → Settings (canto superior direito)
2. **Developer settings** (menu esquerdo, final)
3. **Personal access tokens** → Tokens (classic)
4. **Generate new token** → Generate new token (classic)

**Configurações do Token:**
```
Note: Bizantino Project - Full Access
Expiration: No expiration (ou 1 ano)

Scopes:
✓ repo (Full control of private repositories)
  ✓ repo:status
  ✓ repo_deployment
  ✓ public_repo
  ✓ repo:invite
  ✓ security_events
✓ workflow
✓ write:packages
✓ read:packages
```

5. **Generate token**
6. **Copiar token** (só será mostrado uma vez!)

**Salvar token com segurança:**
```bash
# Windows - Credential Manager
git config --global credential.helper manager

# Ou manualmente em arquivo .env (NÃO COMMITAR!)
GITHUB_TOKEN=ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

**Uso do token:**
```bash
# Quando Git pedir senha, usar o TOKEN (não a senha GitHub)
git push origin main
Username: seu-usuario-github
Password: ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## 📊 Dashboard de Versionamento (Opcional)

### **Criar README.md Visual no Repositório**

```markdown
# 🚀 Bizantino Core - Sistema de Publicação Automatizada

![Status](https://img.shields.io/badge/status-active-success)
![Vendas](https://img.shields.io/badge/vendas-331-blue)
![Livros](https://img.shields.io/badge/livros%20publicados-6-brightgreen)
![Receita](https://img.shields.io/badge/receita-$811-green)

## 📖 Sobre

Sistema de automação para publicação de livros infantis usando IA (Claude AI + Google Gemini).

- **95% de automação** do processo editorial
- **$10-25/livro** vs $5.000 da concorrência (Spines)
- **4 idiomas simultâneos** (PT, EN, ES, DE)
- **10 países** distribuição via Amazon KDP

## 🏗️ Estrutura do Projeto

```
bizantino-core/
├── docs/              # Documentação técnica
├── scripts/           # Automação (Python)
│   ├── 1-MANUSCRITO/
│   ├── 2-TRADUCAO/   # ⭐ Sistema crítico
│   ├── 3-FORMATACAO-KDP/
│   ├── 4-ANALISE/
│   ├── 5-MARKETING-RESEARCH/
│   └── 6-GERACAO-IMAGENS/
└── config/
```

## 🚀 Quick Start

```bash
# Clonar repositório
git clone https://github.com/trae-projetos/bizantino-core.git
cd bizantino-core

# Instalar dependências
pip install -r scripts/requirements.txt

# Ler documentação obrigatória
cat docs/CLAUDE.md
```

## 📝 Workflow de Contribuição

1. Criar branch: `git checkout -b feature/minha-feature`
2. Fazer mudanças
3. Commit: `git commit -m "feat: Descrição clara"`
4. Push: `git push origin feature/minha-feature`
5. Criar Pull Request no GitHub

## 📊 Métricas (atualizado 2026-01-10)

| Métrica | Valor |
|---------|-------|
| Livros Publicados | 6 |
| Títulos (total) | 28 (6×4 idiomas) |
| Vendas | 331 |
| KENP (páginas) | 24.823 |
| Receita | $811 USD |
| Marketing | $0 |
| Crescimento | 3x/mês |

## 🔗 Links Relacionados

- [bizantino-livros](https://github.com/trae-projetos/bizantino-livros) - Manuscritos
- [bizantino-assets](https://github.com/trae-projetos/bizantino-assets) - Recursos visuais
- [bizantino-investidores](https://github.com/trae-projetos/bizantino-investidores) - Pitch decks

## 📄 Licença

Proprietary - Todos os direitos reservados © 2026 TRAE Projetos
```

---

## ✅ Checklist Final de Setup

Antes de começar a usar GitHub:

- [ ] Git instalado e configurado
- [ ] Conta GitHub criada
- [ ] Organization `trae-projetos` criada
- [ ] Personal Access Token gerado
- [ ] `.gitignore` criado e testado
- [ ] First commit preparado (docs + scripts apenas)
- [ ] Repositório `bizantino-core` criado no GitHub
- [ ] Remote `origin` configurado
- [ ] Push inicial realizado com sucesso
- [ ] Git LFS instalado (para bizantino-assets)
- [ ] Two-Factor Authentication habilitado
- [ ] Backup local mantido (D:\TRAE-PROJETOS)
- [ ] Documentação lida (GUIA-GITHUB-VERSIONAMENTO.md)

---

## 🆘 Troubleshooting

### **Erro: "Permission denied (publickey)"**

```bash
# Solução: Usar HTTPS em vez de SSH
git remote set-url origin https://github.com/trae-projetos/bizantino-core.git
```

### **Erro: "Repository not found"**

```bash
# Verificar se URL está correta
git remote -v

# Reconfigurar origin
git remote remove origin
git remote add origin https://github.com/trae-projetos/bizantino-core.git
```

### **Erro: "Failed to push some refs"**

```bash
# Pull primeiro (pode haver mudanças remotas)
git pull origin main --rebase

# Depois push
git push origin main
```

### **Arquivo muito grande (> 100 MB)**

```bash
# Instalar Git LFS
git lfs install

# Rastrear tipo de arquivo
git lfs track "*.pdf"

# Adicionar .gitattributes
git add .gitattributes

# Commit normal
git add arquivo-grande.pdf
git commit -m "chore: Adiciona PDF grande via LFS"
git push
```

---

## 📚 Recursos Adicionais

### **Documentação Oficial**
- Git: https://git-scm.com/doc
- GitHub: https://docs.github.com
- Git LFS: https://git-lfs.github.com

### **Guias Interativos**
- Learn Git Branching: https://learngitbranching.js.org
- GitHub Skills: https://skills.github.com

### **Cheat Sheets**
- Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf
- Conventional Commits: https://www.conventionalcommits.org

---

## 📞 Suporte

Para dúvidas ou problemas:

1. **Consultar este guia** (`GUIA-GITHUB-VERSIONAMENTO.md`)
2. **Documentação do projeto** (`MAPEAMENTO_COMPLETO_PROJETO_BIZANTINO.txt`)
3. **GitHub Issues** (criar issue no repositório relevante)
4. **Claude AI** (assistente técnico do projeto)

---

**Versão**: 1.0  
**Data**: 2026-01-10  
**Autor**: Claude Code (Anthropic) + TRAE Projetos  
**Próxima revisão**: Após setup inicial completo

---

## 🎯 Próximos Passos Imediatos

1. **Executar** `setup-github.ps1`
2. **Criar** repositórios no GitHub (via web)
3. **Conectar** repos locais aos remotos
4. **Push** inicial de todos os repos
5. **Configurar** branch protection em `main`
6. **Documentar** processo no `CHANGELOG.md`
7. **Testar** workflow completo (clone → edit → commit → push)

**Tempo estimado**: 2-3 horas para setup completo de todos os repositórios.

✨ **Boa sorte com o versionamento!**
