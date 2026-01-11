#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SCRIPT DE PESQUISA DE MERCADO PARA NOVAS SÉRIES
Turma da Aventura - Market Intelligence

Este script auxilia na pesquisa de mercado para planejar novos livros
das séries: INVENÇÕES, MISTÉRIOS, CIÊNCIA

Uso:
    python pesquisa_novas_series.py [serie]

    Onde [serie] pode ser: invencoes, misterios, ciencia, ou all
"""

import sys
from datetime import datetime

# Definição das séries e suas características
SERIES = {
    "invencoes": {
        "nome": "SÉRIE INVENÇÕES",
        "tema": "Grandes invenções que mudaram a humanidade",
        "protagonistas": "MIA (inventora) + WILL (tecnologia)",
        "foco_educacional": "STEM, história da tecnologia, engenharia",
        "keywords_amazon": [
            "inventions for kids",
            "STEM books children",
            "history of technology kids",
            "famous inventors",
            "engineering for children",
            "science books 8-12",
            "wheel invention",
            "printing press history",
            "electricity for kids",
            "airplane invention"
        ],
        "topicos_sugeridos": [
            "A Roda - primeira grande invenção",
            "A Imprensa de Gutenberg - democratização do conhecimento",
            "A Lâmpada de Edison - iluminando o mundo",
            "O Avião dos Irmãos Wright - conquistando o céu",
            "O Telefone de Graham Bell - conectando pessoas",
            "A Internet - revolução digital",
            "Vacinas - salvando milhões de vidas"
        ],
        "diretriz_path": "D:\\TRAE-PROJETOS\\livro1\\BIZANTINO\\DIRETRIZES\\SERIE-INVENCOES.txt"
    },

    "misterios": {
        "nome": "SÉRIE MISTÉRIOS",
        "tema": "Mistérios históricos não resolvidos",
        "protagonistas": "SOPHIE (detetive) com papel central",
        "foco_educacional": "Pensamento crítico, método investigativo, história",
        "keywords_amazon": [
            "mysteries for kids",
            "unsolved mysteries children",
            "detective stories 8-12",
            "Stonehenge for kids",
            "Bermuda Triangle children",
            "Atlantis mystery",
            "historical mysteries kids",
            "ancient mysteries children",
            "archaeology for kids",
            "treasure hunt books"
        ],
        "topicos_sugeridos": [
            "Atlântida - cidade perdida mítica",
            "Triângulo das Bermudas - desaparecimentos misteriosos",
            "Stonehenge - quem construiu e por quê?",
            "Linhas de Nazca - geoglifos gigantes",
            "Maldição de Tutancâmon - real ou coincidência?",
            "Monstro do Lago Ness - lenda ou realidade?",
            "Colônia Perdida de Roanoke"
        ],
        "diretriz_path": "D:\\TRAE-PROJETOS\\livro1\\BIZANTINO\\DIRETRIZES\\SERIE-MISTERIOS.txt"
    },

    "ciencia": {
        "nome": "SÉRIE CIÊNCIA",
        "tema": "Descobertas científicas que mudaram nossa compreensão do universo",
        "protagonistas": "MIA (inventora) + WILL (tecnologia) com Íris AI",
        "foco_educacional": "Ciência pura, método científico, biografias de cientistas",
        "keywords_amazon": [
            "science for kids",
            "famous scientists children",
            "scientific discoveries kids",
            "Newton for kids",
            "Darwin evolution children",
            "DNA for kids",
            "Marie Curie children",
            "gravity for kids",
            "biology books 8-12",
            "physics for children"
        ],
        "topicos_sugeridos": [
            "Gravidade (Isaac Newton) - lei universal",
            "DNA (Watson, Crick, Rosalind Franklin) - código da vida",
            "Evolução (Charles Darwin) - seleção natural",
            "Radioatividade (Marie Curie) - primeira mulher Nobel",
            "Heliocentrismo (Copérnico, Galileu) - Terra gira ao redor do Sol",
            "Eletricidade (Benjamin Franklin, Tesla)",
            "Teoria dos Germes (Pasteur) - micro-organismos",
            "Big Bang - origem do universo"
        ],
        "diretriz_path": "D:\\TRAE-PROJETOS\\livro1\\BIZANTINO\\DIRETRIZES\\SERIE-CIENCIA.txt"
    }
}

MERCADOS = {
    "USA": "amazon.com",
    "Brasil": "amazon.com.br",
    "Alemanha": "amazon.de",
    "Reino Unido": "amazon.co.uk",
    "Espanha": "amazon.es"
}


def print_header(title):
    """Imprime cabeçalho formatado"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")


