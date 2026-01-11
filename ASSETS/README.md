# 🎨 ASSETS - Recursos Visuais da Série

Esta pasta contém todos os assets visuais da série "Turma da Aventura: Viajantes do Tempo".

## Estrutura

```
ASSETS/
├── PERSONAGENS-CHROMAKEY/    # Referências dos personagens (NUNCA MODIFICAR)
└── CAPAS/                     # Capas dos livros por idioma
```

## PERSONAGENS-CHROMAKEY/

**⚠️ CRÍTICO: NUNCA MODIFICAR ESTES ARQUIVOS!**

Estes são os character references oficiais usados para:
- Manter consistência visual em TODAS as ilustrações
- Gerar prompts para IA (Gemini, Midjourney, etc.)
- Garantir identidade visual da série

### Personagens Fixos:

1. **WILL.jpg** - Will (Wilian), 9 anos, líder
   - Roupas: Camiseta azul escuro, jeans, tênis
   - Props: Smartphone com Íris (IA holográfica) - SEMPRE visível
   - Cabelo: Castanho claro curto e liso

2. **MIA.jpg** - Mia, 8 anos, inventora
   - Roupas: Camiseta roxa, shorts jeans, tênis roxos
   - Props: Cinto de ferramentas (chave inglesa, trena) - SEMPRE visível
   - Cabelo: Ruivo em dois coques laterais

3. **LEO.jpg** - Leo, 10 anos, protetor atlético
   - Roupas: Camiseta verde escuro, bermuda cáqui
   - Props: Mochila de aventura
   - Cabelo: Loiro bagunçado curto

4. **SOPHIE.jpg** - Sophie, 8 anos, detetive
   - Roupas: Vestido amarelo com estampas de lupa
   - Props: Caderninho de anotações - SEMPRE nas mãos
   - Cabelo: Castanho escuro liso em rabo lateral

5. **MAX.jpg** - Max, 7 anos, alívio cômico
   - Roupas: Camiseta vermelha com estampa de animais, calça bege
   - Props: Geralmente segurando pelúcia ou criaturinha
   - Cabelo: Castanho claro em corte cogumelo

6. **JIMMY.jpg** - Jimmy Hendrix, Border Collie
   - **IMPORTANTE:** Marrom e branco (NÃO caramelo!)
   - Olhos expressivos e inteligentes
   - Pelagem densa, orelhas alertas

7. **GRIMSTONE.jpg** - Dr. Grimstone, vilão excêntrico
   - Objetivo: Acabar com imaginação das crianças
   - Tom: Cômico, NUNCA assustador
   - Sidekick: Morty (corvo preto reclamão)

8. **TURMATODA.fw.png** - Imagem composta do time completo

## CAPAS/

Organização das capas por livro e idioma:

```
CAPAS/
├── LIVRO-01/
│   ├── PT/
│   ├── EN/
│   ├── ES/
│   └── DE/
├── LIVRO-02/
│   └── ...
```

### Especificações Amazon KDP

**Dimensões:**
- Paperback: 6" x 9" (15.24 cm x 22.86 cm)
- eBook: Mínimo 1600 x 2400 pixels (ideal: 2560 x 1600)

**Formato:**
- Paperback: PDF de alta resolução (300 DPI)
- eBook: JPG ou PNG

**Cores:**
- RGB para eBook
- CMYK para paperback

### Diretrizes Visuais

**Veja:** `DOCS/DIRETRIZES_VISUAIS_IDENTIDADE.md` para:
- Templates de prompts Gemini
- Especificações completas de design
- Consistência visual obrigatória
- Exemplos de composição

## Gerando Novas Ilustrações

### 1. Usando Gemini (Google AI Studio)

Consulte `LIVROS/LIVRO-XX/PROMPT_GEMINI_*` para exemplos de prompts.

**Template base:**
```
Criar ilustração estilo Pixar semi-realista de alta qualidade para livro infantil.

Personagens (usar referências):
- Will: [descrição completa com roupas e props]
- Mia: [descrição completa com roupas e props]
[...]

Cena: [descrição da cena específica]

Estilo artístico:
- Qualidade Pixar semi-realista
- Cores vibrantes e ricas
- Iluminação cinematográfica
- Profundidade de campo suave
- Rostos expressivos e vivos
```

### 2. Mantendo Consistência

**✅ SEMPRE:**
- Usar descrições EXATAS dos personagens das referências
- Incluir props característicos de cada personagem
- Manter paleta de cores oficial
- Seguir estilo Spielberg (maravilhamento, aventura, coração)

**❌ NUNCA:**
- Mudar roupas ou aparência dos personagens
- Omitir props característicos (smartphone do Will, cinto da Mia, etc.)
- Fazer Jimmy caramelo (é marrom e branco!)
- Tornar Dr. Grimstone assustador (sempre cômico)

## Workflows

### Criar Capa de Novo Livro

1. Pesquisar capas bestsellers Amazon (5 mercados)
2. Criar conceito alinhado com identidade visual
3. Gerar prompt Gemini baseado em templates
4. Iterar até aprovação
5. Ajustar para specs KDP
6. Criar versões para 4 idiomas (PT/EN/ES/DE)

### Gerar Ilustrações Internas

1. Usar `SCRIPTS/6-GERACAO-IMAGENS/gerar_imagens_livro6.py`
2. Revisar prompts gerados
3. Executar no Gemini/Midjourney
4. Validar consistência com referências
5. Inserir em DOCX via scripts

---

**Última atualização:** 2026-01-02
