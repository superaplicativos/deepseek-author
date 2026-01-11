# README - Sites do Projeto Bizantino

## Visão Geral

Dois sites HTML profissionais foram criados para o Projeto Bizantino:

1. **`site-clientes.html`** - Site para pais comprando livros infantis
2. **`site-investidores.html`** - Site para captação de investimento

Ambos são **standalone** (HTML, CSS e JavaScript inline), **responsivos** e prontos para deploy imediato.

---

## Site 1: Clientes (site-clientes.html)

### Objetivo
Vender livros da série "Turma da Aventura: Viajantes do Tempo" para pais de crianças de 8-12 anos.

### Seções Principais
1. **Hero** - Chamada principal com badges (6 livros, 4 idiomas, 10 países, 331 famílias)
2. **Por Que Pais Amam** - 6 cards com benefícios (educacional, qualidade, valores, multilíngue, sem violência, estimula leitura)
3. **Conheça os Livros** - Catálogo com 6 livros (capas, sinopses, botões compra Amazon)
4. **Conheça os Personagens** - Grid com 7 personagens fixos
5. **Depoimentos** - Métricas reais (331 vendas, 24.823 KENP) + 3 quotes
6. **FAQ** - 6 perguntas comuns (idade, educacional, violência, idiomas, onde comprar, ordem)
7. **Sobre** - História da série
8. **Footer** - Links Amazon por país, newsletter, copyright

### Como Personalizar

#### 1. **Adicionar ASINs da Amazon**
Procure por `[ASIN-LIVRO-X]` e substitua pelos ASINs reais:

```html
<!-- ANTES: -->
<a href="https://amazon.com/dp/[ASIN-LIVRO-1]" class="btn btn-primary">

<!-- DEPOIS (exemplo): -->
<a href="https://amazon.com/dp/B09XYZ1234" class="btn btn-primary">
```

**Onde encontrar ASINs:**
- Vá para a página do livro na Amazon
- ASIN está nos detalhes do produto (exemplo: B09XYZ1234)

**Repita para todos os 6 livros.**

#### 2. **Adicionar Imagens Reais dos Personagens**
Atualmente há placeholders. Para usar imagens reais:

```html
<!-- Hero - Substituir placeholder pela imagem da turma -->
<div class="hero-image" style="background: rgba(255,255,255,0.2);">
    <!-- SUBSTITUIR POR: -->
    <img src="ASSETS/PERSONAGENS-CHROMAKEY/TURMATODA.fw.png" alt="Turma da Aventura" style="max-width: 100%; border-radius: 12px;">
</div>
```

Para personagens individuais, procure por `<div class="character-img">` e adicione imagens:

```html
<!-- ANTES: -->
<div class="character-img">👦</div>

<!-- DEPOIS: -->
<div class="character-img">
    <img src="ASSETS/PERSONAGENS-CHROMAKEY/WILL.jpg" alt="Will" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;">
</div>
```

**Imagens disponíveis:**
- `ASSETS/PERSONAGENS-CHROMAKEY/WILL.jpg`
- `ASSETS/PERSONAGENS-CHROMAKEY/MIA.jpg`
- `ASSETS/PERSONAGENS-CHROMAKEY/LEO.jpg`
- `ASSETS/PERSONAGENS-CHROMAKEY/SOPHIE.jpg`
- `ASSETS/PERSONAGENS-CHROMAKEY/MAX.jpg`
- `ASSETS/PERSONAGENS-CHROMAKEY/JIMMY.jpg`
- `ASSETS/PERSONAGENS-CHROMAKEY/GRIMSTONE.jpg`

#### 3. **Adicionar Capas dos Livros**
Procure por `<div class="book-cover">` e adicione imagens reais:

```html
<!-- ANTES: -->
<div class="book-cover">📘 Capa: Livro 1</div>

<!-- DEPOIS (se você tiver a capa): -->
<div class="book-cover">
    <img src="LIVROS/LIVRO-01/PT/capa.jpg" alt="Capa Livro 1" style="width: 100%; height: 100%; object-fit: cover;">
</div>
```