def print_research_template(serie_key):
    """Imprime template de pesquisa para uma série específica"""
    serie = SERIES[serie_key]

    print_header(f"PESQUISA DE MERCADO: {serie['nome']}")

    print(f"📚 TEMA: {serie['tema']}")
    print(f"👥 PROTAGONISTAS: {serie['protagonistas']}")
    print(f"🎓 FOCO EDUCACIONAL: {serie['foco_educacional']}")
    print(f"📁 DIRETRIZ: {serie['diretriz_path']}")

    print("\n" + "-" * 80)
    print("🔍 PALAVRAS-CHAVE PARA PESQUISA NA AMAZON")
    print("-" * 80)
    for i, keyword in enumerate(serie['keywords_amazon'], 1):
        print(f"  {i:2d}. \"{keyword}\"")

    print("\n" + "-" * 80)
    print("📖 TÓPICOS SUGERIDOS (Alta Prioridade)")
    print("-" * 80)
    for i, topico in enumerate(serie['topicos_sugeridos'], 1):
        print(f"  {i}. {topico}")

    print("\n" + "-" * 80)
    print("🌍 MERCADOS ALVO PARA PESQUISA")
    print("-" * 80)
    for mercado, url in MERCADOS.items():
        print(f"  • {mercado:15s} → {url}")

    print("\n" + "-" * 80)
    print("📋 ROTEIRO DE PESQUISA")
    print("-" * 80)
    print("""
Para cada mercado (USA, Brasil, Alemanha, UK, Espanha):

1. PESQUISA DE BESTSELLERS
   - Acesse a Amazon do mercado
   - Pesquise cada palavra-chave da lista acima
   - Identifique os top 10-20 livros mais vendidos (8-12 anos)
   - Anote títulos, temas, formatos que vendem bem

2. ANÁLISE DE TENDÊNCIAS
   - Quais tópicos aparecem repetidamente?
   - Quais invenções/mistérios/descobertas estão em alta?
   - Há padrões regionais? (Ex: Alemanha prefere ciência, USA prefere mistério?)
   - Há eventos culturais/aniversários relevantes? (Ex: centenário de descoberta)

3. ANÁLISE DE CONCORRÊNCIA
   - Séries similares existentes (Magic Tree House, Who Was?, etc.)
   - O que eles fazem bem?
   - Que lacunas podemos preencher?
   - Como podemos diferenciar?

4. KEYWORDS E SEO
   - Quais keywords têm mais resultados/competição?
   - Quais keywords têm menos competição mas bom volume?
   - Variações regionais de keywords (PT, EN, DE, ES)?

5. ANÁLISE DE REVIEWS
   - O que leitores/pais elogiam em livros similares?
   - O que criticam?
   - Que elementos são "must have"?
   - Que problemas podemos evitar?
    """)

    print("\n" + "-" * 80)
    print("📝 TEMPLATE DE RELATÓRIO")
    print("-" * 80)
    print(f"""
Salve suas descobertas em:
D:\\TRAE-PROJETOS\\livro1\\BIZANTINO\\INTELIGENCIA-DE-MERCADO\\RELATORIO-{serie_key.upper()}-{datetime.now().strftime('%Y%m%d')}.md

Estrutura sugerida do relatório:

# RELATÓRIO DE PESQUISA: {serie['nome']}
Data: {datetime.now().strftime('%Y-%m-%d')}

## 1. RESUMO EXECUTIVO
- Top 3 tópicos recomendados com justificativa
- Insights principais da pesquisa

## 2. ANÁLISE POR MERCADO

### USA (amazon.com)
- Bestsellers encontrados: [listar]
- Tópicos em alta: [listar]
- Keywords mais efetivas: [listar]
- Insights culturais: [descrever]

### Brasil (amazon.com.br)
[Repetir estrutura]

### Alemanha (amazon.de)
[Repetir estrutura]

### Reino Unido (amazon.co.uk)
[Repetir estrutura]

### Espanha (amazon.es)
[Repetir estrutura]

## 3. TÓPICOS RECOMENDADOS (Prioridade)

### Tópico 1: [Nome]
- **Justificativa:** Por que este tópico vende bem em [mercados]
- **Keywords principais:** [listar]
- **Competição:** Alta/Média/Baixa
- **Oportunidade:** [descrever]
- **Conexão com série:** Como se encaixa em {serie['nome']}

[Repetir para 3-5 tópicos]

## 4. ANÁLISE DE CONCORRÊNCIA
- Séries similares: [listar]
- Pontos fortes dos concorrentes: [listar]
- Lacunas de mercado: [descrever]
- Nossa diferenciação: [estratégia]

## 5. ESTRATÉGIA DE KEYWORDS
- Keywords de alta prioridade: [PT, EN, DE, ES]
- Keywords de nicho/oportunidade: [listar]
- Keywords a evitar (muito competitivas): [listar]

## 6. RECOMENDAÇÕES FINAIS
- Ordem de produção sugerida (Livros 1-5)
- Timing de lançamento (considerar eventos, aniversários)
- Adaptações regionais necessárias

## 7. PRÓXIMOS PASSOS
- [ ] Validar tópicos com análise Gemini Deep Research
- [ ] Atualizar DIRETRIZES/SERIE-{serie_key.upper()}.txt com descobertas
- [ ] Planejar cronograma de produção
    """)

    print("\n" + "-" * 80)
    print("🤖 INTEGRAÇÃO COM GEMINI DEEP RESEARCH")
    print("-" * 80)
    print(f"""
Para validação aprofundada, use o Gemini Deep Research com este prompt:

---
Conduza uma pesquisa profunda sobre as melhores [invenções/mistérios/descobertas científicas]
para livros infantis (8-12 anos) que vendem bem na Amazon em 2026.

Contexto:
- Série: {serie['nome']}
- Tema: {serie['tema']}
- Público: Crianças 8-12 anos (foco em 10-12 anos)
- Mercados: USA, Brasil, Alemanha, Reino Unido, Espanha
- Publicação: Simultânea em português, inglês, alemão, espanhol

Analise:
1. Trending topics em cada um dos 5 mercados Amazon
2. Tópicos evergreen que vendem consistentemente
3. Eventos/aniversários 2026-2027 que podemos aproveitar
4. Lacunas de mercado (tópicos pouco explorados mas com potencial)
5. Keywords de alta performance (SEO Amazon)

Foco especial em:
{chr(10).join(f'- {t}' for t in serie['topicos_sugeridos'][:5])}

Forneça:
- Top 5 tópicos recomendados (ordem de prioridade)
- Justificativa com dados de cada mercado
- Keywords principais (PT, EN, DE, ES)
- Análise de competição para cada tópico
- Estratégia de diferenciação
---
    """)


