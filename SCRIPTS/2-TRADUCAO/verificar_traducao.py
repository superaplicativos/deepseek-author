#!/usr/bin/env python3
"""
Script para verificar se a tradução realmente funcionou
"""

import zipfile
import xml.etree.ElementTree as ET
import os
from pathlib import Path

def verificar_traducao(arquivo_docx):
    """Verifica o conteúdo de um arquivo DOCX traduzido"""
    
    if not os.path.exists(arquivo_docx):
        print(f"❌ Arquivo não encontrado: {arquivo_docx}")
        return
    
    print(f"🔍 Verificando: {arquivo_docx}")
    print(f"📁 Tamanho: {os.path.getsize(arquivo_docx) / (1024*1024):.1f} MB")
    
    try:
        with zipfile.ZipFile(arquivo_docx, 'r') as docx_zip:
            # Ler o documento principal
            document_xml = docx_zip.read('word/document.xml').decode('utf-8')
            
            # Parse do XML
            root = ET.fromstring(document_xml)
            
            # Extrair todo o texto
            texto_completo = ""
            for elem in root.iter():
                if elem.text:
                    texto_completo += elem.text + " "
            
            # Mostrar primeiros 500 caracteres
            print(f"\n📝 PRIMEIROS 500 CARACTERES:")
            print("=" * 50)
            print(texto_completo[:500])
            print("=" * 50)
            
            # Verificar idioma
            palavras_portugues = ['o', 'a', 'de', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos', 'já', 'está', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'suas', 'numa', 'pelos', 'pelas', 'esse', 'eles', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'têm', 'numa', 'pelos', 'pelas', 'seu', 'sua']
            
            palavras_ingles = ['the', 'of', 'and', 'a', 'to', 'in', 'is', 'you', 'that', 'it', 'he', 'was', 'for', 'on', 'are', 'as', 'with', 'his', 'they', 'i', 'at', 'be', 'this', 'have', 'from', 'or', 'one', 'had', 'by', 'word', 'but', 'not', 'what', 'all', 'were', 'we', 'when', 'your', 'can', 'said', 'there', 'each', 'which', 'she', 'do', 'how', 'their', 'if', 'will', 'up', 'other', 'about', 'out', 'many', 'then', 'them', 'these', 'so', 'some', 'her', 'would', 'make', 'like', 'into', 'him', 'has', 'two', 'more', 'go', 'no', 'way', 'could', 'my', 'than', 'first', 'been', 'call', 'who', 'its', 'now', 'find', 'long', 'down', 'day', 'did', 'get', 'come', 'made', 'may', 'part']
            
            # Contar palavras
            palavras = texto_completo.lower().split()
            count_pt = sum(1 for palavra in palavras if palavra in palavras_portugues)
            count_en = sum(1 for palavra in palavras if palavra in palavras_ingles)
            
            print(f"\n📊 ANÁLISE DE IDIOMA:")
            print(f"Palavras em português detectadas: {count_pt}")
            print(f"Palavras em inglês detectadas: {count_en}")
            
            if count_pt > count_en:
                print("🇧🇷 RESULTADO: Documento parece estar em PORTUGUÊS")
            elif count_en > count_pt:
                print("🇺🇸 RESULTADO: Documento parece estar em INGLÊS")
            else:
                print("❓ RESULTADO: Idioma indefinido")
            
            # Verificar imagens
            media_files = [f for f in docx_zip.namelist() if f.startswith('word/media/')]
            print(f"\n🖼️ IMAGENS ENCONTRADAS: {len(media_files)}")
            
    except Exception as e:
        print(f"❌ Erro ao verificar arquivo: {e}")

if __name__ == "__main__":
    # Verificar arquivos traduzidos
    base_path = Path("LIVROS/traducoes_com_imagens")
    
    arquivos = [
        base_path / "MANUSCRITO-LIVRO6-COM-IMAGENS-EN.docx",
        base_path / "MANUSCRITO-LIVRO6-COM-IMAGENS-ES.docx"
    ]
    
    for arquivo in arquivos:
        verificar_traducao(str(arquivo))
        print("\n" + "="*80 + "\n")