**Nota:** Apenas o Livro 7 tem capas no projeto atual (`LIVROS/LIVRO-07-CONSTANTINOPLA/IMAGENS/CAPA-EBOOK.png`).

#### 4. **Configurar Newsletter**
O botão "Inscrever" está com placeholder. Para ativar:

**Opção A: Usar FormSpree (gratuito, sem backend)**
1. Vá para https://formspree.io
2. Crie conta e form gratuito
3. Substitua no script:

```javascript
// ANTES:
alert('Obrigado! Em breve você receberá novidades sobre novos livros.\n\n(Integração real de newsletter pendente)');

// DEPOIS:
fetch('https://formspree.io/f/YOUR_FORM_ID', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: email })
}).then(() => {
    alert('Obrigado! Você foi inscrito com sucesso.');
    document.querySelector('.newsletter input').value = '';
});
```

**Opção B: Usar Mailchimp, ConvertKit, etc.**
Substitua o formulário pelos códigos de embed desses serviços.

#### 5. **Ativar Google Analytics**
Descomente e adicione seu tracking ID:

```javascript
// Procure no final do HTML:
/*
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-XXXXXXXXXX'); // Substitua pelo seu tracking ID
*/

// DESCOMENTE e substitua G-XXXXXXXXXX pelo seu ID real
```

---

## Site 2: Investidores (site-investidores.html)

### Objetivo
Atrair investimento mostrando dados reais, comparação com Spines ($16M funding), e sistemas automatizados.

### Seções Principais
1. **Hero** - Headline forte "Clone da Spines por 200x menos" + stats cards
2. **Por Que Investir** - 6 razões principais
3. **Tração e Dados** - Dashboard com métricas reais (331 vendas, $811 receita)
4. **Nós vs Spines** - Tabela comparativa lado a lado
5. **Sistemas e Tecnologia** - 6 sistemas automatizados detalhados
6. **Escalabilidade** - Tabela de projeção (1, 5, 10 contas KDP)
7. **Opções de Investimento** - 3 cards (Seed, Growth, Revenue Share)
8. **Materiais para Download** - Grid com PDFs e Excel
9. **Timeline** - Desenvolvimento, validação, escala, crescimento
10. **Próximos Passos** - 3 passos para investir + formulário contato
11. **Footer** - Links e dados principais

### Como Personalizar

#### 1. **Configurar Formulário de Contato**
O formulário usa FormSpree (placeholder). Para ativar:

1. Vá para https://formspree.io
2. Crie conta gratuita
3. Crie um novo form
4. Copie o form ID (exemplo: `xayvpqwe`)
5. Substitua no HTML:

```html
<!-- ANTES: -->
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">

<!-- DEPOIS: -->
<form action="https://formspree.io/f/xayvpqwe" method="POST">
```

Quando alguém submeter o formulário, você receberá email notificação.

**Alternativa:** Use Google Forms e embuta no site.

#### 2. **Atualizar Links de Download**
Verifique se todos os caminhos de arquivos estão corretos:

```html
<!-- Exemplo: -->
<a href="PITCH-DECK-TECH-AUTOMATION.pdf" class="btn btn-secondary" download>Download PDF</a>
```

**Arquivos disponíveis para download:**
- `ONE-PAGER-INVESTIDORES-SPINES.md`
- `PITCH-DECK-TECH-AUTOMATION.pdf`
- `PITCH-DECK-TURMA-DA-AVENTURA.pdf`
- `TURMA_DA_AVENTURA_Investment_Pitch_Deck_2026.pdf`
- `MENSAGEM-INVESTIDORES-SPINES-CLONE.md`
- `VALIDACAO-DADOS-PITCH.md`
- `INTELIGENCIA-DE-MERCADO/KDP_Orders-*.xlsx`
- `INTELIGENCIA-DE-MERCADO/KDP_Royalties_Estimator-*.xlsx`

