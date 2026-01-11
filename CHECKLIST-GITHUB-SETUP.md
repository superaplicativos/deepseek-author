# 📋 Checklist Interativo - Setup GitHub Bizantino

**Use este arquivo para acompanhar seu progresso no setup do GitHub**  
Marque cada item com `[x]` conforme completar.

---

## 🎯 FASE 1: Preparação (Essencial)

### Pré-requisitos

- [ ] **Git instalado**
  - Verificar: `git --version` no PowerShell
  - Download: https://git-scm.com/download/win
  - Versão mínima: 2.0+

- [ ] **Conta GitHub criada**
  - URL: https://github.com/join
  - Usar email profissional
  - Username profissional (ex: trae-projetos)

- [ ] **Two-Factor Authentication habilitado**
  - GitHub → Settings → Password and authentication
  - App: Google Authenticator, Authy, ou Microsoft Authenticator
  - ⚠️ **CRÍTICO para segurança empresarial**

- [ ] **Personal Access Token criado**
  - URL: https://github.com/settings/tokens/new
  - Note: `Bizantino Project - Full Access`
  - Expiration: `No expiration` (ou 1 ano)
  - Scopes: ✓ `repo` (Full control of private repositories)
  - **Token salvo em local seguro** (1Password, Bitwarden, ou arquivo criptografado)

---

## 🔧 FASE 2: Setup Local (20-30 min)

### Configuração Git

- [ ] **Identidade configurada**
  ```powershell
  git config --global user.name "Seu Nome Completo"
  git config --global user.email "seuemail@empresa.com"
  ```
  - Verificar: `git config --global --list`

- [ ] **Editor padrão configurado (opcional)**
  ```powershell
  git config --global core.editor "code --wait"  # VSCode
  # OU
  git config --global core.editor "notepad"      # Notepad
  ```

- [ ] **Credential helper configurado (Windows)**
  ```powershell
  git config --global credential.helper manager
  ```

### Setup Automático

- [ ] **Script `setup-github.ps1` executado**
  ```powershell
  cd d:\TRAE-PROJETOS\livro1\BIZANTINO
  .\setup-github.ps1
  ```
  - Tempo: ~5-10 minutos
  - Verificar saída: "✅ Setup concluído"

- [ ] **`.gitignore` criado e revisado**
  - Verificar arquivo existe
  - Revisar conteúdo (credenciais, temporários, etc.)

- [ ] **`.env.example` criado**
  - Template de variáveis de ambiente
  - NÃO contém valores reais

- [ ] **Primeiro commit local criado**
  - Verificar: `git log --oneline`
  - Deve mostrar commit inicial

---

## 🌐 FASE 3: GitHub - bizantino-core (15-20 min)

### Criar Repositório Principal

- [ ] **Organization criada (opcional, mas recomendado)**
  - GitHub → `+` → New organization
  - Nome: `trae-projetos` ou `bizantino-publishing`
  - Plan: Free (privacidade incluída)
  - Email: email@empresa.com

- [ ] **Repositório `bizantino-core` criado**
  - URL: https://github.com/new
  - Owner: [sua-conta] ou [organization]
  - Repository name: `bizantino-core`
  - Description: `Sistema de automação para publicação de livros infantis com IA (Claude + Gemini)`
  - Visibility: **✓ Private** ⚠️
  - **NÃO** marcar:
    - ☐ Add a README file
    - ☐ Add .gitignore
    - ☐ Choose a license

### Conectar Local ao Remoto

- [ ] **Remote configurado**
  ```powershell
  git remote add origin https://github.com/SEU-USUARIO/bizantino-core.git
  ```
  - Verificar: `git remote -v`

- [ ] **Push inicial realizado**
  ```powershell
  git push -u origin main
  ```
  - Usar **Personal Access Token** como password
  - Verificar: "Branch 'main' set up to track remote branch 'main'"

- [ ] **Repositório verificado no navegador**
  - Abrir: https://github.com/SEU-USUARIO/bizantino-core
  - ✓ Arquivos docs/ visíveis
  - ✓ Arquivos scripts/ visíveis
  - ✓ README.md visível
  - ✓ .gitignore visível

### Proteções de Segurança

- [ ] **Branch protection configurada**
  - Repo → Settings → Branches → Add rule
  - Branch name pattern: `main`
  - Configurações:
    - ✓ Require pull request reviews before merging
    - ✓ Require status checks to pass before merging
    - ✓ Include administrators

