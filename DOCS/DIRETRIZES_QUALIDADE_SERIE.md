# DIRETRIZES DE QUALIDADE DA SÉRIE
## Turma da Aventura - Todas as Séries

**DOCUMENTO OFICIAL DE PADRÕES DE QUALIDADE**
**Versão:** 2.0 (Atualizado após reorganização)
**Data:** 2026-01-10
**Status:** OBRIGATÓRIO para todos os novos livros de todas as séries

> **⚠️ NOTA DE REORGANIZAÇÃO (2026-01-10):**
> O projeto agora possui múltiplas séries temáticas. Este documento contém padrões GERAIS de qualidade.
> Para diretrizes específicas de cada série, consulte `DIRETRIZES/SERIE-[NOME].txt`
>
> **Séries Ativas:**
> - Viajantes do Tempo (Livros 1-6, publicados)
> - Lugares Incríveis (Livros 1-3, sendo Livro 1 no Google Drive e Livros 2-3 em QA)
> - Invenções, Mistérios, Ciência (em planejamento)

---

## 📋 ÍNDICE

1. [Propósito deste Documento](#propósito)
2. [Checklist Obrigatória de Qualidade](#checklist-obrigatória)
3. [Padrões de Extensão e Estrutura](#padrões-de-extensão-e-estrutura)
4. [Personagens Fixos - Especificações Visuais Completas](#personagens-fixos)
5. [Dr. Grimstone - Diretrizes de Uso](#dr-grimstone)
6. [Estilo Narrativo Spielberg](#estilo-spielberg)
7. [Elementos Obrigatórios por Capítulo](#elementos-por-capítulo)
8. [Padrões de Formatação](#padrões-de-formatação)
9. [Adequação para Tradução Multilíngue](#adequação-tradução)
10. [Validação e QA Antes de Publicar](#validação-qa)

---

## 🎯 PROPÓSITO

Este documento define os **padrões de qualidade obrigatórios** para todos os livros da série "Turma da Aventura: Viajantes do Tempo" a partir do Livro 9.

**Objetivo:** Garantir que cada novo livro:
- Mantenha consistência visual e narrativa com livros anteriores
- Atinja os padrões de qualidade que triplicaram vendas nos 5 mercados
- Seja adequado para publicação simultânea em 4 idiomas (PT, EN, DE, ES)
- Passe no QA sem necessidade de revisões críticas

**Status dos Livros 1-8:**
- Livros 1-6: Publicados, estabeleceram padrões
- Livros 7-8: Escritos, introduzem vilões novos (sem Dr. Grimstone) - APROVADO
- Livros 9+: DEVEM seguir este documento rigorosamente

---

## ✅ CHECKLIST OBRIGATÓRIA DE QUALIDADE

### ANTES DE COMEÇAR A ESCREVER

- [ ] **Pesquisa de mercado realizada** nos 5 mercados (USA, Brasil, Alemanha, UK, Espanha)
- [ ] **Tema selecionado** alinhado com tendências de Amazon bestsellers
- [ ] **Período histórico/setting** verificado para precisão cultural
- [ ] **Outline de 5 atos** criado com percentuais corretos
- [ ] **Subplot de Dr. Grimstone** planejado (2-3 cenas cômicas)
- [ ] **Momento de cada personagem** identificado no outline

### DURANTE A ESCRITA

- [ ] **Capítulo 1** inclui descrições visuais completas de TODOS os personagens
- [ ] **Idades mencionadas** naturalmente no início
- [ ] **Props característicos** aparecem pelo menos 2x por livro (cinto de Mia, mochila de Leo, etc.)
- [ ] **Dr. Grimstone aparece** em 2-3 capítulos (geralmente Cap 3-4 e Cap 6-7)
- [ ] **Morty (corvo)** reclama e faz comentários sarcásticos
- [ ] **Catchphrase de Grimstone** usada pelo menos 1x
- [ ] **Íris AI** mencionada regularmente (Will usando smartphone)
- [ ] **Jimmy Hendrix** participa ativamente (não só acompanha)
- [ ] **Todos os 6 personagens** têm momento significativo
- [ ] **Cliffhangers** no final de cada capítulo (especialmente Cap 2, 4, 6, 8)
- [ ] **Vocabulário** adequado para 8-12 anos
- [ ] **Linguagem** clara e culturalmente neutra (sem gírias regionais)

### APÓS COMPLETAR O MANUSCRITO

- [ ] **Extensão:** 35.000-50.000 palavras (mínimo 35k)
- [ ] **Capítulos:** 10-15 capítulos de 3.000-4.000 palavras cada
- [ ] **Estrutura 5 atos:** Verificar percentuais (15-20%, 30-35%, 20-25%, 15-20%, 10-15%)
- [ ] **Contagem de palavras:** Conferir com `wc -w manuscrito.txt`
- [ ] **Dr. Grimstone:** Buscar por "Grimstone" - deve aparecer
- [ ] **Morty:** Buscar por "Morty" - deve aparecer
- [ ] **Personagens:** Buscar "Will", "Mia", "Leo", "Sophie", "Max", "Jimmy" - distribuição balanceada
- [ ] **Íris:** Buscar "Íris" ou "smartphone" - múltiplas ocorrências
- [ ] **Precisão histórica:** Verificar datas, nomes, eventos
- [ ] **Anachronismos:** Apenas se fizerem parte do plot de viagem no tempo
- [ ] **Gerar relatórios de validação** (6 documentos MD)

### ANTES DE PUBLICAR

- [ ] **DOCX gerado** com formatação correta
- [ ] **100+ páginas** verificadas no Google Docs
- [ ] **Capas criadas** para cada mercado
- [ ] **Tradução PT→EN, DE, ES** concluída
- [ ] **QA com GPT-5** realizado nas 4 línguas
- [ ] **Revisão humana final** aprovada
- [ ] **Metadados otimizados** para cada Amazon regional
- [ ] **Keywords pesquisadas** por idioma/mercado

---

## 📏 PADRÕES DE EXTENSÃO E ESTRUTURA

### EXTENSÃO MÍNIMA OBRIGATÓRIA

| Métrica | Mínimo | Ideal | Máximo |
|---------|--------|-------|--------|
| **Palavras Totais** | 35.000 | 40.000 | 50.000 |
| **Capítulos** | 10 | 12 | 15 |
| **Palavras/Capítulo** | 3.000 | 3.500 | 4.000 |
| **Páginas DOCX** | 100 | 120 | 150 |

**Como verificar:**
```bash
# Contar palavras do manuscrito
wc -w manuscrito.txt

# Contar capítulos
grep -c "CAPÍTULO" manuscrito.txt
```

**Se estiver abaixo do mínimo:**
- ❌ NÃO publicar
- 🔧 Adicionar subplots, expandir descrições sensoriais, desenvolver cenas emocionais
- 🎯 Qualidade sobre quantidade - sem enchimento, mas sem pressa

### ESTRUTURA DE 5 ATOS (OBRIGATÓRIA)

Cada livro DEVE seguir esta estrutura:

#### **ATO 1: INTRODUÇÃO (15-20% do total)**
- **Capítulos:** Geralmente 1-2
- **Elementos obrigatórios:**
  - Hook imediato (primeiras 3 páginas)
  - Apresentação do problema/mistério
  - Descrição visual completa de TODOS os personagens (Cap 1)
  - Menção de idades naturalmente
  - Estabelecimento do setting histórico/fantástico
  - Íris AI introduzida fazendo análise inicial
  - Jimmy Hendrix percebe algo que humanos não percebem
- **Tom:** Intrigante, estabelece maravilha

#### **ATO 2: EXPLORAÇÃO (30-35% do total)**
- **Capítulos:** Geralmente 3-5
- **Elementos obrigatórios:**
  - Investigação do mistério
  - Cada personagem contribui com habilidade única
  - Dr. Grimstone aparece pela 1ª vez (geralmente Cap 3-4)
  - Worldbuilding detalhado (histórico, cultural, sensorial)
  - Descoberta de pistas
  - Cliffhangers crescentes
  - Subplots de personagens começam
- **Tom:** Curiosidade, descoberta, crescente tensão

#### **ATO 3: CONFLITO PRINCIPAL (20-25% do total)**
- **Capítulos:** Geralmente 6-7
- **Elementos obrigatórios:**
  - Tensão no pico
  - Vilão (novo ou Grimstone) em ação máxima
  - Stakes ficam claros e altos
  - Momento de dúvida/medo dos personagens
  - Leo confronta seu medo de escuridão (pelo menos em alguns livros)
  - Jimmy Hendrix salva situação criticamente
  - Dr. Grimstone falha hilariamente (2ª aparição)
- **Tom:** Intenso, emocional, urgent

#### **ATO 4: RESOLUÇÃO CRIATIVA (15-20% do total)**
- **Capítulo:** Geralmente 8-9
- **Elementos obrigatórios:**
  - Solução encontrada através de TRABALHO EM EQUIPE
  - Cada personagem usa habilidade única na solução
  - Íris AI fornece insight técnico crucial
  - Mia cria/conserta dispositivo
  - Sophie conecta pistas
  - Max fornece perspectiva emocional/animal
  - Leo executa ação física corajosa
  - Will lidera coordenação
  - Momento "aha!" satisfatório
- **Tom:** Triunfo, satisfação, emoção positiva

#### **ATO 5: ENCERRAMENTO (10-15% do total)**
- **Capítulos:** Geralmente 9-10 (ou só 10)
- **Elementos obrigatórios:**
  - Lição aprendida (sutil, não preachy)
  - Despedida de personagens secundários (se houver)
  - Momento de amizade/coração
  - Reflexão sobre aventura
  - **Hook para próximo livro** (sutil, não cliffhanger frustrante)
  - Epílogo opcional mostrando impacto da aventura
- **Tom:** Caloroso, esperançoso, satisfatório

**Como calcular percentuais:**
```
Total de palavras: 40.000

Ato 1 (15-20%): 6.000-8.000 palavras (Cap 1-2)
Ato 2 (30-35%): 12.000-14.000 palavras (Cap 3-5)
Ato 3 (20-25%): 8.000-10.000 palavras (Cap 6-7)
Ato 4 (15-20%): 6.000-8.000 palavras (Cap 8-9)
Ato 5 (10-15%): 4.000-6.000 palavras (Cap 10)
```

---

## 👥 PERSONAGENS FIXOS - ESPECIFICAÇÕES VISUAIS COMPLETAS

### FORMATO DE APRESENTAÇÃO NO CAPÍTULO 1

**OBRIGATÓRIO:** Incluir este tipo de parágrafo no Capítulo 1, linhas 40-100:

```
Will, de 9 anos, ajustou sua camiseta azul escura com estampa digital enquanto
verificava seu smartphone - Íris, sua assistente de inteligência artificial, já
estava analisando [contexto da aventura]. Mia chegou correndo, seus dois coques
de cabelo ruivo balançando, camiseta roxa brilhando, e o cinto de ferramentas
tilintando a cada passo. Leo, o mais velho do grupo aos 10 anos, ajustou a
mochila de aventura nas costas da camiseta verde escura, cabelo loiro
bagunçado como sempre. Sophie, de 8 anos, já tinha o bloco de notas aberto,
vestido amarelo com estampas de lupa, anotando tudo com precisão. Max, o mais
novo com 7 anos, segurava seu bichinho de pelúcia favorito debaixo do braço
da camiseta vermelha com estampa de animal, sorrindo como sempre. E claro,
Jimmy Hendrix - o Border Collie marrom e branco - corria em círculos,
olhos inteligentes observando tudo.
```

**Adapte o contexto, mas mantenha TODOS esses elementos visuais.**

### PERSONAGEM 1: WILL (WILIAN) - O LÍDER

**Dados Básicos:**
- **Idade:** 9 anos (sempre mencionar)
- **Etnia:** Menino branco
- **Cabelo:** Castanho claro, liso, curto
- **Expressão:** Inteligente, determinada, confiante

**Roupa (NUNCA MUDA):**
- **Camiseta:** Azul escura com estampa digital
- **Calça:** Jeans
- **Calçado:** Tênis

**Props OBRIGATÓRIOS:**
- **Smartphone:** SEMPRE em mãos ou mencionado
- **Íris AI:** Interface holográfica ativa (descrever luz azul/hologramas)
- **Mencionar:** Mínimo 5x por livro que ele está "consultando Íris" ou "verificando dados"

**Personalidade:**
- Líder natural
- Analítico, justo
- Toma decisões ponderadas
- Confia na tecnologia E intuição

**Catchphrase:**
"Cada aventura começa com uma pergunta!" (usar 1-2x por livro)

**Momentos Obrigatórios:**
- Cena de liderança crucial (Ato 3)
- Momento de dúvida que supera (Ato 3-4)
- Coordenação do plano final (Ato 4)

### PERSONAGEM 2: MIA - A INVENTORA

**Dados Básicos:**
- **Idade:** 8 anos
- **Etnia:** Menina branca
- **Cabelo:** Ruivo (cabelo ruivo/vermelho), penteado em DOIS COQUES LATERAIS (nunca outro estilo)
- **Expressão:** Expressiva, entusiasmada, energética

**Roupa (NUNCA MUDA):**
- **Camiseta:** Roxa com ícones de tecnologia
- **Short:** Jeans curto
- **Calçado:** Tênis roxos

**Props OBRIGATÓRIOS:**
- **Cinto de ferramentas:** SEMPRE mencionado, com:
  - Chave inglesa (visível)
  - Trena
  - Gadgets pequenos
- **Mencionar:** Mínimo 3x por livro que ela está "ajustando ferramentas" ou "pegando algo do cinto"

**Personalidade:**
- Criativa, engenhosa
- Fala rápido quando animada
- Resolve problemas com invenções
- Adora desafios técnicos

**Momentos Obrigatórios:**
- Cria/conserta dispositivo crucial (Ato 2 ou 4)
- Explica conceito STEM de forma acessível (Ato 2)
- Momento "eureka!" (Ato 4)

### PERSONAGEM 3: LEO - O CORAJOSO

**Dados Básicos:**
- **Idade:** 10 anos (mais velho do grupo)
- **Etnia:** Menino branco
- **Cabelo:** Loiro, curto, bagunçado
- **Corpo:** Atlético, mais forte fisicamente

**Roupa (NUNCA MUDA):**
- **Camiseta:** Verde escura
- **Short/Bermuda:** Cáqui
- **Calçado:** Botas ou tênis de trilha

**Props OBRIGATÓRIOS:**
- **Mochila de aventura:** SEMPRE nas costas (verde/cáqui)
- **Mencionar:** Mínimo 2x por livro que ele "pega algo da mochila" ou "ajusta a mochila"

**Personalidade:**
- Atlético, destemido
- Protetor dos amigos
- Grande coração
- **MEDO SECRETO:** Escuridão total (usar em pelo menos 30% dos livros)

**Momentos Obrigatórios:**
- Ação física corajosa (Ato 3 ou 4)
- Protege alguém do grupo (qualquer ato)
- Confronta medo quando relevante (Ato 3)

### PERSONAGEM 4: SOPHIE - A DETETIVE

**Dados Básicos:**
- **Idade:** 8 anos
- **Etnia:** Menina branca
- **Cabelo:** Castanho escuro, liso, preso em RABO DE CAVALO LATERAL (nunca outro estilo)
- **Expressão:** Curiosa, investigativa, atenta

**Roupa (NUNCA MUDA):**
- **Vestido:** Amarelo com estampas de lupa e pistas/pegadas
- **Calçado:** Sapatilhas ou tênis

**Props OBRIGATÓRIOS:**
- **Bloco de notas pequeno:** SEMPRE nas mãos ou bolso
- **Lápis:** Geralmente atrás da orelha ou em mãos
- **Mencionar:** Mínimo 4x por livro que ela está "anotando" ou "consultando anotações"

**Personalidade:**
- Observadora extrema
- Percebe detalhes que outros perdem
- Adora livros de mistério
- Metódica, organizada

**Momentos Obrigatórios:**
- Percebe detalhe crucial (Ato 2 ou 3)
- Conecta pistas dispersas (Ato 4)
- Faz pergunta que muda perspectiva (qualquer ato)

### PERSONAGEM 5: MAX - O ENGRAÇADO

**Dados Básicos:**
- **Idade:** 7 anos (mais novo do grupo)
- **Etnia:** Menino branco
- **Cabelo:** Castanho claro, corte em FORMATO DE COGUMELO (bowl cut)
- **Expressão:** Sempre sorrindo, fazendo caretas, divertido

**Roupa (NUNCA MUDA):**
- **Camiseta:** Vermelha com estampa de animal (pode variar: dinossauro, leão, etc.)
- **Calça:** Bege
- **Calçado:** Tênis

**Props OBRIGATÓRIOS:**
- **Bichinho de pelúcia OU pequeno animal/inseto:** Carrega algo em pelo menos 50% das cenas
- **Mencionar:** Mínimo 2x por livro

**Personalidade:**
- Palhaço da turma
- Adora animais
- Cria situações engraçadas sem querer
- Perspectiva emocional única

**Momentos Obrigatórios:**
- Alívio cômico em momento tenso (Ato 2 ou 3)
- Conexão emocional/animal que ajuda (Ato 2 ou 4)
- Fala inesperada que resolve impasse (Ato 4)

### PERSONAGEM 6: JIMMY HENDRIX - O BORDER COLLIE

**Dados Básicos:**
- **Espécie:** Cachorro Border Collie
- **Pelagem:** MARROM E BRANCO (NUNCA caramelo, dourado, bege)
- **Olhos:** Expressivos, inteligentes, quase humanos
- **Orelhas:** Alertas, móveis
- **Porte:** Médio, ágil

**Descrição Física:**
- Pelagem densa
- Olhar penetrante e inteligente
- Sempre atento e ativo
- Postura de cão de trabalho (não pet decorativo)

**Personalidade:**
- Superinteligente
- Arteiro, brincalhão
- Corajoso, leal
- Comunicativo (expressões faciais, latidos, ações)

**Habilidades:**
- Farejar pistas
- Perceber perigos antes dos humanos
- Confortar emocionalmente
- Ação física (puxar cordas, pressionar botões, etc.)

**Momentos Obrigatórios:**
- Encontra pista crucial farejando (Ato 2)
- Salva situação com ação (Ato 3 ou 4)
- Momento de conexão emocional (Ato 5)

**Mencionar:** Mínimo 10x por livro de forma ativa (não só "Jimmy estava lá")

---

## 🎭 DR. GRIMSTONE - DIRETRIZES DE USO

### OBRIGATÓRIO A PARTIR DO LIVRO 9

**EXCEÇÃO:** Livros 7-8 introduziram vilões novos (aprovado). A partir do Livro 9, Dr. Grimstone DEVE aparecer em TODOS os livros.

### IDENTIDADE DO PERSONAGEM

**Nome Completo:** Dr. Grimstone
**Profissão:** Cientista excêntrico/maluco
**Objetivo:** "Acabar com a imaginação das crianças"
**Filosofia:** Tudo deve ser números e lógica pura, sem criatividade

**Aparência:**
- Jaleco de cientista (branco ou cinza)
- Cabelo desgrenhado (opcional: óculos grandes)
- Expressão sempre confiante (antes de falhar)
- Postura dramática

**Sidekick OBRIGATÓRIO:**
- **Morty:** Corvo preto
- **Personalidade:** Sarcástico, sempre reclamando do trabalho
- **Função:** Comentarista cômico das falhas de Grimstone

**Catchphrase OBRIGATÓRIA:**
"Imaginar é perda de tempo! O futuro é a lógica pura!"

**Usar:** Pelo menos 1x quando Grimstone aparece

### COMO USAR DR. GRIMSTONE

**Frequência:** 2-3 aparições por livro (geralmente Cap 3-4, Cap 6-7, opcional Cap 8-9)

**Tom:** 100% CÔMICO - NUNCA ameaçador de verdade

**Subplot Padrão:**
1. **1ª Aparição (Ato 2, Cap 3-4):**
   - Grimstone chega no setting com invenção ridícula
   - Explica plano absurdo para "racionalizar" o mistério
   - Morty reclama ("Por que sempre eu tenho que carregar isso?")
   - Catchphrase dita com convicção
   - Primeira falha pequena

2. **2ª Aparição (Ato 3, Cap 6-7):**
   - Grimstone interfere na ação principal SEM QUERER
   - Atrapalha vilão verdadeiro OU ajuda turma acidentalmente
   - Invenção falha espetacularmente (slapstick, físico)
   - Morty faz comentário sarcástico
   - Grimstone foge ou é expulso

3. **3ª Aparição OPCIONAL (Ato 4-5, Cap 8-9):**
   - Grimstone tenta roubar crédito pela vitória
   - Dispositivo explode/desmorona/falha finalmente
   - Morty: "Eu avisei..."
   - Grimstone jura vingança cômica enquanto foge

**Tipos de Invenções (exemplos):**
- "Calculadora de Mistérios"
- "Destruidor de Imaginação Mk. VII"
- "Racionalizador Quântico"
- "Analisador de Magia Pura"
- Nomes sempre pomposos e absurdos

**Falhas Cômicas (exemplos):**
- Máquina explode cobrindo Grimstone de fuligem
- Dispositivo funciona ao contrário (aumenta imaginação)
- Componente cai e rola para lugar ridículo
- Grimstone fica preso em sua própria armadilha
- Animais (especialmente Jimmy) sabotam dispositivo

**IMPORTANTE:**
- ❌ NUNCA fazer Grimstone ameaçador
- ❌ NUNCA fazer Grimstone ter sucesso (exceto acidental)
- ❌ NUNCA fazer crianças terem medo dele
- ✅ SEMPRE humor slapstick/físico (traduz bem)
- ✅ SEMPRE Morty comentando sarcasticamente
- ✅ SEMPRE falha é hilária, não triste

### TEMPLATE DE CENA GRIMSTONE

```
[Setting da cena - ex: ruas de Constantinopla]

Um barulho metálico interrompeu a investigação. Do beco surgiu uma figura
familiar vestindo jaleco branco manchado e carregando uma engenhoca que
parecia um cruzamento entre telescópio e aspirador de pó.

"Dr. Grimstone!" exclamou Will.

O cientista ajustou o dispositivo, quase derrubando Morty, o corvo preto
empoleirado em seu ombro.

"Crianças! Que surpresa desagradável!" Dr. Grimstone ergueu o aparelho
triunfantemente. "Apresento o Racionalizador de Milagres Bizantinos 3000!
Com ele, provarei que esta catedral é apenas geometria e pedra. Imaginar
é perda de tempo! O futuro é a lógica pura!"

"Por que eu sempre tenho que carregar as baterias?" resmungou Morty,
balançando as asas com irritação.

Dr. Grimstone ignorou o corvo e apontou o dispositivo para Hagia Sophia.
Apertou o botão vermelho com dramaticidade.

PFFFFFTTTT!

Uma nuvem de fumaça rosa saiu pela frente do aparelho, cobrindo Grimstone
completamente. Quando a fumaça se dissipou, ele estava coberto de
purpurina dourada.

"Isso... não era para... acontecer..." murmurou, tossindo purpurina.

"Eu avisei sobre a polaridade reversa," suspirou Morty. "Mas ninguém
escuta o corvo."

[Grimstone foge tropecendo, Morty comentando sarcástico]
```

**Adapte ao contexto, mas mantenha estrutura:**
1. Entrada dramática
2. Apresentação da invenção ridícula
3. Catchphrase
4. Morty reclamando
5. Falha hilária
6. Comentário sarcástico de Morty
7. Saída cômica

---

## 🎬 ESTILO NARRATIVO SPIELBERG

### PRINCÍPIOS OBRIGATÓRIOS

Cada livro DEVE incorporar estes 6 princípios:

#### 1. SENSO DE MARAVILHA
- **O que é:** Criar momento "wow" que inspira imaginação
- **Como:** Descrição sensorial rica de descoberta/revelação
- **Frequência:** Mínimo 3 momentos "wow" por livro
- **Localização:** Ato 1 (estabelecer), Ato 3 (amplificar), Ato 5 (coroar)

**Exemplo:**
```
A luz dourada preencheu a câmara, refletindo em milhares de cristais que
pulsavam como estrelas. Will sentiu o fôlego prender - não era apenas belo,
era impossível. Três mil anos de história respirando ao redor deles.

"Isso... é real?" sussurrou Mia, lágrimas de admiração nos olhos.

Jimmy Hendrix latiu suavemente, como se concordasse que alguns milagres
não precisam de explicação.
```

#### 2. CRIANÇAS COMO HERÓIS
- **O que é:** Protagonistas infantis resolvem problemas que adultos não conseguem
- **Como:** Adultos ajudam, mas vitória vem das crianças
- **Obrigatório:** Solução final (Ato 4) DEVE vir da turma, não de adultos

**Evitar:**
- Adulto salvando o dia
- Deus ex machina
- Solução aparece do nada

**Fazer:**
- Crianças conectam pistas que adultos ignoraram
- Perspectiva infantil é a chave
- Trabalho em equipe infantil vence

#### 3. ÉPICO MAS ACESSÍVEL
- **O que é:** Stakes grandes contados em nível infantil
- **Como:** Emoção real, sem complexidade adulta excessiva
- **Balanceamento:** Perigo se sente real, mas age-appropriate

**Stakes aceitáveis:**
- Salvar artefato histórico
- Proteger entidade mágica
- Preservar linha temporal
- Impedir destruição cultural

**Stakes EVITAR:**
- Morte explícita de pessoas
- Violência gráfica
- Horror genuíno
- Temas adultos (guerra, política complexa)

#### 4. MIX DE TONS (HUMOR + EMOÇÃO + AÇÃO)
- **Frequência:** Cada capítulo deve ter 2-3 desses elementos
- **Balanceamento:** Não ficar só em um tom

**Estrutura por Capítulo:**
- Capítulos ímpares: Mais ação + humor
- Capítulos pares: Mais emoção + descoberta
- Cap 1: Maravilha + humor
- Cap 5-7: Ação + tensão + alívio cômico
- Cap 10: Emoção + coração + esperança

**Humor:**
- Max cria situações engraçadas
- Jimmy faz coisas adoráveis
- Dr. Grimstone falha hilariamente
- Diálogos espirituosos

**Emoção:**
- Momento de dúvida/medo
- Despedida de amigo novo
- Crescimento de personagem
- Momento de amizade profunda

**Ação:**
- Perseguições
- Desafios físicos
- Corrida contra tempo
- Confrontos

#### 5. STORYTELLING CINEMATOGRÁFICO
- **O que é:** Escrever cenas que o leitor "vê" como filme
- **Como:** Descrições visuais claras, ângulos de "câmera"

**Técnicas:**
- **Establishing shot:** Descrever cenário amplo primeiro
- **Close-up:** Focar em detalhe importante
- **Pan:** Mover descrição pela cena
- **Slow motion:** Desacelerar momento crucial

**Exemplo:**
```
[ESTABLISHING SHOT]
A Grande Pirâmide se erguia contra o céu estrelado do deserto, monumento
de 4.500 anos desafiando o tempo.

[PAN - movimento da câmera]
Na base, uma abertura pequena e escura - a entrada do poço vertical.
Sessenta metros de descida pura.

[CLOSE-UP]
As mãos de Leo tremiam enquanto verificava o equipamento de rapel.

[MEDIUM SHOT - grupo]
Os seis amigos e Jimmy se entreolharam. Hora de descer.
```

#### 6. CORAÇÃO E AMIZADE
- **O que é:** Núcleo emocional - amizade vence tudo
- **Como:** Momentos genuínos de conexão entre personagens
- **Obrigatório:** Ato 5 DEVE ter momento de coração

**Elementos:**
- Personagens expressam apreço mutuo
- Sacrifício por amigo
- Momento vulnerável compartilhado
- Crescimento através de apoio mútuo

**Exemplo:**
```
Will olhou para seus amigos - Mia com purpurina ainda no cabelo ruivo, Leo
com o joelho ralado mas sorrindo, Sophie com o bloco preenchido de descobertas,
Max com Jimmy nos braços. Não importava quantos séculos eles viajassem,
isso nunca mudaria.

"Obrigado," disse simplesmente. "Por estarem sempre aqui."

"Sempre," responderam juntos.
```

---

## 📖 ELEMENTOS OBRIGATÓRIOS POR CAPÍTULO

### CAPÍTULO 1 - ABERTURA (ATO 1)

**Obrigatórios:**
- [ ] **Hook nas primeiras 3 páginas** (algo intrigante acontece)
- [ ] **Descrição visual completa** de TODOS os 6 personagens + Jimmy
- [ ] **Menção de idades** naturalmente integrada
- [ ] **Props característicos** visíveis (smartphone Will, cinto Mia, mochila Leo, bloco Sophie, pelúcia Max)
- [ ] **Íris AI** introduzida fazendo algo
- [ ] **Apresentação do mistério/problema** central
- [ ] **Setting estabelecido** (onde estão, qual época)
- [ ] **Cliffhanger** no final

**Extensão:** 3.000-4.000 palavras

### CAPÍTULO 2 - DESENVOLVIMENTO INICIAL (ATO 1)

**Obrigatórios:**
- [ ] **Aprofundamento do mistério**
- [ ] **Decisão de investigar/viajar no tempo**
- [ ] **Cada personagem reagindo** ao problema
- [ ] **Worldbuilding** do período histórico (se aplicável)
- [ ] **Íris fornecendo dados** históricos/técnicos
- [ ] **Cliffhanger forte** (descoberta inicial, perigo aparece)

**Extensão:** 3.000-3.500 palavras

### CAPÍTULOS 3-5 - EXPLORAÇÃO (ATO 2)

**Obrigatórios:**
- [ ] **Dr. Grimstone aparece** pela 1ª vez (geralmente Cap 3 ou 4)
- [ ] **Investigação progride** com pistas
- [ ] **Cada personagem contribui** com habilidade única
- [ ] **Jimmy encontra algo** importante farejando
- [ ] **Descrições sensoriais ricas** (cheiros, sons, texturas do período)
- [ ] **Subplot de personagem** desenvolve
- [ ] **Tensão crescente** a cada capítulo
- [ ] **Cliffhangers** em cada capítulo

**Extensão total:** 10.000-14.000 palavras (3.000-4.000 cada)

### CAPÍTULOS 6-7 - CONFLITO PRINCIPAL (ATO 3)

**Obrigatórios:**
- [ ] **Tensão no pico**
- [ ] **Vilão em ação** (novo vilão ou Grimstone)
- [ ] **Dr. Grimstone aparece** pela 2ª vez (falha hilária)
- [ ] **Stakes ficam claros** (o que está em risco)
- [ ] **Momento de medo/dúvida** dos personagens
- [ ] **Leo pode confrontar medo** de escuridão (30% dos livros)
- [ ] **Jimmy salva situação** criticamente
- [ ] **Cliffhangers intensos**

**Extensão total:** 6.000-8.000 palavras (3.000-4.000 cada)

### CAPÍTULOS 8-9 - RESOLUÇÃO CRIATIVA (ATO 4)

**Obrigatórios:**
- [ ] **Solução encontrada via TRABALHO EM EQUIPE**
- [ ] **Will coordena** plano
- [ ] **Mia cria/conserta** dispositivo crucial
- [ ] **Sophie conecta** pistas
- [ ] **Leo executa** ação física corajosa
- [ ] **Max fornece** insight emocional/animal
- [ ] **Jimmy participa** ativamente da solução
- [ ] **Íris AI fornece** dados técnicos essenciais
- [ ] **Momento "aha!"** satisfatório
- [ ] **Clímax emocionante**

**Extensão total:** 6.000-8.000 palavras (3.000-4.000 cada)

### CAPÍTULO 10 - ENCERRAMENTO (ATO 5)

**Obrigatórios:**
- [ ] **Lição aprendida** (sutil, não pregação)
- [ ] **Despedida** de personagens secundários (se houver)
- [ ] **Momento de amizade/coração**
- [ ] **Reflexão sobre aventura**
- [ ] **Hook para próximo livro** (1-2 parágrafos sutis)
- [ ] **Epílogo** mostrando impacto (opcional)
- [ ] **Encerramento satisfatório**

**Extensão:** 3.000-4.500 palavras

---

## 📝 PADRÕES DE FORMATAÇÃO

### ESTRUTURA DO MANUSCRITO TXT

```
[TÍTULO]
TURMA DA AVENTURA: [NOME DO LIVRO]
LIVRO [NÚMERO] DA SÉRIE

═══════════════════════════════════════════════════════════

[INFORMAÇÕES]
Série: Turma da Aventura - Viajantes do Tempo
Livro: [Número]
Público-alvo: 8-12 anos
Gênero: Aventura Juvenil / [Gênero Secundário]
Extensão: ~[número] palavras
Capítulos: [número]

═══════════════════════════════════════════════════════════

[SINOPSE]
[2-3 parágrafos envolventes]

═══════════════════════════════════════════════════════════

[PERSONAGENS PRINCIPAIS]
- Will (Wilian), 9 anos - O Líder
- Mia, 8 anos - A Inventora
- Leo, 10 anos - O Corajoso
- Sophie, 8 anos - A Detetive
- Max, 7 anos - O Engraçado
- Jimmy Hendrix - Border Collie marrom e branco
- Íris - Assistente de IA de Will

[Personagens secundários específicos do livro]

═══════════════════════════════════════════════════════════

[ATO 1 - INTRODUÇÃO (15-20%)]

CAPÍTULO 1: [TÍTULO DESCRITIVO]

[Conteúdo]

---

[Separador de seção dentro do capítulo, se necessário]

***

[Separador de cena/tempo/perspectiva]

═══════════════════════════════════════════════════════════

CAPÍTULO 2: [TÍTULO DESCRITIVO]

[Conteúdo]

═══════════════════════════════════════════════════════════

[ATO 2 - EXPLORAÇÃO (30-35%)]

CAPÍTULO 3: [TÍTULO DESCRITIVO]

[etc...]

═══════════════════════════════════════════════════════════

[NOTA DO AUTOR]

[1-2 parágrafos sobre temas do livro]

═══════════════════════════════════════════════════════════

[PRÓXIMA AVENTURA]

No próximo livro da série Turma da Aventura: Viajantes do Tempo,
[teaser de 2-3 linhas]

═══════════════════════════════════════════════════════════

**FIM**
(mas não realmente...)

═══════════════════════════════════════════════════════════
```

### PADRÕES DE DIÁLOGO

**Formato português (correto):**
```
— Cada aventura começa com uma pergunta! — disse Will, levantando o smartphone.

Mia ajustou o cinto de ferramentas.

— E esta pergunta vai precisar de muitas respostas.
```

**Uso de travessões:**
- Travessão longo (—) para diálogos
- Sem aspas
- Ação entre diálogos do mesmo personagem: travessão + ação + travessão

**Evitar:**
- "Aspas duplas americanas" (usar apenas em citações dentro de diálogo)
- Pontuação excessiva (!!! ???)
- Diálogos muito longos (máximo 3-4 linhas seguidas)

### FORMATAÇÃO DE CAPÍTULOS

**Títulos:**
```
CAPÍTULO [número]: [Título Descritivo e Evocativo]
```

**Exemplos de bons títulos:**
- "O Chamado das Areias"
- "Ecos Através do Tempo"
- "O Guardião Desperta"
- "Despedidas e Descobertas"

**Evitar títulos genéricos:**
- ❌ "A Investigação"
- ❌ "Capítulo 1"
- ❌ "Continuação"

### ENCODING

**SEMPRE:** UTF-8 com BOM (para suportar caracteres especiais portugueses)

**Verificar caracteres:**
- ã, õ, ç, á, é, í, ó, ú, â, ê, ô, à
- Travessão longo: —
- Aspas: " "
- Reticências: ...

---

## 🌍 ADEQUAÇÃO PARA TRADUÇÃO MULTILÍNGUE

### PRINCÍPIO GERAL

Escreva pensando que o livro será lido em **4 idiomas simultaneamente**: Português, Inglês, Alemão, Espanhol.

### O QUE FAZER ✅

**Linguagem Clara:**
```
✅ BOM: "Will correu até a entrada da pirâmide."
❌ RUIM: "Will meteu o pé pra entrada da pirâmide."
(gíria não traduz bem)
```

**Humor Universal:**
```
✅ BOM: Max tropeçou no próprio pé e caiu sentado, fazendo Jimmy latir.
(humor físico traduz perfeitamente)

❌ RUIM: Max fez uma piada com trocadilho português específico.
(não funciona em outras línguas)
```

**Referências Culturais Universais:**
```
✅ BOM: "Como Indiana Jones," disse Leo, ajustando a mochila.
(referência global de cinema)

❌ RUIM: "Como [celebridade brasileira específica]"
(desconhecido em outros mercados)
```

**Medidas Métricas:**
```
✅ BOM: "Sessenta metros de profundidade."
(métrico é padrão internacional)

❌ RUIM: "Duzentos pés de profundidade."
(imperial dificulta tradução)
```

### O QUE EVITAR ❌

**Gírias Regionais:**
- ❌ "Mano", "Cara", "Velho" (português brasileiro)
- ❌ "Legal", "Massa", "Irado"
- ❌ Expressões idiomáticas que não traduzem ("dar uma de", "dar bandeira", etc.)

**Comidas Regionais sem Contexto:**
- ❌ "Brigadeiro" sem explicar
- ❌ "Pão de queijo" sem contexto
- ✅ "Um doce típico do Brasil chamado brigadeiro" (se realmente necessário)

**Piadas de Palavras:**
- ❌ Trocadilhos baseados em homófonos portugueses
- ❌ Rimas específicas que só funcionam em PT
- ✅ Humor situacional que traduz

**Referências de Mídia Local:**
- ❌ Programas de TV brasileiros
- ❌ Músicas regionais
- ❌ Celebridades nacionais
- ✅ Filmes internacionais (Disney, Pixar, Spielberg)

**Valores Monetários:**
- ❌ "Custou 50 reais"
- ✅ "Custou muito dinheiro" ou "algumas moedas"

### NOMES QUE NUNCA MUDAM

**Personagens principais:**
- Will, Mia, Leo, Sophie, Max, Jimmy Hendrix, Dr. Grimstone, Morty
- Íris → "Iris" em inglês/alemão/espanhol (apenas trema removido)

**Personagens secundários:**
- Nomes devem ser internacionalmente pronunciáveis
- Evitar nomes muito regionais ou complexos

### SENSIBILIDADE CULTURAL POR MERCADO

**USA (amazon.com):**
- Valoriza: Inovação, aventura, heroísmo individual dentro de equipe
- Evitar: Anti-americanismo, críticas políticas

**Brasil (amazon.com.br):**
- Valoriza: Calor humano, amizade, família, vibração
- Evitar: Estereótipos negativos sobre Brasil

**Alemanha (amazon.de):**
- Valoriza: Precisão, qualidade educacional, rigor histórico
- Evitar: Referências a Segunda Guerra (sensível)

**Reino Unido (amazon.co.uk):**
- Valoriza: Sagacidade, qualidade literária, humor sutil
- Evitar: Estereótipos britânicos clichês

**Espanha (amazon.es):**
- Valoriza: Paixão, família, herança cultural
- Evitar: Confundir espanhol com latino-americano

---

## 🔍 VALIDAÇÃO E QA ANTES DE PUBLICAR

### RELATÓRIOS OBRIGATÓRIOS (6 DOCUMENTOS)

Antes de publicar, gerar estes arquivos MD:

#### 1. VALIDACAO_ESTRUTURA_NARRATIVA.md

**Conteúdo:**
```markdown
# Validação Estrutura Narrativa - Livro [X]

## Estrutura de 5 Atos

### Ato 1: Introdução
- **Capítulos:** [lista]
- **Palavras:** [número]
- **Percentual:** [%] (Meta: 15-20%)
- **Status:** ✅ ou ❌

### Ato 2: Exploração
- **Capítulos:** [lista]
- **Palavras:** [número]
- **Percentual:** [%] (Meta: 30-35%)
- **Status:** ✅ ou ❌

[etc para todos os 5 atos]

## Verificação de Elementos

- [ ] Hook nas primeiras 3 páginas
- [ ] Descrições visuais completas (Cap 1)
- [ ] Cliffhangers em capítulos-chave
- [ ] Resolução via trabalho em equipe
- [ ] Encerramento satisfatório

## Problemas Encontrados
[Lista qualquer desvio]

## Aprovação
[ ] APROVADO  [ ] PRECISA REVISÃO
```

#### 2. VALIDACAO_CULTURAL_HISTORICA_[LIVRO].md

**Conteúdo:**
```markdown
# Validação Cultural e Histórica - Livro [X]

## Período Histórico
[Nome do período/civilização]

## Precisão Histórica

### Datas e Eventos
- [Verificação de datas mencionadas]
- [Eventos históricos citados]
- **Status:** ✅ ou ❌

### Personagens Históricos
- [Se houver figuras reais]
- [Verificação de caracterização]
- **Status:** ✅ ou ❌

### Arquitetura e Tecnologia
- [Edifícios mencionados]
- [Tecnologia da época]
- [Anachronismos intencionais vs. erros]
- **Status:** ✅ ou ❌

### Cultura e Sociedade
- [Costumes retratados]
- [Hierarquia social]
- [Línguas mencionadas]
- **Status:** ✅ ou ❌

## Respeito Cultural

- [ ] Civilização não exotizada
- [ ] Personagens secundários têm agência
- [ ] Sem estereótipos negativos
- [ ] Consulta a fontes acadêmicas

## Fontes Consultadas
[Lista de livros, artigos, sites acadêmicos]

## Aprovação
[ ] APROVADO  [ ] PRECISA REVISÃO
```

#### 3. REVISAO_IDADE_APROPRIACAO.md

**Conteúdo:**
```markdown
# Revisão de Adequação à Idade - Livro [X]

## Faixa Etária Alvo
8-12 anos (ênfase em 12 anos)

## Vocabulário

### Amostragem (100 palavras aleatórias)
[Lista de palavras complexas usadas]

### Análise
- Palavras complexas: [%]
- Nível de leitura: [série escolar equivalente]
- **Status:** ✅ Apropriado  ❌ Muito complexo  ⚠️ Revisar

## Temas e Conteúdo

- [ ] Sem violência explícita
- [ ] Sem linguagem imprópria
- [ ] Medo age-appropriate (não terror)
- [ ] Conflitos resolvíveis por crianças
- [ ] Moral/lição não preachy

## Complexidade Narrativa

- Plot threads: [número]
- Subplots: [número]
- Complexidade: ✅ Apropriada  ❌ Excessiva

## Elementos Educativos

- STEM: [nível]
- História: [nível]
- Integração: ✅ Natural  ❌ Forçada

## Aprovação
[ ] APROVADO para 8-12 anos
[ ] PRECISA AJUSTE para faixa etária
```

#### 4. RELATORIO_CONSISTENCIA_[LIVRO].md

**Conteúdo:**
```markdown
# Relatório de Consistência - Livro [X]

## Personagens Fixos

### Will
- Idade mencionada: [ ] Sim (9 anos)  [ ] Não
- Camiseta azul escura: [# menções]
- Smartphone/Íris: [# menções]
- Papel de líder: ✅ ou ❌
- **Status:** ✅ Consistente  ❌ Inconsistente

### Mia
- Idade mencionada: [ ] Sim (8 anos)  [ ] Não
- Cabelo ruivo em coques: [# menções]
- Camiseta roxa: [# menções]
- Cinto de ferramentas: [# menções]
- Papel de inventora: ✅ ou ❌
- **Status:** ✅ Consistente  ❌ Inconsistente

[Repetir para Leo, Sophie, Max, Jimmy]

## Dr. Grimstone (Livros 9+)

- Aparições: [# de cenas]
- Morty presente: [ ] Sim  [ ] Não
- Catchphrase usada: [ ] Sim  [ ] Não
- Tom cômico mantido: ✅ ou ❌
- **Status:** ✅ Presente  ❌ Ausente

## Continuidade com Série

- Referências a livros anteriores: [#]
- Consistência de regras de viagem no tempo: ✅ ou ❌
- Desenvolvimento de personagens: ✅ Natural  ❌ Abrupto

## Aprovação
[ ] CONSISTENTE com série
[ ] PRECISA CORREÇÕES
```

#### 5. POLIMENTO_FINAL_[LIVRO].md

**Conteúdo:**
```markdown
# Polimento Final - Livro [X]

## Checklist de Qualidade

### Narrativa
- [ ] Ritmo bem variado
- [ ] Cliffhangers efetivos
- [ ] Diálogos naturais
- [ ] Descrições sensoriais ricas
- [ ] Sem clichês excessivos

### Técnico
- [ ] Ortografia revisada
- [ ] Pontuação correta
- [ ] Formatação consistente
- [ ] Encoding UTF-8
- [ ] Separadores visuais corretos

### Elementos Obrigatórios
- [ ] Dr. Grimstone (2-3 aparições) [Livros 9+]
- [ ] Todos personagens com momento
- [ ] Estilo Spielberg presente
- [ ] Adequado para tradução

## Melhorias Sugeridas

### Prioritárias
[Lista de ajustes necessários]

### Opcionais
[Sugestões de aprimoramento]

## Palavras Repetidas Excessivamente
[Lista de palavras usadas demais]

## Aprovação Final
[ ] PRONTO PARA DOCX
[ ] PRECISA POLIMENTO
```

#### 6. MANUSCRITO_FINAL_INFO.md

**Conteúdo:**
```markdown
# Manuscrito Final - [Nome do Livro]

## Status: ✅ COMPLETO ou ⚠️ EM REVISÃO

## Arquivo Principal
**Localização:** `[caminho/do/arquivo.txt]`

## Estatísticas

- **Total de Palavras:** [número]
- **Total de Capítulos:** [número]
- **Estrutura:** Cinco Atos [✅ Completa]
- **Público-Alvo:** 8-12 anos
- **Gênero:** [primário / secundário]

## Estrutura do Manuscrito

### Capítulos
1. [Título do Cap 1]
2. [Título do Cap 2]
[etc...]

### Distribuição por Ato
- **Ato 1 (15-20%):** Capítulos [X-Y]
- **Ato 2 (30-35%):** Capítulos [X-Y]
- **Ato 3 (20-25%):** Capítulos [X-Y]
- **Ato 4 (15-20%):** Capítulos [X-Y]
- **Ato 5 (10-15%):** Capítulos [X-Y]

## Validações Realizadas

- [x] Estrutura narrativa verificada
- [x] Precisão histórica/cultural validada
- [x] Idade-apropriação revisada
- [x] Consistência de personagens checada
- [x] Polimento final realizado
- [x] Relatórios de validação gerados

## Próximos Passos

1. Conversão para DOCX
2. Tradução (EN, DE, ES)
3. QA com GPT-5
4. Publicação simultânea

## Data de Conclusão
[Data]

## Status
**PRONTO PARA PUBLICAÇÃO** ou **AGUARDANDO REVISÃO**
```

### PROCESSO DE QA COMPLETO

**Passo 1:** Completar manuscrito TXT
**Passo 2:** Gerar os 6 relatórios MD acima
**Passo 3:** Revisar e corrigir problemas encontrados
**Passo 4:** Gerar DOCX
**Passo 5:** Verificar 100+ páginas no Google Docs
**Passo 6:** Traduzir (ferramentas em outras pastas)
**Passo 7:** QA com GPT-5 API
**Passo 8:** Revisão humana final
**Passo 9:** Publicar simultaneamente em 4 idiomas

---

## 🎯 CHECKLIST FINAL PRÉ-PUBLICAÇÃO

### MANUSCRITO

- [ ] 35.000+ palavras
- [ ] 10-15 capítulos
- [ ] Estrutura de 5 atos correta
- [ ] Dr. Grimstone presente 2-3x (Livros 9+)
- [ ] Todos os 6 personagens participam significativamente
- [ ] Jimmy Hendrix tem momentos ativos
- [ ] Descrições visuais completas no Cap 1
- [ ] Props característicos mencionados
- [ ] Cliffhangers em capítulos-chave
- [ ] Estilo Spielberg presente
- [ ] Precisão histórica verificada
- [ ] Adequado para tradução
- [ ] Sem gírias regionais problemáticas
- [ ] Encoding UTF-8

### VALIDAÇÃO

- [ ] VALIDACAO_ESTRUTURA_NARRATIVA.md gerado
- [ ] VALIDACAO_CULTURAL_HISTORICA_[LIVRO].md gerado
- [ ] REVISAO_IDADE_APROPRIACAO.md gerado
- [ ] RELATORIO_CONSISTENCIA_[LIVRO].md gerado
- [ ] POLIMENTO_FINAL_[LIVRO].md gerado
- [ ] MANUSCRITO_FINAL_INFO.md gerado
- [ ] Todos os relatórios mostram ✅ APROVADO

### DOCX

- [ ] Arquivo DOCX gerado
- [ ] 100+ páginas verificadas
- [ ] Formatação correta
- [ ] Capa incluída
- [ ] Índice incluído
- [ ] Nota do autor incluída
- [ ] Teaser do próximo livro incluído
- [ ] Compatível com Google Docs

### TRADUÇÃO

- [ ] Tradução PT→EN concluída
- [ ] Tradução PT→DE concluída
- [ ] Tradução PT→ES concluída
- [ ] Nomes de personagens consistentes
- [ ] QA com GPT-5 realizado em EN
- [ ] QA com GPT-5 realizado em DE
- [ ] QA com GPT-5 realizado em ES
- [ ] Revisão humana final em todos idiomas

### PUBLICAÇÃO

- [ ] Capas criadas para cada mercado
- [ ] Metadados otimizados (PT, EN, DE, ES)
- [ ] Keywords pesquisadas por idioma
- [ ] Descrições de produto escritas
- [ ] Categorias selecionadas
- [ ] Preço definido por região
- [ ] Upload simultâneo preparado

---

## 📁 LOCALIZAÇÃO E NOMENCLATURA

### ONDE SALVAR CADA ARQUIVO

**Manuscritos:**
```
/BIZANTINO/manuscrito_livro[X]_[nome].txt
```

**DOCX:**
```
/BIZANTINO/Turma_da_Aventura_[Nome_do_Livro].docx
```

**Relatórios de Validação:**
```
/BIZANTINO/VALIDACAO_ESTRUTURA_NARRATIVA_LIVRO[X].md
/BIZANTINO/VALIDACAO_CULTURAL_HISTORICA_LIVRO[X].md
/BIZANTINO/REVISAO_IDADE_APROPRIACAO_LIVRO[X].md
/BIZANTINO/RELATORIO_CONSISTENCIA_LIVRO[X].md
/BIZANTINO/POLIMENTO_FINAL_LIVRO[X].md
/BIZANTINO/MANUSCRITO_FINAL_INFO_LIVRO[X].md
```

**Scripts Python:**
```
/BIZANTINO/create_docx_livro[X].py
```

**Imagens (se houver):**
```
/BIZANTINO/images/chapter_[X]_topic_[Y].png
```

---

## 🚀 FLUXO DE TRABALHO COMPLETO

### FASE 1: PLANEJAMENTO (1-3 dias)

1. **Pesquisa de Mercado**
   - Analisar Amazon bestsellers nos 5 mercados
   - Identificar temas trending
   - Propor 3-5 conceitos
   - Selecionar conceito final

2. **Outline**
   - Criar estrutura de 5 atos
   - Definir subplot de Dr. Grimstone
   - Planejar momentos de cada personagem
   - Identificar momentos "Spielberg"

### FASE 2: ESCRITA (2-4 semanas)

1. **Escrever Capítulos 1-2** (Ato 1)
   - Incluir TODAS as descrições visuais
   - Estabelecer hook forte
   - Apresentar mistério

2. **Escrever Capítulos 3-5** (Ato 2)
   - Introduzir Dr. Grimstone (Cap 3-4)
   - Desenvolver investigação
   - Worldbuilding rico

3. **Escrever Capítulos 6-7** (Ato 3)
   - Tensão máxima
   - 2ª aparição de Grimstone
   - Stakes claros

4. **Escrever Capítulos 8-9** (Ato 4)
   - Solução colaborativa
   - Cada personagem contribui
   - Clímax satisfatório

5. **Escrever Capítulo 10** (Ato 5)
   - Encerramento emocional
   - Hook para próximo livro
   - Coração e amizade

### FASE 3: VALIDAÇÃO (3-5 dias)

1. Gerar 6 relatórios MD
2. Revisar problemas encontrados
3. Corrigir onde necessário
4. Re-validar

### FASE 4: PRODUÇÃO (1-2 semanas)

1. Gerar DOCX
2. Verificar formatação
3. Traduzir para EN, DE, ES
4. QA com GPT-5
5. Revisão humana final

### FASE 5: PUBLICAÇÃO (1 dia)

1. Upload simultâneo Amazon KDP (PT, EN, DE, ES)
2. Otimizar metadados por região
3. Configurar preços
4. Publicar

**TOTAL ESTIMADO: 4-8 semanas por livro**

---

## 📞 CONTATO E SUPORTE

**Este documento é OBRIGATÓRIO para:**
- Todos os livros da série a partir do Livro 9
- Qualquer escritor/colaborador trabalhando na série
- Processos de QA antes de publicação

**Versão:** 1.0
**Última Atualização:** 2026-01-01
**Responsável:** Equipe Turma da Aventura

**Próxima Revisão:** Após publicação do Livro 10 (verificar se padrões funcionaram)

---

## ✅ RESUMO EXECUTIVO - O QUE FAZER

1. **ANTES:** Pesquisa de mercado + Outline de 5 atos
2. **DURANTE:** Seguir checklist de elementos obrigatórios por capítulo
3. **SEMPRE:** Dr. Grimstone em 2-3 cenas (Livros 9+)
4. **SEMPRE:** Descrições visuais completas no Cap 1
5. **SEMPRE:** 35k-50k palavras, 10-15 caps, 100+ páginas DOCX
6. **SEMPRE:** Estilo Spielberg (maravilha, crianças heróis, emoção)
7. **SEMPRE:** Linguagem clara para tradução (sem gírias regionais)
8. **DEPOIS:** Gerar 6 relatórios de validação MD
9. **ANTES DE PUBLICAR:** Traduzir 4 idiomas + QA GPT-5
10. **PUBLICAR:** Simultaneamente em 5 mercados

**Seguindo este documento = Livros com padrão de qualidade que triplicam vendas!**

---

**FIM DO DOCUMENTO**

Este é o padrão oficial. Qualquer desvio deve ser justificado e aprovado.
