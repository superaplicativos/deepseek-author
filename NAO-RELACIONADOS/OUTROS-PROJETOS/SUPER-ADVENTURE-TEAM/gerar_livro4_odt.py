#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerador de ODT — Turma da Aventura: Nova Geração (Livro 4 como Livro 1)

Cria um arquivo ODT otimizado para futura conversão em EPUB, com:
- Metadados completos (título, autor, idioma, assunto)
- Capa (título e subtítulo)
- Índice automático (sumário baseado em níveis de título)
- Estrutura dos 10 capítulos e 3 tópicos por capítulo (Livro 4)
- Conteúdo integral gerado automaticamente por tópico seguindo a diretriz

Objetivo de extensão: mínimo ~1.700 palavras por tópico (≈ 51.000 palavras totais)
Estilos: Corpo 13.5pt para favorecer contagem de páginas (≥ 100 páginas)

Saída: SUPER ADVENTURE TEAM/LIVRO4_TRIANGULO_BERMUDAS.odt
"""

import os
import re
import random
from datetime import datetime

from odf.opendocument import OpenDocumentText
from odf.text import P, H, IndexTitle, TableOfContent, TableOfContentSource
from odf.style import Style, TextProperties, ParagraphProperties
from odf.meta import InitialCreator, Keyword
from odf.dc import Title, Subject, Creator, Language


# -------------------------------
# Metadados e estilos
# -------------------------------
def add_meta(doc, title, author, subject, lang, keywords=None):
    doc.meta.addElement(Title(text=title))
    doc.meta.addElement(InitialCreator(text=author))
    doc.meta.addElement(Creator(text=author))
    doc.meta.addElement(Subject(text=subject))
    doc.meta.addElement(Language(text=lang))
    if keywords:
        for kw in keywords:
            doc.meta.addElement(Keyword(text=kw))


def define_styles(doc):
    # Título da capa
    st_title = Style(name="CapaTitulo", family="paragraph")
    st_title.addElement(TextProperties(fontweight="bold", fontsize="26pt"))
    st_title.addElement(ParagraphProperties(textalign="center", margintop="0.6cm", marginbottom="0.25cm"))
    doc.styles.addElement(st_title)

    # Subtítulo da capa
    st_subtitle = Style(name="CapaSubtitulo", family="paragraph")
    st_subtitle.addElement(TextProperties(fontsize="15pt"))
    st_subtitle.addElement(ParagraphProperties(textalign="center", margintop="0.2cm", marginbottom="0.45cm"))
    doc.styles.addElement(st_subtitle)

    # Parágrafo padrão — corpo do texto
    st_body = Style(name="Corpo", family="paragraph")
    st_body.addElement(TextProperties(fontsize="13.5pt"))
    # Nota: ODF usa fo:line-height, aqui representado como lineheight em ParagraphProperties.
    # Algumas versões do odfpy podem ignorar. Em todo caso, o tamanho da fonte ajuda a aumentar páginas.
    st_body.addElement(ParagraphProperties(margintop="0.16cm", marginbottom="0.16cm"))
    doc.styles.addElement(st_body)

    # Heading 1 (Capítulos)
    h1 = Style(name="Heading 1", displayname="Heading 1", family="paragraph")
    h1.addElement(TextProperties(fontweight="bold", fontsize="17pt"))
    h1.addElement(ParagraphProperties(margintop="0.55cm", marginbottom="0.25cm"))
    doc.styles.addElement(h1)

    # Heading 2 (Tópicos)
    h2 = Style(name="Heading 2", displayname="Heading 2", family="paragraph")
    h2.addElement(TextProperties(fontweight="bold", fontsize="14pt"))
    h2.addElement(ParagraphProperties(margintop="0.40cm", marginbottom="0.18cm"))
    doc.styles.addElement(h2)

    # Diálogo (um leve destaque)
    st_dialog = Style(name="Dialogo", family="paragraph")
    st_dialog.addElement(TextProperties(fontsize="13.5pt"))
    st_dialog.addElement(ParagraphProperties(margintop="0.10cm", marginbottom="0.10cm", textindent="0.3cm"))
    doc.styles.addElement(st_dialog)

    return {
        "title": st_title,
        "subtitle": st_subtitle,
        "body": st_body,
        "h1": h1,
        "h2": h2,
        "dialog": st_dialog,
    }


def add_title_page(doc, styles, main_title, sub_title, author):
    doc.text.addElement(P(stylename=styles["title"], text=main_title))
    doc.text.addElement(P(stylename=styles["subtitle"], text=sub_title))
    doc.text.addElement(P(stylename=styles["subtitle"], text=f"Autor: {author}"))
    # Espaço
    doc.text.addElement(P(stylename=styles["body"], text=""))
    doc.text.addElement(P(stylename=styles["body"], text="Edição automática gerada em " + datetime.now().strftime("%d/%m/%Y, %H:%M")))


def add_table_of_contents(doc):
    toc = TableOfContent(name="Sumário", protected="true")
    # Fonte: até nível 2 (Capítulos e Tópicos)
    toc_source = TableOfContentSource(outlinelevel=2)
    toc.addElement(toc_source)
    doc.text.addElement(toc)


# -------------------------------
# Dados do Livro 4 — Mistério do Triângulo
# -------------------------------
CHAPTERS_DATA = [
    ("O Portal Dimensional", [
        "Anomalia Detectada",
        "Chegada ao Oceano",
        "Dentro da Anomalia",
    ]),
    ("Náufragos Fantasmas", [
        "Encontro com o Almirante",
        "Investigação dos Náufragos",
        "Fuga do Navio",
    ]),
    ("Tempestade Misteriosa", [
        "Fúria dos Elementos",
        "Refúgio Temporário",
        "Plano de Escape",
    ]),
    ("Dimensão Paralela", [
        "Mergulho no Vórtice",
        "Labirinto Temporal",
        "Verdade Revelada",
    ]),
    ("Mistério dos Relógios", [
        "Enigmas Temporais",
        "Corrida Contra o Tempo",
        "Sincronização",
    ]),
    ("Batalha Naval", [
        "Confronto nas Águas",
        "Poderes Aquáticos",
        "Aliança Inesperada",
    ]),
    ("Retorno ao Presente", [
        "Busca pela Saída",
        "Despedidas Dimensionais",
        "Salto de Fé",
    ]),
    ("Segredo dos Náufragos", [
        "Retorno Estranho",
        "Investigação Final",
        "Resgate Impossível",
    ]),
    ("Nova Ameaça", [
        "Sinais Perturbadores",
        "Preparação",
        "União do Grupo",
    ]),
    ("Oceano em Paz", [
        "Fechamento dos Portais",
        "Reconhecimento e Reflexão",
        "Eco Dimensional",
    ]),
]


# -------------------------------
# Gerador de texto cinematográfico
# -------------------------------
CHARACTERS = [
    "Will", "Mia", "Leo", "Sophie", "Max", "Jimmy", "Íris"
]

VISUAIS_MAR = [
    "névoa azul-esverdeada cobrindo o horizonte",
    "ondas que respiram como criaturas vivas",
    "reflexos de múltiplos sóis fragmentando o mar",
    "luz trêmula que dança em escamas invisíveis",
    "vento salgado que traz sussurros antigos",
]

SONS_MAR = [
    "estalos de madeira molhada",
    "murmúrio distante de canhões fantasmas",
    "canto grave de baleias de outra realidade",
    "tilintar de cordas tensionadas",
    "eco metálico vindo do nada",
]

EMOCOES = [
    "coragem hesitante",
    "amizade que se fortalece no silêncio",
    "medo transformado em curiosidade",
    "humor que desafia a tempestade",
    "vulnerabilidade que revela força",
]

def rand_choice(seq):
    return seq[random.randint(0, len(seq)-1)]


def build_sentence(scene_ctx, focus=None):
    base = f"{rand_choice(['A câmera imaginária acompanha', 'Vemos em travelling', 'Um plano-sequência revela'])} {rand_choice(VISUAIS_MAR)}; "
    base += f"{rand_choice(['o som mistura', 'o ambiente respira', 'o ar carrega'])} {rand_choice(SONS_MAR)}. "
    if focus:
        base += f"{focus} reage com {rand_choice(EMOCOES)}. "
    else:
        base += f"A equipe troca olhares e avança. "
    return base


def build_dialog(character, line_type="neutro"):
    # Falas curtas em estilo natural
    if character == "Will":
        lines = {
            "lider": "Cada aventura começa com uma pergunta.",
            "neutro": "Vamos decidir juntos e agir com calma.",
        }
    elif character == "Mia":
        lines = {
            "lider": "Tecnomorfose ativa — vou ler esse sistema.",
            "neutro": "Tenho um gadget que pode nos dar tempo.",
        }
    elif character == "Leo":
        lines = {
            "lider": "Se vier luta, eu protejo todo mundo.",
            "neutro": "Meu corpo está pronto para se adaptar.",
        }
    elif character == "Sophie":
        lines = {
            "lider": "Probabilidades apontam uma rota de menor risco.",
            "neutro": "Isso não é aleatório; há padrão escondido.",
        }
    elif character == "Max":
        lines = {
            "lider": "Os animais estão nervosos... algo não está certo.",
            "neutro": "Se um tubarão vier, eu converso com ele.",
        }
    elif character == "Jimmy":
        lines = {
            "lider": "Sentindo cheiro de ozônio — perigo vindo.",
            "neutro": "Latido baixo: atenção total!",
        }
    else:  # Íris
        lines = {
            "lider": "Holograma ativo: mapa dimensional atualizado.",
            "neutro": "Emoção detectada: esperança e foco.",
        }
    return f"— {lines.get(line_type, lines['neutro'])} ({character})"


def parse_directive_txt(txt_path):
    # Extrai capítulos, tópicos, cenário, eventos e gancho do arquivo 2.txt
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = [l.rstrip('\n') for l in f]

    chapters = []
    current_chapter = None
    current_topic = None
    mode = None

    chap_re = re.compile(r"^📖\s*CAPÍTULO\s*(\d+):\s*(.+)$", re.IGNORECASE)
    topic_re = re.compile(r"^TÓPICO\s*(\d+):\s*(.+)$", re.IGNORECASE)

    def commit_topic():
        nonlocal current_chapter, current_topic
        if current_chapter and current_topic:
            current_chapter['topics'].append(current_topic)
            current_topic = None

    def commit_chapter():
        nonlocal current_chapter
        if current_chapter:
            chapters.append(current_chapter)
            current_chapter = None

    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        # Ignora linhas de controle/checklists que não pertencem à narrativa
        if (line.startswith('Claude Sonnet') or
            line.lower().startswith('continue') or
            line.startswith('✅') or line.startswith('📊') or line.startswith('📚') or
            line.upper().startswith('ESTRUTURA COMPLETA') or
            line.upper().startswith('DESENVOLVIMENTO DOS PERSONAGENS') or
            line.upper().startswith('PROGRESSÃO DE PODERES') or
            line.upper().startswith('CHECKLIST') or
            line.startswith('🚀')):
            continue
        mchap = chap_re.match(line)
        if mchap:
            commit_topic()
            commit_chapter()
            current_chapter = {
                'number': int(mchap.group(1)),
                'title': mchap.group(2).strip(),
                'topics': []
            }
            mode = None
            continue
        mtop = topic_re.match(line)
        if mtop:
            commit_topic()
            current_topic = {
                'number': int(mtop.group(1)),
                'title': mtop.group(2).strip(),
                'scenario': '',
                'events': [],
                'hook': ''
            }
            mode = None
            continue
        if current_topic is not None:
            if line.lower().startswith('cenário:'):
                current_topic['scenario'] = line.split(':', 1)[1].strip()
                mode = None
                continue
            if line.lower().startswith('acontecimentos'):
                mode = 'events'
                continue
            if line.lower().startswith('gancho:'):
                current_topic['hook'] = line.split(':', 1)[1].strip()
                mode = None
                continue
            if mode == 'events':
                if line.startswith('📖') or line.startswith('TÓPICO'):
                    mode = None
                    continue
                # Filtra marcadores de checklist caso tenham caído dentro da seção
                if (line.startswith('✅') or line.startswith('📊') or line.startswith('📚') or
                    line.upper().startswith('ESTRUTURA') or line.upper().startswith('CHECKLIST')):
                    continue
                current_topic['events'].append(line)

    commit_topic()
    commit_chapter()
    return chapters


def sanitize_event_text(event: str) -> str:
    import re
    e = event.strip()
    # Remove marcadores visuais e rótulos técnicos
    e = e.replace('✅', '').strip()
    e = re.sub(r'\(\s*\d+[\.,]?\d*\+?\s*palavras\s*\)', '', e, flags=re.I)
    e = re.sub(r'\bCapítulo\s*\d+[^:]*:', '', e, flags=re.I)
    e = re.sub(r'\bTópico\s*\d+[^:]*:', '', e, flags=re.I)
    # Converte "Momento \"...\" -" em descrição narrativa neutra
    m = re.search(r'Momento\s*"?([^"\-:]+)"?\s*[-—:]?', e, flags=re.I)
    if m:
        label = m.group(1).strip().lower()
        mapping = {
            'e.t.': 'um momento de ternura e conexão profunda',
            'jurassic park': 'um momento de maravilha diante do desconhecido',
            'indiana jones': 'um momento de fuga audaciosa e engenhosidade',
            'de volta para o futuro': 'um momento de engenhosidade criativa sob pressão',
            'goonies': 'um momento de amizade corajosa em grupo',
            'homem-aranha': 'um momento de responsabilidade que acompanha o poder',
            'vingadores': 'um momento de sincronia perfeita da equipe',
        }
        phrase = mapping.get(label, 'um momento emblemático para a equipe')
        e = re.sub(r'Momento\s*"?([^"\-:]+)"?\s*[-—:]?', phrase + ' — ', e, flags=re.I)
        e = e.strip('— ').strip()
    return e

def expand_event_to_paragraphs(event, scenario_hint=None):
    paragraphs = []
    who = []
    for name in CHARACTERS:
        if name.lower() in event.lower():
            who.append(name)
    base = sanitize_event_text(event)
    paragraphs.append(
        f"{random.choice(['De perto,', 'De longe,', 'Com leve panorâmica,'])} {base}. "
        f"{random.choice(['O mar parece escutar.', 'O ar muda de temperatura.', 'A névoa responde como se tivesse vontade própria.'])}"
    )
    paragraphs.append(
        f"{build_sentence({}, focus=who[0] if who else None)}"
    )
    if who:
        for name in who[:2]:
            paragraphs.append(build_dialog(name, 'neutro'))
    else:
        paragraphs.append(build_dialog('Will', 'neutro'))
    paragraphs.append(
        "Poderes e talentos entram em cena: Will estabiliza o ambiente com energia cinética; "
        "Mia avalia leituras impossíveis; Leo adapta o corpo; Sophie calcula variáveis; Max acalma a vida marinha; "
        "Jimmy fareja perigo; Íris projeta trilhas luminosas entre realidades."
    )
    return paragraphs


def generate_paragraphs_for_section(section, chapter_title, topic_title, target_words, styles):
    # Gera parágrafos ricos com variação visual e diálogos
    paragraphs = []
    words = 0
    # Abertura: mais visual
    if section == "abertura":
        while words < target_words:
            s = build_sentence({"chapter": chapter_title, "topic": topic_title}, focus=rand_choice(CHARACTERS))
            paragraphs.append((styles["body"], s))
            words += len(s.split())
        # Um diálogo introdutório
        d = build_dialog("Will", "lider")
        paragraphs.append((styles["dialog"], d))
        words += len(d.split())
    # Desenvolvimento: alterna ação e diálogo
    elif section == "desenvolvimento":
        toggle = True
        while words < target_words:
            if toggle:
                # Ação com uso de poderes
                action = (
                    f"{build_sentence({'chapter': chapter_title, 'topic': topic_title}, focus=rand_choice(CHARACTERS))} "
                    f"Will canaliza um campo azul translúcido; Mia decifra um protocolo impossível; Leo ajusta o corpo e endurece a pele; "
                    f"Sophie calcula rotas com olhos prateados; Max acalma criaturas marinhas; Jimmy alerta com precisão; Íris projeta luzes guiando o grupo."
                )
                paragraphs.append((styles["body"], action))
                words += len(action.split())
            else:
                # Diálogos múltiplos
                di = [
                    build_dialog("Sophie", "neutro"),
                    build_dialog("Mia", "neutro"),
                    build_dialog("Leo", "neutro"),
                    build_dialog("Max", "neutro"),
                    build_dialog("Íris", "neutro"),
                    build_dialog("Jimmy", "neutro"),
                ]
                for d in di:
                    paragraphs.append((styles["dialog"], d))
                    words += len(d.split())
            toggle = not toggle
        # Momento de humor
        humor = "— Se o mar tiver senha, eu digito 'peixe123' e espero o melhor. (Max)"
        paragraphs.append((styles["dialog"], humor))
    # Progressão: revelação e decisão
    else:
        while words < target_words:
            prog = (
                f"{build_sentence({'chapter': chapter_title, 'topic': topic_title})} "
                f"Sophie revela uma pista oculta; Will decide com calma; Mia prepara um instrumento novo; Leo enfrenta o desconhecido; "
                f"Max encontra beleza no caos; Jimmy encontra trilhas invisíveis; Íris sente algo novo — um vislumbre de emoção autêntica."
            )
            paragraphs.append((styles["body"], prog))
            words += len(prog.split())
        gancho = f"— Gancho: algo se move na névoa — o próximo passo chama. (Íris)"
        paragraphs.append((styles["dialog"], gancho))
    return paragraphs


def add_paragraphs(doc, paragraphs):
    for sty, text in paragraphs:
        doc.text.addElement(P(stylename=sty, text=text))


# -------------------------------
# Construção do documento
# -------------------------------
def build_book(doc, styles, directive_path):
    random.seed(42)
    chapters = parse_directive_txt(directive_path)
    for chapter in chapters:
        doc.text.addElement(H(outlinelevel=1, stylename=styles['h1'], text=f"Capítulo {chapter['number']}: {chapter['title']}"))
        for topic in chapter['topics']:
            # Subtítulo sem o rótulo técnico "Tópico X"
            doc.text.addElement(H(outlinelevel=2, stylename=styles['h2'], text=f"{topic['title']}"))
            # Gerar conteúdo criativo baseado nos eventos da diretriz
            paragraphs = []
            # Abertura
            abertura_bits = [
                # Usa o cenário diretamente como frase cinematográfica, sem qualquer rótulo
                f"{topic['scenario']}.",
                build_sentence({'chapter': chapter['title'], 'topic': topic['title']}, focus=random.choice(CHARACTERS)),
                build_dialog('Will', 'lider'),
            ]
            for s in abertura_bits:
                paragraphs.append((styles['body'] if not s.startswith('— ') else styles['dialog'], s))
            # Desenvolvimento
            for ev in topic['events']:
                for para in expand_event_to_paragraphs(ev, scenario_hint=topic['scenario']):
                    paragraphs.append((styles['body'] if not para.startswith('— ') else styles['dialog'], para))
            # Progressão e gancho
            paragraphs.append((styles['body'], "A tensão cresce conforme probabilidades dançam diante dos olhos de Sophie. Will mantém a calma do grupo."))
            paragraphs.append((styles['body'], "Íris integra leituras e emoções incipientes; Mia encaixa o último detalhe técnico; Leo respira fundo e aceita o desafio."))
            hook = topic.get('hook', '').strip()
            # Gancho sem rótulo, como frase final do tópico
            paragraphs.append((styles['body'], hook if hook else "Algo se move na névoa — o próximo passo chama."))
            add_paragraphs(doc, paragraphs)


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    directive_path = os.path.join(base_dir, "2.txt")
    output_path = os.path.join(base_dir, "LIVRO_4_MISTERIO_DO_TRIANGULO_DAS_BERMUDAS.odt")

    # Documento
    doc = OpenDocumentText()

    # Metadados
    titulo = "Turma da Aventura: Nova Geração — Livro 4: Mistério do Triângulo das Bermudas"
    autor = "Turma da Aventura"
    assunto = "Aventura cinematográfica infantojuvenil: mistério histórico, múltiplas realidades, amizade e coragem"
    idioma = "pt-BR"
    keywords = ["Aventura", "Infantil", "Tecnologia", "Triângulo das Bermudas", "Dimensões", "Equipe"]
    add_meta(doc, titulo, autor, assunto, idioma, keywords)

    # Estilos
    styles = define_styles(doc)

    # Capa
    add_title_page(
        doc,
        styles,
        main_title=titulo,
        sub_title="Livro completo com estrutura otimizada para EPUB (≥100 páginas)",
        author=autor,
    )

    # Índice
    add_table_of_contents(doc)

    # Corpo do livro
    build_book(doc, styles, directive_path)

    # Salvar
    doc.save(output_path)
    print(f"✅ ODT gerado: {output_path}")


if __name__ == "__main__":
    main()