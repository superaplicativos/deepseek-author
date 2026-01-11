# ================================================================================
# BIZANTINO - Setup GitHub Completo
# Script de inicialização automática do controle de versionamento
# ================================================================================

Write-Host @"

╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║           🚀 BIZANTINO - Setup GitHub para Controle Empresarial           ║
║                                                                           ║
║  Sistema de publicação automatizada de livros infantis                   ║
║  6 livros publicados │ 331 vendas │ $811 receita │ $0 marketing          ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

"@ -ForegroundColor Cyan

# -------------------------
# 1. VERIFICAR REQUISITOS
# -------------------------
Write-Host "`n📋 ETAPA 1/6: Verificando requisitos..." -ForegroundColor Yellow

# Verificar Git
Write-Host "Verificando Git..." -NoNewline
if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host " ❌" -ForegroundColor Red
    Write-Host "`nGit não está instalado. Por favor, instale antes de continuar:" -ForegroundColor Red
    Write-Host "https://git-scm.com/download/win`n" -ForegroundColor Yellow
    Read-Host "Pressione Enter para abrir o site de download"
    Start-Process "https://git-scm.com/download/win"
    exit 1
}
$gitVersion = git --version
Write-Host " ✅ ($gitVersion)" -ForegroundColor Green

# Verificar Python
Write-Host "Verificando Python..." -NoNewline
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host " ⚠️  Python não detectado (opcional)" -ForegroundColor Yellow
} else {
    $pythonVersion = python --version
    Write-Host " ✅ ($pythonVersion)" -ForegroundColor Green
}

# Verificar configuração Git
$gitUser = git config --global user.name
$gitEmail = git config --global user.email

if (!$gitUser -or !$gitEmail) {
    Write-Host "`n⚙️  Configuração de identidade Git necessária" -ForegroundColor Yellow
    Write-Host "=" * 70 -ForegroundColor Gray
    
    $nome = Read-Host "`nDigite seu nome completo"
    $email = Read-Host "Digite seu email profissional"
    
    git config --global user.name $nome
    git config --global user.email $email
    
    Write-Host "`n✅ Identidade Git configurada:" -ForegroundColor Green
    Write-Host "   Nome:  $nome" -ForegroundColor Gray
    Write-Host "   Email: $email" -ForegroundColor Gray
} else {
    Write-Host "✅ Identidade Git já configurada:" -ForegroundColor Green
    Write-Host "   Nome:  $gitUser" -ForegroundColor Gray
    Write-Host "   Email: $gitEmail" -ForegroundColor Gray
}

# -------------------------
# 2. CRIAR .GITIGNORE
# -------------------------
Write-Host "`n📄 ETAPA 2/6: Criando .gitignore estratégico..." -ForegroundColor Yellow

$gitignorePath = ".gitignore"

if (Test-Path $gitignorePath) {
    Write-Host "⚠️  Arquivo .gitignore já existe. Deseja sobrescrever?" -ForegroundColor Yellow
    $resposta = Read-Host "Digite 's' para sobrescrever, qualquer outra tecla para manter o atual"
    if ($resposta -ne 's') {
        Write-Host "✅ Mantendo .gitignore existente" -ForegroundColor Green
        $criarGitignore = $false
    } else {
        $criarGitignore = $true
    }
} else {
    $criarGitignore = $true
}