- [ ] **Acesso auditável**
  - Organization → Settings → Audit log
  - Verificar eventos de criação do repo

---

## 📚 FASE 4: Repositórios Adicionais (30-45 min)

### bizantino-livros

- [ ] **Repositório criado** (GitHub → New repository)
  - Nome: `bizantino-livros`
  - Private: ✓
  - Descrição: `Manuscritos, traduções e validações da série Turma da Aventura`

- [ ] **Organizados localmente**
  ```powershell
  # Criar pasta separada ou subdiretório
  mkdir d:\TRAE-PROJETOS\bizantino-livros
  cd d:\TRAE-PROJETOS\bizantino-livros
  ```

- [ ] **Copiados arquivos relevantes**
  - LIVROS/SERIE-VIAJANTES-DO-TEMPO/
  - Relatórios de validação (VALIDACOES/)

- [ ] **Git inicializado e pushed**
  ```powershell
  git init
  git add .
  git commit -m "feat: Initial commit - Biblioteca de livros (6 publicados + 2 em QA)"
  git branch -M main
  git remote add origin https://github.com/SEU-USUARIO/bizantino-livros.git
  git push -u origin main
  ```

### bizantino-assets

- [ ] **Git LFS instalado**
  - Download: https://git-lfs.github.com/
  - Verificar: `git lfs version`

- [ ] **Repositório criado no GitHub**
  - Nome: `bizantino-assets`
  - Private: ✓
  - Descrição: `Assets visuais - personagens chromakey, capas, imagens internas`

- [ ] **Organizados localmente**
  ```powershell
  mkdir d:\TRAE-PROJETOS\bizantino-assets
  cd d:\TRAE-PROJETOS\bizantino-assets
  ```

- [ ] **Git LFS configurado**
  ```powershell
  git init
  git lfs install
  git lfs track "*.jpg"
  git lfs track "*.png"
  git lfs track "*.psd"
  git lfs track "*.ai"
  git add .gitattributes
  ```

- [ ] **Assets copiados**
  - ASSETS/PERSONAGENS-CHROMAKEY/
  - Capas dos livros
  - PROMPT-GEMINI arquivos

- [ ] **Pushed ao GitHub**
  ```powershell
  git add .
  git commit -m "feat: Initial commit - Assets visuais (personagens + capas)"
  git branch -M main
  git remote add origin https://github.com/SEU-USUARIO/bizantino-assets.git
  git push -u origin main
  ```

### bizantino-investidores

- [ ] **Repositório criado no GitHub**
  - Nome: `bizantino-investidores`
  - Private: ✓ ⚠️ **CRÍTICO - dados sensíveis**
  - Descrição: `Materiais para captação - pitch decks, financials, dados KDP`

- [ ] **Organizados localmente**
  ```powershell
  mkdir d:\TRAE-PROJETOS\bizantino-investidores
  cd d:\TRAE-PROJETOS\bizantino-investidores
  ```

- [ ] **Arquivos copiados**
  - PITCH-DECK-*.pdf
  - ONE-PAGER-*.md
  - MENSAGEM-INVESTIDORES-*.md
  - VALIDACAO-DADOS-PITCH.md
  - TALKING-POINTS-*.md

- [ ] **Pushed (com acesso restrito)**
  ```powershell
  git init
  git add .
  git commit -m "feat: Initial commit - Materiais para investidores"
  git branch -M main
  git remote add origin https://github.com/SEU-USUARIO/bizantino-investidores.git
  git push -u origin main
  ```

- [ ] **Acesso configurado**
  - Repo → Settings → Manage access
  - Apenas Owner + CFO (futuro)

### bizantino-inteligencia

- [ ] **Repositório criado no GitHub**
  - Nome: `bizantino-inteligencia`
  - Private: ✓
  - Descrição: `Market intelligence - research, keywords, analytics KDP`

- [ ] **Organizados localmente**
  ```powershell
  mkdir d:\TRAE-PROJETOS\bizantino-inteligencia
  cd d:\TRAE-PROJETOS\bizantino-inteligencia
  ```

- [ ] **Arquivos copiados**
  - INTELIGENCIA-DE-MERCADO/
  - Scripts de pesquisa
  - KDP data (Excel - verificar .gitignore!)