def main():
    """Função principal"""
    if len(sys.argv) < 2:
        print_header("PESQUISA DE MERCADO - NOVAS SÉRIES TURMA DA AVENTURA")
        print("Uso: python pesquisa_novas_series.py [serie]")
        print("\nSéries disponíveis:")
        print("  • invencoes    - Série Invenções (Roda, Imprensa, Eletricidade, etc.)")
        print("  • misterios    - Série Mistérios (Stonehenge, Bermuda, Atlântida, etc.)")
        print("  • ciencia      - Série Ciência (Newton, Darwin, DNA, etc.)")
        print("  • all          - Gerar templates para todas as séries")
        print("\nExemplo:")
        print("  python pesquisa_novas_series.py invencoes")
        print("  python pesquisa_novas_series.py all")
        return

    serie_arg = sys.argv[1].lower()

    if serie_arg == "all":
        for serie_key in SERIES.keys():
            print_research_template(serie_key)
            print("\n\n" + "🔸" * 40 + "\n")

        print_header("PRÓXIMOS PASSOS")
        print("""
1. Execute pesquisas para cada série usando os templates acima
2. Salve relatórios em INTELIGENCIA-DE-MERCADO/RELATORIO-[SERIE]-[DATA].md
3. Use Gemini Deep Research para validação aprofundada
4. Atualize as diretrizes em DIRETRIZES/SERIE-*.txt com descobertas
5. Defina cronograma de produção (qual série produzir primeiro?)
6. Para cada série, defina ordem dos livros (quais tópicos primeiro?)
        """)

    elif serie_arg in SERIES:
        print_research_template(serie_arg)
    else:
        print(f"❌ Série '{serie_arg}' não reconhecida.")
        print("Séries válidas: invencoes, misterios, ciencia, all")
        sys.exit(1)


if __name__ == "__main__":
    main()
