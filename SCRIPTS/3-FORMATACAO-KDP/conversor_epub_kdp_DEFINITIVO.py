#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CONVERSOR EPUB DEFINITIVO PARA AMAZON KDP
Extrai imagens do DOCX e cria EPUB compatível com KDP
"""

import os
import zipfile
import xml.etree.ElementTree as ET
from docx import Document
from PIL import Image
import io
import uuid
import re
from datetime import datetime

def extrair_imagens_docx(docx_path):
    """Extrai todas as imagens do DOCX original"""
    print("🖼️ EXTRAINDO IMAGENS DO DOCX ORIGINAL...")
    
    imagens = []
    
    try:
        # Abre o DOCX como ZIP
        with zipfile.ZipFile(docx_path, 'r') as docx_zip:
            # Lista todos os arquivos de mídia
            media_files = [f for f in docx_zip.namelist() if f.startswith('word/media/')]
            
            print(f"📊 Encontrados {len(media_files)} arquivos de mídia")
            
            for i, media_file in enumerate(media_files, 1):
                try:
                    # Lê os dados da imagem
                    img_data = docx_zip.read(media_file)
                    
                    # Determina a extensão
                    if media_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                        ext = os.path.splitext(media_file)[1].lower()
                        if ext == '.jpeg':
                            ext = '.jpg'
                        
                        # Verifica se é uma imagem válida
                        try:
                            img = Image.open(io.BytesIO(img_data))
                            width, height = img.size
                            
                            # Converte para RGB se necessário (para compatibilidade)
                            if img.mode in ('RGBA', 'LA', 'P'):
                                background = Image.new('RGB', img.size, (255, 255, 255))
                                if img.mode == 'P':
                                    img = img.convert('RGBA')
                                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                                img = background
                            
                            # Salva a imagem processada
                            img_buffer = io.BytesIO()
                            img.save(img_buffer, format='JPEG' if ext == '.jpg' else 'PNG', quality=95)
                            img_data_processed = img_buffer.getvalue()
                            
                            imagem_info = {
                                'nome': f"image_{i:03d}{ext}",
                                'dados': img_data_processed,
                                'largura': width,
                                'altura': height,
                                'formato': img.format,
                                'tamanho': len(img_data_processed)
                            }
                            
                            imagens.append(imagem_info)
                            print(f"✅ Imagem {i}: {imagem_info['nome']} ({width}x{height}) - {len(img_data_processed):,} bytes")
                            
                        except Exception as e:
                            print(f"❌ Erro ao processar {media_file}: {e}")
                    
                except Exception as e:
                    print(f"❌ Erro ao ler {media_file}: {e}")
        
        print(f"🎯 Total de imagens extraídas: {len(imagens)}")
        return imagens
        
    except Exception as e:
        print(f"❌ Erro ao extrair imagens: {e}")
        return []

def extrair_texto_docx(docx_path):
    """Extrai texto do DOCX traduzido"""
    print("📖 EXTRAINDO TEXTO DO DOCX...")
    
    try:
        doc = Document(docx_path)
        paragrafos = []
        
        for para in doc.paragraphs:
            texto = para.text.strip()
            if texto:
                paragrafos.append(texto)
        
        print(f"📊 Extraídos {len(paragrafos)} parágrafos")
        return paragrafos
        
    except Exception as e:
        print(f"❌ Erro ao extrair texto: {e}")
        return []

def dividir_em_capitulos(paragrafos, imagens):
    """Divide o texto em capítulos e distribui as imagens"""
    print("📚 DIVIDINDO EM CAPÍTULOS...")
    
    # Calcula parágrafos por capítulo
    total_paragrafos = len(paragrafos)
    paragrafos_por_capitulo = max(50, total_paragrafos // 25)  # Mínimo 50 parágrafos por capítulo
    
    capitulos = []
    imagens_por_capitulo = len(imagens) // 25 if len(imagens) >= 25 else 1
    
    for i in range(0, total_paragrafos, paragrafos_por_capitulo):
        cap_paragrafos = paragrafos[i:i + paragrafos_por_capitulo]
        cap_numero = len(capitulos) + 1
        
        # Distribui imagens pelo capítulo
        inicio_img = (cap_numero - 1) * imagens_por_capitulo
        fim_img = min(inicio_img + imagens_por_capitulo, len(imagens))
        cap_imagens = imagens[inicio_img:fim_img] if inicio_img < len(imagens) else []
        
        capitulo = {
            'numero': cap_numero,
            'titulo': f"Chapter {cap_numero}",
            'paragrafos': cap_paragrafos,
            'imagens': cap_imagens
        }
        
        capitulos.append(capitulo)
        print(f"📖 Capítulo {cap_numero}: {len(cap_paragrafos)} parágrafos, {len(cap_imagens)} imagens")
    
    print(f"🎯 Total de capítulos criados: {len(capitulos)}")
    return capitulos

def criar_epub_kdp(docx_path, epub_path):
    """Cria EPUB otimizado para Amazon KDP"""
    print("🚀 CRIANDO EPUB OTIMIZADO PARA AMAZON KDP...")
    print("=" * 60)
    
    # 1. Extrai imagens do DOCX original
    imagens = extrair_imagens_docx(docx_path)
    if not imagens:
        print("❌ Nenhuma imagem encontrada no DOCX")
        return False
    
    # 2. Extrai texto do DOCX traduzido
    docx_traduzido = "MANUSCRITOPORTUGUES-EN-GRATUITO.docx"
    paragrafos = extrair_texto_docx(docx_traduzido)
    if not paragrafos:
        print("❌ Nenhum texto encontrado no DOCX traduzido")
        return False
    
    # 3. Divide em capítulos
    capitulos = dividir_em_capitulos(paragrafos, imagens)
    
    # 4. Cria estrutura EPUB
    print("\n📦 CRIANDO ESTRUTURA EPUB...")
    
    try:
        with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as epub_zip:
            
            # Mimetype (deve ser o primeiro arquivo, sem compressão)
            epub_zip.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
            
            # META-INF/container.xml
            container_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>'''
            epub_zip.writestr('META-INF/container.xml', container_xml)
            
            # CSS
            css_content = '''
body {
    font-family: "Times New Roman", serif;
    line-height: 1.6;
    margin: 0;
    padding: 20px;
    text-align: justify;
}

h1, h2, h3 {
    color: #333;
    text-align: center;
    margin: 30px 0 20px 0;
}

p {
    margin: 0 0 15px 0;
    text-indent: 1.5em;
}

.chapter-title {
    font-size: 1.5em;
    font-weight: bold;
    text-align: center;
    margin: 40px 0 30px 0;
    page-break-before: always;
}

.image-container {
    text-align: center;
    margin: 20px 0;
    page-break-inside: avoid;
}

.image-container img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
}

.image-caption {
    font-size: 0.9em;
    color: #666;
    font-style: italic;
    margin-top: 10px;
}
'''
            epub_zip.writestr('OEBPS/styles/main.css', css_content)
            
            # Salva todas as imagens
            print("🖼️ SALVANDO IMAGENS...")
            for img in imagens:
                img_path = f"OEBPS/images/{img['nome']}"
                epub_zip.writestr(img_path, img['dados'])
                print(f"✅ Salva: {img['nome']}")
            
            # Cria capítulos XHTML
            print("📖 CRIANDO CAPÍTULOS...")
            manifest_items = []
            spine_items = []
            
            for cap in capitulos:
                cap_filename = f"chapter_{cap['numero']:03d}.xhtml"
                cap_path = f"OEBPS/text/{cap_filename}"
                
                # Conteúdo do capítulo
                cap_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>{cap['titulo']}</title>
    <link rel="stylesheet" type="text/css" href="../styles/main.css"/>
</head>
<body>
    <h1 class="chapter-title">{cap['titulo']}</h1>
'''
                
                # Adiciona parágrafos e imagens intercalados
                paragrafos_por_imagem = len(cap['paragrafos']) // max(1, len(cap['imagens']))
                img_index = 0
                
                for i, paragrafo in enumerate(cap['paragrafos']):
                    cap_content += f'    <p>{paragrafo}</p>\n'
                    
                    # Insere imagem a cada X parágrafos
                    if (i + 1) % max(10, paragrafos_por_imagem) == 0 and img_index < len(cap['imagens']):
                        img = cap['imagens'][img_index]
                        cap_content += f'''
    <div class="image-container">
        <img src="../images/{img['nome']}" alt="Image {img_index + 1}"/>
        <div class="image-caption">Image {img_index + 1}</div>
    </div>
'''
                        img_index += 1
                
                # Adiciona imagens restantes no final do capítulo
                while img_index < len(cap['imagens']):
                    img = cap['imagens'][img_index]
                    cap_content += f'''
    <div class="image-container">
        <img src="../images/{img['nome']}" alt="Image {img_index + 1}"/>
        <div class="image-caption">Image {img_index + 1}</div>
    </div>
'''
                    img_index += 1
                
                cap_content += '''
</body>
</html>'''
                
                epub_zip.writestr(cap_path, cap_content)
                
                # Adiciona ao manifest e spine
                cap_id = f"chapter_{cap['numero']:03d}"
                manifest_items.append(f'    <item id="{cap_id}" href="text/{cap_filename}" media-type="application/xhtml+xml"/>')
                spine_items.append(f'    <itemref idref="{cap_id}"/>')
                
                print(f"✅ Capítulo {cap['numero']}: {len(cap['paragrafos'])} parágrafos, {len(cap['imagens'])} imagens")
            
            # Navigation Document (EPUB 3)
            nav_content = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>Navigation</title>
    <link rel="stylesheet" type="text/css" href="styles/main.css"/>
</head>
<body>
    <nav epub:type="toc" id="toc">
        <h1>Table of Contents</h1>
        <ol>
'''
            
            for cap in capitulos:
                cap_num = cap["numero"]
                cap_titulo = cap["titulo"]
                nav_content += f'            <li><a href="text/chapter_{cap_num:03d}.xhtml">{cap_titulo}</a></li>\n'
            
            nav_content += '''        </ol>
    </nav>
</body>
</html>'''
            
            epub_zip.writestr('OEBPS/nav.xhtml', nav_content)
            
            # TOC NCX (EPUB 2 compatibility)
            toc_uuid = str(uuid.uuid4())
            toc_ncx = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
    <head>
        <meta name="dtb:uid" content="{toc_uuid}"/>
        <meta name="dtb:depth" content="1"/>
        <meta name="dtb:totalPageCount" content="0"/>
        <meta name="dtb:maxPageNumber" content="0"/>
    </head>
    <docTitle>
        <text>Manuscrito Português - English Translation</text>
    </docTitle>
    <navMap>
'''
            
            for cap in capitulos:
                cap_num = cap["numero"]
                cap_titulo = cap["titulo"]
                toc_ncx += f'''        <navPoint id="chapter_{cap_num:03d}" playOrder="{cap_num}">
            <navLabel>
                <text>{cap_titulo}</text>
            </navLabel>
            <content src="text/chapter_{cap_num:03d}.xhtml"/>
        </navPoint>
'''
            
            toc_ncx += '''    </navMap>
</ncx>'''
            
            epub_zip.writestr('OEBPS/toc.ncx', toc_ncx)
            
            # Content.opf (Package Document)
            book_uuid = str(uuid.uuid4())
            current_date = datetime.now().strftime('%Y-%m-%d')
            
            # Manifest items para imagens
            img_manifest = []
            for img in imagens:
                img_id = os.path.splitext(img['nome'])[0]
                img_nome = img['nome']
                media_type = 'image/jpeg' if img_nome.endswith('.jpg') else 'image/png'
                img_manifest.append(f'    <item id="{img_id}" href="images/{img_nome}" media-type="{media_type}"/>')
            
            content_opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="3.0">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
        <dc:identifier id="BookId">{book_uuid}</dc:identifier>
        <dc:title>Manuscrito Português - English Translation</dc:title>
        <dc:creator opf:role="aut">Autor Original</dc:creator>
        <dc:language>en</dc:language>
        <dc:date>{current_date}</dc:date>
        <meta property="dcterms:modified">{current_date}T00:00:00Z</meta>
    </metadata>
    <manifest>
        <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
        <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
        <item id="css" href="styles/main.css" media-type="text/css"/>
{chr(10).join(manifest_items)}
{chr(10).join(img_manifest)}
    </manifest>
    <spine toc="ncx">
{chr(10).join(spine_items)}
    </spine>
</package>'''
            
            epub_zip.writestr('OEBPS/content.opf', content_opf)
            
        print(f"\n🎉 EPUB CRIADO COM SUCESSO!")
        print(f"📁 Arquivo: {epub_path}")
        print(f"📊 Tamanho: {os.path.getsize(epub_path) / (1024*1024):.1f} MB")
        print(f"🖼️ Imagens: {len(imagens)}")
        print(f"📖 Capítulos: {len(capitulos)}")
        print(f"🚀 Otimizado para Amazon KDP!")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar EPUB: {e}")
        return False

def main():
    """Função principal"""
    docx_original = "MANUSCRITOPORTUGUES.docx"
    epub_output = "MANUSCRITOPORTUGUES-EN-GRATUITO-KDP.epub"
    
    print("🚀 CONVERSOR EPUB DEFINITIVO PARA AMAZON KDP")
    print("=" * 60)
    print("🎯 Objetivo: Criar EPUB com imagens compatível com KDP")
    print(f"📄 DOCX Original: {docx_original}")
    print(f"📄 DOCX Traduzido: MANUSCRITOPORTUGUES-EN-GRATUITO.docx")
    print(f"📚 EPUB Output: {epub_output}")
    print()
    
    if not os.path.exists(docx_original):
        print(f"❌ Arquivo não encontrado: {docx_original}")
        return
    
    if not os.path.exists("MANUSCRITOPORTUGUES-EN-GRATUITO.docx"):
        print("❌ Arquivo traduzido não encontrado: MANUSCRITOPORTUGUES-EN-GRATUITO.docx")
        return
    
    if criar_epub_kdp(docx_original, epub_output):
        print("\n🎉 CONVERSÃO CONCLUÍDA COM SUCESSO!")
        print("✅ EPUB otimizado para Amazon KDP criado")
        print("🖼️ Todas as imagens do DOCX original preservadas")
        print("📱 Pronto para upload no KDP!")
    else:
        print("\n❌ ERRO NA CONVERSÃO")

if __name__ == "__main__":
    main()