if ($criarGitignore) {
    $gitignoreContent = @"
# ================================================================================
# BIZANTINO - GitIgnore Master
# Sistema de Publicação Automatizada de Livros Infantis
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
*.key
*.pem

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
.venv/

# -------------------------
# 3. ARQUIVOS TEMPORÁRIOS
# -------------------------
temp_*
tmp/
*.tmp
~$*
.~lock.*
*.swp
*~

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

# Linux
*~
.directory

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

# Sublime Text
*.sublime-project
*.sublime-workspace

# Vim
*.swp
*.swo
*~

# -------------------------
# 6. ARQUIVOS GRANDES/BINÁRIOS (usar Git LFS se necessário)
# -------------------------
# Rascunhos e versões temporárias
*-RASCUNHO.pdf
*-DRAFT.docx
*-TEMP.xlsx
*-WIP.*

# -------------------------
# 7. ARQUIVOS DE LOG
# -------------------------
*.log
logs/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# -------------------------
# 8. OUTPUTS DE SCRIPTS
# -------------------------
output/
generated/
*.output.txt
*-OUTPUT.md
*_output/

# -------------------------
# 9. ARQUIVOS ESPECÍFICOS DO PROJETO BIZANTINO
# -------------------------
# Backups locais (já versionados no GitHub)
ARQUIVADOS/backup-*
*-backup-*.zip

# Versões antigas não versionáveis
*-OLD.*
*-ANTIGO.*
*-v0.*
CERTOOOOOOOOOOOOOO.docx
FINALAAAAAA.docx

# Arquivos de teste
test_*.txt
teste-*.py
*_teste.*

# Arquivos temporários de conversão
*-convertido-temp.*
*-traducao-temp.*

# -------------------------
# 10. DADOS SENSÍVEIS KDP E ANALYTICS
# -------------------------
# Downloads diretos KDP (usar Git LFS para versões controladas em repo específico)
KDP_Orders-*.csv
KDP_Sales-*.csv
KDP_Royalties-*.csv
kdp-raw-data/

# Dados pessoais
personal-data.xlsx
customer-emails.txt
pii-data/

# -------------------------
# 11. NODE_MODULES (se usar Node.js futuro)
# -------------------------
node_modules/
package-lock.json
yarn.lock

# -------------------------
# 12. CONFIGURAÇÕES LOCAIS
# -------------------------
# Configurações específicas da máquina
.local/
local-config.yaml
local-settings.json

# -------------------------
# FIM DO GITIGNORE
# ================================================================================
# 
# NOTAS:
# - Arquivos DOCX/PDF de produção DEVEM ser versionados (são assets do negócio)
# - Usar Git LFS para arquivos > 50MB
# - Dados sensíveis devem ficar em .env (nunca commitar)
# - Manter backup local mesmo com GitHub
#
# Criado: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
# Versão: 1.0
# ================================================================================
"@

    $gitignoreContent | Out-File -FilePath $gitignorePath -Encoding UTF8
    Write-Host "✅ .gitignore criado com sucesso ($((Get-Item $gitignorePath).Length) bytes)" -ForegroundColor Green
}

# -------------------------
# 3. CRIAR .ENV.EXAMPLE
# -------------------------
Write-Host "`n🔐 ETAPA 3/6: Criando template de variáveis de ambiente..." -ForegroundColor Yellow

$envExamplePath = ".env.example"
if (!(Test-Path $envExamplePath)) {
    $envExampleContent = @"
# ================================================================================
# BIZANTINO - Template de Variáveis de Ambiente
# ================================================================================
# IMPORTANTE: Este arquivo NÃO contém valores reais.
# Copie para .env e preencha com suas credenciais reais.
# O arquivo .env será automaticamente ignorado pelo Git (.gitignore)

# -------------------------
# AMAZON KDP
# -------------------------
KDP_EMAIL=seu-email-kdp@exemplo.com
KDP_PASSWORD=sua-senha-super-segura

# -------------------------
# GOOGLE APIs (quando necessário)
# -------------------------
GOOGLE_API_KEY=sua-chave-google-api
GOOGLE_CLOUD_PROJECT_ID=seu-project-id

# -------------------------
# GEMINI AI (geração de imagens)
# -------------------------
GEMINI_API_KEY=sua-chave-gemini

# -------------------------
# CLAUDE AI (se usar API)
# -------------------------
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx

# -------------------------
# FORMSPREE (formulários sites)
# -------------------------
FORMSPREE_FORM_ID=xayvpqwe

# -------------------------
# ANALYTICS
# -------------------------
GOOGLE_ANALYTICS_ID=G-XXXXXXXXXX
FACEBOOK_PIXEL_ID=123456789012345

# -------------------------
# GITHUB
# -------------------------
GITHUB_TOKEN=ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# -------------------------
# OUTRAS CONFIGURAÇÕES
# -------------------------
AMBIENTE=desenvolvimento
DEBUG=true

# ================================================================================
# INSTRUÇÕES:
# 1. Copie este arquivo: cp .env.example .env
# 2. Preencha com valores reais no arquivo .env
# 3. NUNCA commite o arquivo .env (está no .gitignore)
# ================================================================================
"@

    $envExampleContent | Out-File -FilePath $envExamplePath -Encoding UTF8
    Write-Host "✅ .env.example criado (template de credenciais)" -ForegroundColor Green
} else {
    Write-Host "✅ .env.example já existe" -ForegroundColor Green
}

# -------------------------
# 4. INICIALIZAR REPOSITÓRIO GIT
# -------------------------
Write-Host "`n🔧 ETAPA 4/6: Inicializando repositório Git..." -ForegroundColor Yellow

