#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerador de ODT — Turma da Aventura: Nova Geração (Livro 1)

Cria um arquivo ODT otimizado para futura conversão em EPUB, com:
- Metadados completos (título, autor, idioma, assunto)
- Capa (título e subtítulo)
- Índice automático (sumário baseado em níveis de título)
- Estrutura dos 10 capítulos e 3 tópicos por capítulo
- Conteúdo integral do Capítulo 1, Tópico 1 (extenso e cinematográfico)

Saída: SUPER ADVENTURE TEAM/arquivo.odt
"""

import os
from datetime import datetime

from odf.opendocument import OpenDocumentText
from odf.text import P, H, IndexTitle, TableOfContent, TableOfContentSource
from odf.style import Style, TextProperties, ParagraphProperties
from odf.meta import Title, InitialCreator, Creator, Keyword, Language, Subject


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
    st_title.addElement(TextProperties(fontweight="bold", fontsize="24pt"))
    st_title.addElement(ParagraphProperties(textalign="center", margintop="0.5cm", marginbottom="0.2cm"))
    doc.styles.addElement(st_title)

    # Subtítulo da capa
    st_subtitle = Style(name="CapaSubtitulo", family="paragraph")
    st_subtitle.addElement(TextProperties(fontsize="14pt"))
    st_subtitle.addElement(ParagraphProperties(textalign="center", margintop="0.2cm", marginbottom="0.4cm"))
    doc.styles.addElement(st_subtitle)

    # Parágrafo padrão
    st_body = Style(name="Corpo", family="paragraph")
    st_body.addElement(TextProperties(fontsize="11pt"))
    st_body.addElement(ParagraphProperties(margintop="0.15cm", marginbottom="0.15cm"))
    doc.styles.addElement(st_body)

    # Heading 1 (Capítulos) — compatível com ToC
    h1 = Style(name="Heading 1", displayname="Heading 1", family="paragraph")
    h1.addElement(TextProperties(fontweight="bold", fontsize="16pt"))
    h1.addElement(ParagraphProperties(margintop="0.5cm", marginbottom="0.2cm"))
    doc.styles.addElement(h1)

    # Heading 2 (Tópicos) — compatível com ToC
    h2 = Style(name="Heading 2", displayname="Heading 2", family="paragraph")
    h2.addElement(TextProperties(fontweight="bold", fontsize="13pt"))
    h2.addElement(ParagraphProperties(margintop="0.35cm", marginbottom="0.15cm"))
    doc.styles.addElement(h2)

    return {
        "title": st_title,
        "subtitle": st_subtitle,
        "body": st_body,
        "h1": h1,
        "h2": h2,
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
    toc.addElement(IndexTitle(P(text="Índice")))
    # Fonte: até nível 2 (Capítulos e Tópicos)
    toc_source = TableOfContentSource(outlinelevel=2)
    toc.addElement(toc_source)
    doc.text.addElement(toc)


def add_paragraphs(doc, styles, text_block):
    # Adiciona parágrafos simples, dividindo por linhas em branco
    for raw_para in [p.strip() for p in text_block.split("\n\n") if p.strip()]:
        doc.text.addElement(P(stylename=styles["body"], text=raw_para))


def build_structure(doc, styles, chapters):
    # Insere toda a estrutura dos capítulos e tópicos
    for ci, (chap_title, topics) in enumerate(chapters, start=1):
        doc.text.addElement(H(outlinelevel=1, stylename=styles["h1"], text=f"Capítulo {ci}: {chap_title}"))
        for ti, topic_title in enumerate(topics, start=1):
            doc.text.addElement(H(outlinelevel=2, stylename=styles["h2"], text=f"Tópico {ti}: {topic_title}"))
            # Placeholder para conteúdos futuros
            doc.text.addElement(P(stylename=styles["body"], text="[Conteúdo detalhado a ser expandido]"))


def insert_chapter1_topic1(doc, styles):
    # Substitui o placeholder do primeiro tópico por conteúdo completo
    # Estrutura: Abertura (200+), Desenvolvimento (600+), Progressão (400+)
    abertura = (
        "O pátio da Escola Horizonte parecia um palco de cinema naquela manhã de céu limpo. A grama recém-cortada exalava um perfume úmido que flutuava com a brisa, enquanto o sol derramava um brilho dourado sobre as pedras do caminho. As sombras das árvores dançavam como figuras em movimento, recortando o chão com manchas ondulantes. Ao fundo, o prédio de tijolos com janelas altas refletia retângulos de luz, formando padrões que lembravam códigos secretos. O som distante de um apito de educação física misturava-se ao zumbido elétrico de lâmpadas que, por algum motivo, vibravam mais forte do que de costume. Will parou no centro do pátio, a mochila pendendo de um ombro, os olhos fixos em algo que só ele parecia escutar: um leve assobio no ar, como se a realidade estivesse chamando pelo seu nome. Ao lado dele, Mia ajustava um bracelete com tiras metálicas – um protótipo que ela jurava que faria qualquer celular antigo funcionar como novo. Leo alongava o pescoço e os braços, inquieto, pronto para correr. Sophie, com o caderno de investigação, anotava padrões de comportamento de professores e estudantes que passavam. Max, sentado no banco de madeira, chamava dois sabiás que respondiam com cantos curiosos, enquanto Jimmy Hendrix, o border collie, fazia um giro elegante e olhava para Will com olhos azuis que brilhavam de forma quase humana. Íris, projetada como um holograma azul acima do smartwatch de Mia, piscou com uma nuance emocional inédita: curiosidade."
        "\n\n"
        "A atmosfera tinha uma tensão doce, como o segundo antes da primeira nota de uma música. Uma nuvem fina passou diante do sol e, por meio segundo, tudo ficou mais frio, mais silencioso, mais... consciente. Will respirou fundo e sentiu o arrepio familiar que precedia o uso de seu poder: ondas azuis, ainda invisíveis, se comprimiam na palma de suas mãos. Ele não queria chamar atenção. Não ali. Mas algo no ar dizia que uma pergunta – a frase que sempre o guiava – estava prestes a encontrar sua resposta: cada aventura começa com uma pergunta. Qué aventura? O que estava prestes a acontecer? Íris sussurrou na pulseira: ‘Sinal elétrico irregular detectado nos postes do pátio. Probabilidade de evento incomum: 67%.’ Sophie ergueu os olhos, prata reluzindo, e murmurou: ‘As lâmpadas não estão falhando; estão sincronizadas... como se alguém as estivesse tocando com código.’"
    )

    desenvolvimento = (
        "Mia encostou dois dedos na base de uma das luminárias e, como se tivesse aberto uma porta invisível, linhas de circuito douradas floresceram em sua pele. ‘Tecnomorfose ativa’, disse com um sorriso rápido. ‘Tem algum firmware mandando uma sequência estranha... e tem assinatura humana. Não é vento, não é falha. Alguém está testando algo.’ Leo deu um passo à frente, os músculos do antebraço contraindo num reflexo quase imperceptível. ‘Se alguém está testando, a gente pode ser parte do teste sem pedir.’ Ele tentou brincar, mas os olhos denunciavam o instinto protetor. Max levantou o dedo, como quem faz uma pergunta em sala de aula: ‘Se for um teste, os pássaros estão nervosos. Eles estão cantando rápido demais.’ Os sabiás, de fato, batiam as asas em pequenos saltos coordenados. Jimmy soltou um latido curto e elegante – um som que só a equipe entendia como ‘atenção’. ‘Ar ao redor mudou’, comunicou com seu olhar intenso. ‘Cheiro de ozônio. Perigo leve.’ Will se posicionou na frente. ‘Pessoal, formem um semicírculo. Se for só uma brincadeira de hacker, a gente ri. Se não for... a gente testa nossos limites com cuidado.’"
        "\n\n"
        "Sophie fechou os olhos por um instante, respirou, e quando tornou a abrir, viu probabilidades sobrepostas como sobreposições de transparências: setas apontando para o poste central, uma curva de risco envolvendo o painel elétrico, e um fio de luz correndo pela calçada até a porta da administração. ‘Há 72% de chance de uma invasão tentando usar a rede elétrica como vetor,’ disse rapidamente. ‘Se alguém está mexendo na infra, provavelmente quer acesso à escola sem passar pela rede Wi-Fi oficial.’ Íris completou: ‘Tráfego incomum detectado vindo de um dispositivo próximo ao laboratório de informática. O sinal está fragmentado, mas tem assinatura do Cipher Syndicate.’ O nome pairou no ar como uma tempestade que ainda não começou. Mia bateu a mão no bracelete: ‘Ok, se for o Cipher Syndicate, isso é grande. Eles adoram usar infraestrutura silenciosa – coisas que ninguém suspeita.’ Leo fechou os punhos, e uma luz dourada passou pelos tendões, denunciando a preparação do corpo para adaptação. ‘Will, qual é o plano?’"
        "\n\n"
        "Will senti o campo de energia cinética estalar atrás dos olhos. ‘Primeiro, ninguém corre. Segundo, Mia, você fica no hardware. Sophie, analisa probabilidades de rotas. Íris, dá a gente uma visão holográfica do mapa da escola. Max, conversa com os pássaros e qualquer outro animal por perto. Jimmy, você fica em patrulha olfativa – qualquer cheiro de queimado ou metal aquecido, você avisa.’ O semicírculo se ajustou como se já fosse coreografado. Íris projetou um mapa holográfico azul acima da pulseira de Mia – linhas finas traçavam corredores, salas, cabos e pontos de acesso como se alguém tivesse desenhado a escola com luz. Mia deslizou o dedo pelo holograma. ‘O laboratório é o ponto de emissão. Estão tentando acoplar a energia de postes ao painel de rede. Se conseguirem, podem abrir uma porta fantasma dentro da intranet.’ Ela falou rápido, como sempre, mas cada palavra era cristalina. Sophie anotou sem olhar para o papel – a mão parecia saber escrever sozinha. ‘Há uma chance significativa de que o evento atual seja só um teste de intensidade... e que o ataque real venha depois que descobrirem a resposta da escola.’ Leo forçou um sorriso. ‘Então a gente dá uma resposta que eles não esperam.’"
        "\n\n"
        "Max ergueu a mão e os sabiás pousaram no corrimão ao lado. ‘Amigos, vocês sentem perigo?’, ele perguntou como quem conversa com colegas. Os pássaros tilintaram um canto curto, que Max traduziu: ‘Cheiro de metal quente. As lâmpadas estão com pressa. Há um barulho lá dentro.’ Jimmy inclinou a cabeça e, com um latido baixo, complementou: ‘Som de relés alternando. Não é normal.’ Will apertou a mandíbula. Seu poder pulsava, pedindo para ser usado, mas ele conhecia a limitação: se exagerasse cedo demais, o cansaço chegaria como um peso nas pernas e uma névoa na cabeça. ‘Tá. Vamos como equipe. Mia, você conduz. Íris, mantém a gente informados. Leo, você fica na retaguarda para proteção física. Sophie, guia por probabilidade de menor risco. Max, você e Jimmy escutam os animais e o ambiente.’"
        "\n\n"
        "Eles avançaram pelo corredor interno. O movimento de câmera imaginário seria um travelling suave, acompanhando os passos com o som dos tênis sobre o piso encerado. O corredor estava mais escuro do que deveria. Luzes piscavam, criando um ritmo estranho, como um coração que pulava batidas. Ao longe, portas fechadas refletiam pequenas faixas de luz. Sophie levantou o caderno e falou quase sem som: ‘Se chegarmos no laboratório por esse caminho, há 18% de chance de encontramos um dispositivo isca. Sugestão: contornar pela sala de teatro e entrar pelo fundo.’ Will acenou. ‘Muda rota. Sem pressa.’ Íris projetou setas no ar, e Mia sorriu. ‘Eu amo quando tecnologia vira arte.’ Leo passou o ombro pela parede, sentindo a textura fria que se tornava, aos poucos, um aviso: se precisasse de pele endurecida, seu corpo estava pronto para isso. Max encostou na porta, e ela vibrava como um instrumento afinando. ‘Tem alguém tocando a escola,’ ele disse, e Jimmy rosnou baixinho, sem agressividade – apenas consciência.")

    progressao = (
        "Quando chegaram ao fundo do laboratório, a cena era de suspense meticuloso. Cabos finos tinham sido puxados para fora de uma caixa técnica, e uma peça improvisada – uma espécie de ponte de metal com fios coloridos – estava acoplada ao quadro de energia como se fosse um parasita eficiente. Sobre a mesa, um pequeno dispositivo com LED azul pulsava em ritmo idêntico ao das lâmpadas do pátio. Mia aproximou a mão, e os circuitos dourados floresceram novamente. ‘Eu consigo ler o protocolo,’ disse, os olhos dançando sobre o LED. ‘É um handshake... que tenta se passar por manutenção. Se eu interromper errado, o sistema pode achar que foi pane e religar tudo em modo de segurança – o que daria ao atacante um minuto de janela perfeita.’ Sophie franziu a testa. ‘Há uma forma de desacoplar lentamente e simular um ruído ambiental. Mas o intervalo precisa ser exato. Íris, você consegue sincronizar as variações?’ Íris se manifestou em um holograma mais nítido, a voz com leveza emocional: ‘Consigo. Mas aviso: há uma chance de 41% de que o atacante perceba que alguém está respondendo com inteligência.’ Leo colocou a mão no ombro de Will. ‘Se perceber, eu seguro. Você direciona.’ Will respirou, sentindo seu poder percorrer as mãos como água vibrante, azul. ‘Vamos desarmar isso como quem dança.’"
        "\n\n"
        "Os próximos segundos pareceram um plano-sequência. Mia tocou o dispositivo e reduziu o pulso do LED em milissegundos; Íris ecoou o tempo em hologramas; Sophie contou em voz baixa: ‘Três, dois, um... parar... três, dois... reduzir...’ Will concentrou o campo energético, criando um casulo azul transparente em torno do quadro para amortecer qualquer pico súbito. Leo ajustou o corpo, a pele do antebraço densificando como se duas camadas de defesa se sobrepusessem, pronto para absorver impacto. Max, com as mãos espalmadas, sussurrou para uma família de andorinhas que, surpreendentemente, tinha feito ninho no duto: ‘Se algo fizer barulho alto, fiquem calmas. É só gente boa tentando consertar.’ Jimmy posicionou-se entre a porta e o grupo, os olhos brilhando em azul, atento a cheiros e vibrações. Por um momento, tudo se alinhou: luz, som, intenções. Então, o LED azul apagou com um estalo quase inaudível. Mia sorriu, e depois mordeu o lábio. ‘Ok... desligamos a ponte. Mas...’ Ela apontou para a tela de um notebook antigo que estava escondido atrás de uma pilha de revistas. Na tela, caracteres fluíam como chuva de código: alguém estava logado remotamente. ‘Eles já estão aqui,’ disse Sophie, fria. Will sentiu o cansaço roçar o fundo das costelas – o uso prolongado do escudo o cobrava. ‘Eu seguro mais um pouco,’ disse devagar. ‘Mas precisamos decidir: confrontar ou observar?’"
        "\n\n"
        "O grupo trocou olhares. Max quebrou a tensão com o humor que parecia nascer dele como primavera: ‘Se for um concurso de digitação, a gente perde. Eu ainda digito com dois dedos.’ Mia riu, leve. ‘Eu posso digitar por você com a minha pele.’ Leo deu um passo, os olhos dourados. ‘Se eles quiserem vir por aqui, eu fico na porta.’ Íris aumentou o holograma: um mapa com pontos vermelhos surgindo como estrelas perigosas. ‘Três possíveis acessos fantasma conectados à rede de manutenção. Um deles na sala da administração.’ Sophie fechou o caderno. ‘Decisão: precisamos ver o rosto do perigo. Se ficarmos nesta sala, só veremos reflexos. Sugestão: seguir o rastro até a administração e preparar um engodo. Algo que force o atacante a revelar a mão.’ Will assentiu. ‘Isto é uma missão. Primeira oficial. Sem dramatizar, sem correr. A gente vai juntos, e se falharmos, vamos aprender juntos.’ Ele olhou para a equipe, e por um segundo, o silêncio foi tão forte que parecia ter textura. ‘Cada aventura começa com uma pergunta,’ disse, agora com solenidade. ‘E a nossa é: quem está tocando a escola como se fosse um instrumento?’"
        "\n\n"
        "Sairam do laboratório em silêncio, o travelling agora acompanhando os passos pela lateral do corredor. Will reduziu o campo azul, sentindo o cansaço subir as pernas como areia. Ele sabia a limitação e não a esconderia do grupo. ‘Estou economizando energia,’ avisou, ‘mas posso criar escudo em emergência.’ Leo fez um gesto de ok; Sophie marcou mais duas probabilidades no caderno; Mia bateu levemente na pulseira e fez os circuitos desaparecerem. Max e Jimmy seguiram com atenção, e Íris manteve o holograma minimalista, como uma luz guia discreta. Ao virar a última esquina antes da administração, eles ouviram um som pequeno e agudo – como o drop de um arquivo enviado com sucesso. A porta da administração estava entreaberta. Mia levantou a mão, pedindo pausa. Sophie calculou. ‘Há 55% de chance de estarmos a ponto de entrar em uma armadilha de observação.’ Will inspirou. ‘Então, vamos construir nosso próprio labirinto. Íris, prepara uma rota alternativa e um eco do nosso sinal. Mia, cria um handshake falso – uma música que faça o atacante achar que a gente dança errado.’ Mia sorriu. ‘Adoro quando plano tem ritmo.’"
        "\n\n"
        "Eles se posicionaram. O próximo passo seria a primeira falha – porque aprender tem custo. Mas como toda boa história que respeita seus heróis, a falha não os quebraria: uniria. O gancho estava armado, delicado como a tensão de uma corda de violino. E, enquanto o sol se escondia por trás de uma nuvem e a escola respirava um suspiro elétrico, Will sentiu no fundo que, apesar do medo, eles estavam exatamente onde deveriam estar: no primeiro capítulo de uma aventura que exigiria coragem, humor e amizade.")

    # Adiciona conteúdo sob os títulos já criados — substituindo apenas o primeiro placeholder
    doc.text.addElement(P(text=""))
    # Reinsere os títulos para garantir posição correta do conteúdo
    doc.text.addElement(H(outlinelevel=1, stylename=styles["h1"], text="Capítulo 1: O Despertar dos Poderes"))
    doc.text.addElement(H(outlinelevel=2, stylename=styles["h2"], text="Tópico 1: Descoberta dos poderes pela equipe"))
    add_paragraphs(doc, styles, abertura)
    add_paragraphs(doc, styles, desenvolvimento)
    add_paragraphs(doc, styles, progressao)


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "arquivo.odt")

    # Documento
    doc = OpenDocumentText()

    # Metadados
    titulo = "Turma da Aventura: Nova Geração — Livro 1: Cidade dos Hackers"
    autor = "Turma da Aventura"
    assunto = "Aventura infantojuvenil cinematográfica com tecnologia e amizade"
    idioma = "pt-BR"
    keywords = ["Aventura", "Infantil", "Tecnologia", "Hackers", "Equipe"]
    add_meta(doc, titulo, autor, assunto, idioma, keywords)

    # Estilos
    styles = define_styles(doc)

    # Capa
    add_title_page(
        doc,
        styles,
        main_title=titulo,
        sub_title="Livro completo com estrutura otimizada para EPUB",
        author=autor,
    )

    # Índice
    add_table_of_contents(doc)

    # Estrutura dos capítulos conforme diretriz
    chapters = [
        ("O Despertar dos Poderes", [
            "Descoberta dos poderes pela equipe",
            "Primeira missão: invasão misteriosa na escola",
            "Primeira falha e união do grupo",
        ]),
        ("O Enigma do Código Azul", [
            "Mia decifra um código impossível",
            "Sophie investiga pistas digitais",
            "Will lidera a equipe em uma fuga eletrizante",
        ]),
        ("Ameaça Invisível", [
            "Íris detecta um vírus digital perigoso",
            "Max e Jimmy enfrentam animais controlados",
            "Leo protege o grupo em combate físico",
        ]),
        ("O Hacker Fantasma", [
            "Invasão à base secreta dos vilões",
            "Combate de poderes e gadgets",
            "Descoberta de uma mensagem enigmática",
        ]),
        ("Armadilha na Rede", [
            "Mia constrói um gadget para rastrear o vilão",
            "Equipe cai em uma armadilha digital",
            "Will precisa tomar uma decisão difícil",
        ]),
        ("O Labirinto Virtual", [
            "Íris cria um mapa holográfico",
            "Sophie desvenda enigmas do labirinto",
            "Leo enfrenta seu medo para salvar todos",
        ]),
        ("Combo de Poderes", [
            "Treinamento de combos em equipe",
            "Max traz humor e leveza durante o treino",
            "Primeira vitória contra os vilões",
        ]),
        ("O Grande Roubo de Dados", [
            "Vilão invade sistemas da cidade",
            "Mia e Íris unem forças para contra-atacar",
            "Equipe sofre consequências e aprende com erros",
        ]),
        ("A Última Defesa", [
            "Preparação para o confronto final",
            "Jimmy descobre uma fraqueza do vilão",
            "Momento emocional une o grupo",
        ]),
        ("O Hacker Revelado", [
            "Batalha épica e uso máximo dos poderes",
            "Vilão é derrotado de forma criativa",
            "Gancho para próxima aventura: uma nova ameaça surge",
        ]),
    ]

    build_structure(doc, styles, chapters)
    insert_chapter1_topic1(doc, styles)

    # Salvar
    doc.save(output_path)
    print(f"✅ ODT gerado: {output_path}")


if __name__ == "__main__":
    main()