**Se hospedar em servidor web:** Coloque todos esses arquivos na mesma pasta que o HTML.

#### 3. **Atualizar Email de Contato**
Procure por `investidores@projetobizantino.com` e substitua pelo email real:

```html
<!-- Exemplo: -->
<p>Email: investidores@projetobizantino.com</p>

<!-- Substitua por: -->
<p>Email: seuemail@seudominio.com</p>
```

#### 4. **Ajustar Métricas (Opcional)**
As métricas estão com dados reais de 26 meses. Se quiser atualizar:

- Procure por valores como "331", "24,823", "$811", etc.
- Atualize com dados mais recentes do KDP

---

## Hospedagem

### Opção 1: Netlify (Recomendado - Gratuito)

**Vantagens:** Gratuito, fácil, domínio customizado, SSL automático, deploy em 2 minutos

**Passos:**
1. Vá para https://netlify.com
2. Crie conta gratuita
3. Clique "Add new site" → "Deploy manually"
4. Arraste a pasta com os arquivos HTML
5. Pronto! Site estará em `seu-nome.netlify.app`

**Domínio customizado:**
1. Compre domínio (ex: `turmadaaventura.com`)
2. No Netlify, vá em "Domain settings"
3. Adicione domínio customizado
4. Configure DNS conforme instruções

### Opção 2: GitHub Pages (Gratuito)

**Vantagens:** Gratuito, integrado com Git, versionamento automático

**Passos:**
1. Crie repositório GitHub
2. Faça upload dos arquivos HTML
3. Vá em Settings → Pages
4. Selecione branch "main" e pasta raiz
5. Salve - site estará em `usuario.github.io/repo`

### Opção 3: Vercel (Gratuito)

**Vantagens:** Gratuito, deploy automático via Git, performance excelente

**Passos:**
1. Vá para https://vercel.com
2. Conecte com GitHub
3. Importe repositório
4. Deploy automático

### Opção 4: Amazon S3 + CloudFront (Profissional)

**Vantagens:** Altamente escalável, baixo custo (~$1-5/mês), CDN global

**Passos:**
1. Crie bucket S3
2. Habilite "Static website hosting"
3. Faça upload dos arquivos
4. Configure CloudFront para CDN
5. Aponte domínio para CloudFront

---

## Estrutura de Arquivos para Hospedagem

Quando fizer upload para servidor, organize assim:

```
/
├── site-clientes.html (renomeie para index.html se for site principal)
├── site-investidores.html (ou investors.html)
├── ASSETS/
│   └── PERSONAGENS-CHROMAKEY/
│       ├── WILL.jpg
│       ├── MIA.jpg
│       ├── LEO.jpg
│       ├── SOPHIE.jpg
│       ├── MAX.jpg
│       ├── JIMMY.jpg
│       ├── GRIMSTONE.jpg
│       └── TURMATODA.fw.png
├── LIVROS/
│   └── LIVRO-07-CONSTANTINOPLA/
│       └── IMAGENS/
│           └── CAPA-EBOOK.png
├── PITCH-DECK-TECH-AUTOMATION.pdf
├── PITCH-DECK-TURMA-DA-AVENTURA.pdf
├── TURMA_DA_AVENTURA_Investment_Pitch_Deck_2026.pdf
├── ONE-PAGER-INVESTIDORES-SPINES.md
├── MENSAGEM-INVESTIDORES-SPINES-CLONE.md
├── VALIDACAO-DADOS-PITCH.md
└── INTELIGENCIA-DE-MERCADO/
    ├── KDP_Orders-db6f12e2-0887-4442-a911-009dfe2e395c.xlsx
    └── KDP_Royalties_Estimator-0c6d1550-2d07-46e7-828c-7fa60c66a2e5.xlsx
```

---

## Domínios Sugeridos