if (Test-Path ".git") {
    Write-Host "⚠️  Repositório Git já existe nesta pasta" -ForegroundColor Yellow
    Write-Host "Status atual:" -ForegroundColor Gray
    git status --short | Select-Object -First 10 | ForEach-Object { Write-Host "   $_" -ForegroundColor Gray }
} else {
    Write-Host "Criando novo repositório Git..." -NoNewline
    git init | Out-Null
    git branch -M main
    Write-Host " ✅" -ForegroundColor Green
    Write-Host "Branch principal: main" -ForegroundColor Gray
}

# -------------------------
# 5. PREPARAR PRIMEIRO COMMIT
# -------------------------
Write-Host "`n💾 ETAPA 5/6: Preparando primeiro commit (bizantino-core)..." -ForegroundColor Yellow

Write-Host "`nEste commit incluirá:" -ForegroundColor Cyan
Write-Host "  ✓ Documentação técnica (docs/)" -ForegroundColor Gray
Write-Host "  ✓ Scripts de automação (scripts/)" -ForegroundColor Gray
Write-Host "  ✓ Arquivos README e guias" -ForegroundColor Gray
Write-Host "  ✓ Configurações (.gitignore, .env.example)" -ForegroundColor Gray
Write-Host "  ✗ Livros completos (irão para bizantino-livros)" -ForegroundColor DarkGray
Write-Host "  ✗ Assets grandes (irão para bizantino-assets)" -ForegroundColor DarkGray

$prosseguir = Read-Host "`nDeseja prosseguir com o primeiro commit? (s/n)"
if ($prosseguir -ne 's') {
    Write-Host "`n⚠️  Setup cancelado pelo usuário" -ForegroundColor Yellow
    Write-Host "Você pode executar este script novamente quando estiver pronto.`n" -ForegroundColor Gray
    exit 0
}

# Adicionar arquivos estratégicos
Write-Host "`nAdicionando arquivos ao Git..." -ForegroundColor Yellow

# Docs
if (Test-Path "docs") {
    git add docs/
    Write-Host "  ✅ docs/" -ForegroundColor Green
}
if (Test-Path "DOCS") {
    git add DOCS/
    Write-Host "  ✅ DOCS/" -ForegroundColor Green
}

# Scripts
if (Test-Path "scripts") {
    git add scripts/
    Write-Host "  ✅ scripts/" -ForegroundColor Green
}
if (Test-Path "SCRIPTS") {
    git add SCRIPTS/
    Write-Host "  ✅ SCRIPTS/" -ForegroundColor Green
}

# READMEs e guias
git add *.md
Write-Host "  ✅ Arquivos .md (README, guias)" -ForegroundColor Green

# Configurações
git add .gitignore
git add .env.example
Write-Host "  ✅ Configurações (.gitignore, .env.example)" -ForegroundColor Green

# Sites HTML (sem dados sensíveis)
if (Test-Path "site-*.html") {
    git add site-*.html
    Write-Host "  ✅ Sites HTML" -ForegroundColor Green
}
if (Test-Path "index.html") {
    git add index.html
    Write-Host "  ✅ index.html" -ForegroundColor Green
}

# Commit
Write-Host "`nCriando commit inicial..." -ForegroundColor Yellow

$commitMessage = @"
feat: Initial commit - Bizantino Core v1.0

Sistema de automação completo para publicação de livros infantis usando IA.

## 📦 Componentes Incluídos

### Automação (95% do processo)
- 25+ scripts Python organizados por função
- Pipeline de tradução gratuita (Google Translate via web)
- Formatação automática Amazon KDP
- Geração de prompts para imagens (Gemini AI)
- Marketing research e keyword intelligence

### Documentação Técnica
- CLAUDE.md: Guia master para assistentes IA
- DIRETRIZES_QUALIDADE_SERIE.md: Padrões editoriais
- DIRETRIZES_VISUAIS_IDENTIDADE.md: Identidade visual
- epic-book-writer.md: Agente de narrativa

### Sistemas
1. MANUSCRITO: Conversão TXT → DOCX
2. TRADUCAO: PT → EN/ES/DE (preserva formatação)
3. FORMATACAO-KDP: Ajuste para Amazon KDP
4. ANALISE: QA e validação
5. MARKETING-RESEARCH: Inteligência de mercado
6. GERACAO-IMAGENS: Prompts para Gemini AI

## 📊 Status do Projeto

- Livros publicados: 6
- Títulos (4 idiomas): 28
- Vendas validadas: 331
- KENP (páginas lidas): 24.823
- Receita total: $811 USD
- Investimento marketing: $0
- Crescimento: 3x/mês

## 🚀 Tecnologias