- [ ] **`.gitignore` específico criado**
  ```gitignore
  # Dados KDP sensíveis (downloads brutos)
  KDP_Orders-*.csv
  KDP_Sales-raw-*.xlsx
  personal-*.xlsx
  ```

- [ ] **Pushed ao GitHub**
  ```powershell
  git init
  git add .
  git commit -m "feat: Initial commit - Market intelligence e research"
  git branch -M main
  git remote add origin https://github.com/SEU-USUARIO/bizantino-inteligencia.git
  git push -u origin main
  ```

---

## 🔐 FASE 5: Segurança e Compliance (20-30 min)

### Proteção de Dados

- [ ] **Arquivo `.env` nunca commitado**
  - Verificar: `git status` não mostra .env
  - Se aparecer: adicionar ao .gitignore e `git rm --cached .env`

- [ ] **Credenciais removidas de arquivos**
  - Buscar: `grep -r "password" --include="*.py"`
  - Buscar: `grep -r "api_key" --include="*.py"`
  - Mover para `.env`

- [ ] **`.env.example` atualizado**
  - Template com variáveis sem valores reais

### Auditoria

- [ ] **Histórico de commits revisado**
  ```powershell
  git log --all --oneline
  ```
  - Verificar mensagens descritivas
  - Sem commits com credenciais

- [ ] **Tamanho dos repos verificado**
  - Repos grandes (> 1 GB) usar Git LFS
  - GitHub: Repo → Insights → Network

### Backup

- [ ] **Backup local mantido**
  - D:\TRAE-PROJETOS\livro1\BIZANTINO (ativo)
  - C:\Users\xberi\Documents\trae_projects\154 (backup antigo)

- [ ] **Backup cloud configurado (opcional)**
  - Google Drive / OneDrive / Dropbox
  - Sincronização automática da pasta local

---

## 📊 FASE 6: Documentação e Testes (10-15 min)

### Documentação

- [ ] **README.md atualizado em cada repo**
  - bizantino-core/README.md
  - bizantino-livros/README.md
  - bizantino-assets/README.md
  - bizantino-investidores/README.md
  - bizantino-inteligencia/README.md

- [ ] **CHANGELOG.md criado (bizantino-core)**
  - Formato: https://keepachangelog.com/
  - Versão 1.0.0 documentada

- [ ] **CONTRIBUTING.md criado (opcional)**
  - Guia para colaboradores futuros

### Testes

- [ ] **Clonar em outra pasta (teste)**
  ```powershell
  cd C:\temp
  git clone https://github.com/SEU-USUARIO/bizantino-core.git
  cd bizantino-core
  # Verificar arquivos
  ```

- [ ] **Fazer mudança de teste**
  ```powershell
  echo "# Teste" >> TEST.md
  git add TEST.md
  git commit -m "test: Teste de workflow"
  git push origin main
  ```

- [ ] **Verificar no GitHub web**
  - Mudança aparece imediatamente
  - Commit visível no histórico

- [ ] **Deletar pasta de teste**
  ```powershell
  cd ..
  rm -r bizantino-core
  ```

---

## 🚀 FASE 7: Próximos Passos e Scaling (Contínuo)

### Workflow Estabelecido

- [ ] **Workflow diário documentado**
  - Pull → Edit → Add → Commit → Push
  - Convenção de commits seguida

- [ ] **Branches para features (opcional)**
  ```powershell
  git checkout -b feature/livro-09
  # fazer mudanças
  git commit -m "feat(livro-09): Adiciona manuscrito"
  git push origin feature/livro-09
  # Criar Pull Request no GitHub
  ```

### Automação Futura

- [ ] **CI/CD planejado (GitHub Actions)**
  - .github/workflows/test.yml
  - Rodar testes automaticamente

- [ ] **Backup automatizado**
  - Script PowerShell agendado
  - Task Scheduler (Windows)

### Colaboração

- [ ] **Equipe futura preparada**
  - Permissões por repo definidas
  - Onboarding documentado

- [ ] **Issues e Projects habilitados**
  - GitHub Issues para tarefas
  - GitHub Projects para roadmap

---

## ✅ VERIFICAÇÃO FINAL

### Checklist de Validação