### Site de Clientes:
- `turmadaaventura.com` (recomendado)
- `aventuratempo.com`
- `viajantesdotempo.com`
- `timemachine adventures.com` (para mercado internacional)

### Site de Investidores:
- `bizantino.invest`
- `investors.turmadaaventura.com` (subdomínio)
- `projetobizantino.com`

**Registradores recomendados:**
- Namecheap (barato, fácil)
- Google Domains (simples, confiável)
- Cloudflare (com CDN gratuito)

---

## Otimizações Recomendadas

### 1. Imagens

**Compressão:**
- Use TinyPNG (https://tinypng.com) para comprimir JPG/PNG
- Reduza tamanho dos arquivos em 50-70% sem perda visível

**Formatos modernos:**
```html
<!-- Substitua PNG por WebP para menor tamanho: -->
<img src="imagem.webp" alt="...">

<!-- Fallback para navegadores antigos: -->
<picture>
    <source srcset="imagem.webp" type="image/webp">
    <img src="imagem.jpg" alt="...">
</picture>
```

**Lazy loading:**
```html
<img src="imagem.jpg" loading="lazy" alt="...">
```

### 2. Performance

**Minificar HTML/CSS:**
- Use https://minifier.org
- Reduza tamanho em ~20-30%

**CDN para assets:**
- Hospede imagens pesadas em Cloudinary (gratuito até 25 GB)
- Melhora velocidade de carregamento

### 3. SEO

**Adicione meta tags personalizadas:**
```html
<meta name="description" content="Sua descrição aqui">
<meta name="keywords" content="livros infantis, aventura, educacional">
```

**Open Graph (compartilhamento social):**
```html
<meta property="og:image" content="URL-DA-IMAGEM-PRINCIPAL">
<meta property="og:title" content="Turma da Aventura">
<meta property="og:description" content="Aventuras épicas para crianças">
```

**Sitemap:**
Crie `sitemap.xml`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://seudominio.com/site-clientes.html</loc>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://seudominio.com/site-investidores.html</loc>
    <priority>0.8</priority>
  </url>
</urlset>
```

### 4. Analytics

**Google Analytics 4:**
1. Crie conta em https://analytics.google.com
2. Crie propriedade
3. Copie Measurement ID (G-XXXXXXXXXX)
4. Adicione antes de `</head>`:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**Facebook Pixel (opcional para ads):**
Se quiser fazer anúncios no Facebook/Instagram:
```html
<!-- Facebook Pixel Code -->
<script>
  !function(f,b,e,v,n,t,s){...}
  fbq('init', 'YOUR_PIXEL_ID');
  fbq('track', 'PageView');
</script>
```

---

## Testes Pré-Lançamento

### Checklist Site de Clientes:
- [ ] Todos os 6 botões "Comprar na Amazon" têm ASINs corretos
- [ ] Imagens dos personagens carregam corretamente
- [ ] Links do footer funcionam (Amazon Brasil, USA, Alemanha, etc.)
- [ ] Newsletter (se ativada) está funcionando
- [ ] FAQ responde perguntas relevantes
- [ ] Site é responsivo em mobile (testar no celular)
- [ ] Velocidade de carregamento < 3 segundos (teste em PageSpeed Insights)

### Checklist Site de Investidores:
- [ ] Formulário de contato enviando emails corretamente
- [ ] Todos os links de download funcionam
- [ ] PDFs e Excel estão hospedados e acessíveis
- [ ] Email de contato está correto
- [ ] Tabela "Nós vs Spines" exibe corretamente
- [ ] Métricas estão atualizadas
- [ ] Site é responsivo em desktop/tablet

### Ferramentas de Teste:
- **PageSpeed Insights** - https://pagespeed.web.dev (velocidade)
- **Mobile-Friendly Test** - https://search.google.com/test/mobile-friendly
- **GTmetrix** - https://gtmetrix.com (performance)
- **BrowserStack** - Testar em múltiplos navegadores/dispositivos

---

## Segurança

### SSL/HTTPS
Netlify, Vercel e GitHub Pages fornecem SSL gratuito automaticamente.

Se usar servidor próprio:
- Use Let's Encrypt (gratuito)
- Configure redirecionamento HTTP → HTTPS

### Formulários
FormSpree tem proteção anti-spam integrada.

Para proteção extra, adicione reCAPTCHA:
```html
<script src="https://www.google.com/recaptcha/api.js" async defer></script>
<div class="g-recaptcha" data-sitekey="YOUR_SITE_KEY"></div>
```

---

## Suporte e Manutenção

### Atualizar Conteúdo

**Adicionar novo livro:**
1. Abra `site-clientes.html`
2. Copie uma das divs `.book-card`
3. Cole e edite: título, sinopse, ASIN, período histórico
4. Salve e faça re-deploy

**Atualizar métricas:**
1. Abra `site-investidores.html`
2. Procure por valores numéricos (331, 24823, $811, etc.)
3. Atualize com dados mais recentes
4. Salve e faça re-deploy

### Backup
Sempre mantenha backup dos arquivos:
- GitHub (versionamento automático)
- Google Drive / Dropbox
- Local (pasta ARQUIVADOS/)

---

## Perguntas Frequentes

**Q: Preciso de servidor PHP/Node.js?**
A: Não. Os sites são 100% estáticos (HTML/CSS/JS). Qualquer hospedagem de arquivos estáticos funciona.

**Q: Posso editar os sites?**
A: Sim! Todo código é seu. Edite livremente no VS Code, Notepad++, ou qualquer editor.

**Q: Como adiciono mais idiomas no site de clientes?**
A: Pode criar páginas separadas (ex: `site-clientes-en.html`) ou usar tradutor automático no navegador. Para solução profissional, considere i18n frameworks.

**Q: Os sites funcionam offline?**
A: Sim, são standalone. Baixe e abra em qualquer navegador.

**Q: Preciso pagar por FormSpree?**
A: Plano gratuito permite 50 submissões/mês. Suficiente para começar.

**Q: Como sei se alguém está visitando meu site?**
A: Configure Google Analytics (instruções acima). Mostra visitantes, páginas vistas, origens de tráfego, etc.

---

## Recursos Adicionais

### Documentação Técnica:
- **HTML5:** https://developer.mozilla.org/en-US/docs/Web/HTML
- **CSS3:** https://developer.mozilla.org/en-US/docs/Web/CSS
- **Responsivo:** https://web.dev/responsive-web-design-basics/

### Ferramentas Úteis:
- **Canva:** Criar banners/imagens (https://canva.com)
- **Unsplash:** Fotos gratuitas (https://unsplash.com)
- **Font Awesome:** Ícones (https://fontawesome.com)
- **Google Fonts:** Fontes customizadas (https://fonts.google.com)

### Aprendizado:
- **W3Schools:** Tutoriais HTML/CSS (https://w3schools.com)
- **freeCodeCamp:** Curso completo web dev (https://freecodecamp.org)

---

## Contato e Suporte

Se tiver dúvidas sobre os sites:

1. **Documentação do Projeto:** `MAPEAMENTO_COMPLETO_PROJETO_BIZANTINO.txt`
2. **Diretrizes Visuais:** `DOCS/DIRETRIZES_VISUAIS_IDENTIDADE.md`
3. **Diretrizes de Qualidade:** `DOCS/DIRETRIZES_QUALIDADE_SERIE.md`

---

## Conclusão

Os sites estão prontos para uso imediato. Basta:

1. **Personalizar ASINs da Amazon** (site clientes)
2. **Configurar formulário FormSpree** (site investidores)
3. **Fazer upload para Netlify/Vercel/GitHub Pages**
4. **Compartilhar URLs!**

Boa sorte com os sites! 🚀

---

**Versão:** 1.0
**Data:** 2026-01-10
**Criado por:** Claude Code (Anthropic)