- Claude AI (Anthropic) - Geração de manuscritos
- Google Gemini - Geração de ilustrações
- Python 3.x - Automação
- Amazon KDP - Publicação e distribuição
- LibreOffice - Exportação EPUB

## 🎯 Próximos Passos

1. Conectar ao GitHub remoto
2. Configurar repositórios adicionais (livros, assets, investidores)
3. Setup Git LFS para arquivos grandes
4. Publicar Livros 7-8 (em QA)
5. Escalar para 10 contas KDP

---

Criado: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
Versão: 1.0
"@

git commit -m $commitMessage
Write-Host "✅ Commit inicial criado" -ForegroundColor Green

$commitHash = git rev-parse --short HEAD
Write-Host "   Hash: $commitHash" -ForegroundColor Gray

# -------------------------
# 6. INSTRUÇÕES FINAIS
# -------------------------
Write-Host "`n" -NoNewline
Write-Host "=" * 80 -ForegroundColor Cyan
Write-Host "✨ SETUP CONCLUÍDO COM SUCESSO!" -ForegroundColor Green
Write-Host "=" * 80 -ForegroundColor Cyan

Write-Host @"

📋 PRÓXIMOS PASSOS CRÍTICOS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣  CRIAR REPOSITÓRIO NO GITHUB
    
    a) Acesse: https://github.com/new
    
    b) Configurações recomendadas:
       Owner: [sua-conta] ou criar Organization "trae-projetos"
       Repository name: bizantino-core
       Description: Sistema de automação para publicação de livros infantis com IA
       Visibility: ✓ Private (IMPORTANTE!)
       
       NÃO marcar:
       ☐ Add a README file
       ☐ Add .gitignore
       ☐ Choose a license
    
    c) Clique "Create repository"


2️⃣  CONECTAR REPOSITÓRIO LOCAL AO GITHUB

    Após criar o repositório, copie a URL e execute:
    
    git remote add origin https://github.com/SEU-USUARIO/bizantino-core.git
    git push -u origin main


3️⃣  AUTENTICAÇÃO (primeira vez)

    Quando solicitar credenciais, use:
    
    Username: seu-usuario-github
    Password: USE UM PERSONAL ACCESS TOKEN (não sua senha!)
    
    Para criar token:
    → https://github.com/settings/tokens/new
    
    Configurações do token:
    • Note: Bizantino Project Access
    • Expiration: No expiration (ou 1 ano)
    • Select scopes: ✓ repo (Full control of private repositories)
    
    ⚠️  Salve o token em local seguro! Será mostrado apenas uma vez.


4️⃣  CRIAR DEMAIS REPOSITÓRIOS

    Repetir processo para:
    
    a) bizantino-livros
       → Manuscritos e traduções
       → Relatórios de validação
    
    b) bizantino-assets (requer Git LFS)
       → Personagens chromakey
       → Capas por idioma
       → Imagens internas
    
    c) bizantino-investidores
       → Pitch decks
       → Dados financeiros
       → Materiais para fundraising
    
    d) bizantino-inteligencia
       → Pesquisa de mercado
       → Keywords research
       → Analytics KDP


5️⃣  CONFIGURAR GIT LFS (para bizantino-assets)

    # Instalar Git LFS
    → https://git-lfs.github.com/
    
    # No repositório bizantino-assets:
    git lfs install
    git lfs track "*.jpg"
    git lfs track "*.png"
    git lfs track "*.psd"
    git lfs track "*.docx"
    git add .gitattributes
    git commit -m "chore: Configure Git LFS for binary assets"


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 DOCUMENTAÇÃO COMPLETA:

   • GUIA-GITHUB-VERSIONAMENTO.md (nesta pasta)
     → Estratégia completa de multi-repositório
     → Workflows de colaboração
     → Segurança e proteção
     → Comandos Git essenciais

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"@ -ForegroundColor White

Write-Host "✅ Tudo pronto para conectar ao GitHub!" -ForegroundColor Green
Write-Host "`nEstimate de tempo para completar passos 1-5: 30-60 minutos`n" -ForegroundColor Gray

# Perguntar se quer abrir GitHub
$abrirGitHub = Read-Host "Deseja abrir o GitHub no navegador agora? (s/n)"
if ($abrirGitHub -eq 's') {
    Start-Process "https://github.com/new"
    Write-Host "`n🌐 GitHub aberto no navegador" -ForegroundColor Green
}

Write-Host "`n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "  Script finalizado. Boa sorte com o versionamento! 🚀" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`n" -ForegroundColor Cyan