- [ ] **5 repositórios criados e acessíveis**
  1. bizantino-core ✓
  2. bizantino-livros ✓
  3. bizantino-assets ✓
  4. bizantino-investidores ✓
  5. bizantino-inteligencia ✓

- [ ] **Todos repositórios são PRIVATE**
  - Verificar: Repo → Settings → Danger Zone

- [ ] **Branch protection em main (bizantino-core)**
  - Settings → Branches → Verify rules

- [ ] **Two-Factor Authentication ativo**
  - GitHub → Settings → Password and authentication

- [ ] **Personal Access Token salvo seguramente**
  - 1Password, Bitwarden, ou arquivo criptografado

- [ ] **`.env` nunca commitado em nenhum repo**
  - Buscar: `git log --all --full-history -- .env`
  - Resultado: vazio

- [ ] **Backup local mantido (independente do GitHub)**
  - Verificar: D:\TRAE-PROJETOS\livro1\BIZANTINO

- [ ] **Documentação completa lida**
  - GUIA-GITHUB-VERSIONAMENTO.md ✓
  - GITHUB-RESUMO-EXECUTIVO.md ✓

---

## 📈 MÉTRICAS DE SUCESSO

| Métrica | Meta | Status |
|---------|------|--------|
| Repositórios criados | 5 | [ ] |
| Commits iniciais | 5 | [ ] |
| Repos privados | 5/5 | [ ] |
| 2FA habilitado | Sim | [ ] |
| Branch protection | Sim (core) | [ ] |
| Backup local | Sim | [ ] |
| Testes bem-sucedidos | Sim | [ ] |

---

## 🎓 PRÓXIMOS APRENDIZADOS

- [ ] **Git intermediate**
  - Branches e merges
  - Rebasing
  - Cherry-picking

- [ ] **GitHub Actions (CI/CD)**
  - Testes automatizados
  - Deploy automatizado

- [ ] **Git LFS avançado**
  - Migration de arquivos grandes
  - Cleanup de histórico

- [ ] **Monorepo vs Multi-repo**
  - Avaliar estratégia para escala

---

## 📞 SUPORTE

Se travou em alguma etapa:

1. Consultar **GUIA-GITHUB-VERSIONAMENTO.md** (seção Troubleshooting)
2. Consultar **GITHUB-RESUMO-EXECUTIVO.md** (seção Troubleshooting Rápido)
3. Buscar erro no Google: `site:stackoverflow.com "mensagem do erro"`
4. Pedir ajuda ao Claude AI (assistente do projeto)

---

## 📊 TEMPO ESTIMADO TOTAL

| Fase | Tempo | Acumulado |
|------|-------|-----------|
| 1. Preparação | 15-20 min | 15-20 min |
| 2. Setup Local | 20-30 min | 35-50 min |
| 3. bizantino-core | 15-20 min | 50-70 min |
| 4. Repos Adicionais | 30-45 min | 80-115 min |
| 5. Segurança | 20-30 min | 100-145 min |
| 6. Documentação/Testes | 10-15 min | 110-160 min |
| 7. Próximos Passos | 10 min | 120-170 min |

**TOTAL**: 2-3 horas (com atenção aos detalhes)

---

## 🏆 CONQUISTAS

Ao completar todas as fases acima, você terá:

✅ **Controle empresarial** de versionamento  
✅ **5 repositórios privados** organizados  
✅ **Backup cloud** automático via GitHub  
✅ **Segurança** de nível enterprise (2FA, branch protection)  
✅ **Preparação para escalabilidade** (equipe futura)  
✅ **Due diligence pronta** para investidores  
✅ **Histórico auditável** de todas mudanças  
✅ **Proteção contra perda de dados** (multi-camada)  

**PARABÉNS!** 🎉

Você estabeleceu uma infraestrutura de versionamento profissional que suporta:
- Crescimento de 1 → 10 contas KDP
- Team scaling de 1 → 10+ colaboradores
- Compliance regulatório
- Transparência para stakeholders

---

**Versão**: 1.0  
**Última atualização**: 2026-01-10  
**Próxima revisão**: Após conclusão do setup  

---

## 📝 NOTAS PESSOAIS

Use este espaço para anotar:
- Dificuldades encontradas
- Soluções improvisadas
- Melhorias a fazer
- Lembretes para próxima vez

---

**Marcar como concluído quando 100% dos itens estiverem com [x]**
