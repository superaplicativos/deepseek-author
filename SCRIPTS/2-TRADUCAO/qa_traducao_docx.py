#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QA automático para DOCX traduzidos
- Remove espaços antes de ? ! ; (inglês e espanhol)
- Conta palavras, imagens e verifica resquícios de português
- Aplica correções seguras no document.xml, headers/footers, footnotes/endnotes
"""

import os
import sys
import zipfile
import xml.etree.ElementTree as ET
import re
from pathlib import Path
import tempfile

PUNCT_FIX_RE = re.compile(r"\s+([\?\!;])")

XML_TARGETS = [
    'word/document.xml',
]

EXTRA_TARGETS_PREFIXES = (
    'word/header',
    'word/footer',
)

EXTRA_TARGETS_EXACT = (
    'word/footnotes.xml',
    'word/endnotes.xml',
)

PT_WORDS = set(['o','a','de','que','e','do','da','em','um','para','é','com','não','uma','os','no','se','na','por','mais','as','dos','como','mas','foi','ao','ele','das','tem','à','seu','sua','ou','ser','quando','muito','há','nos','já','está','eu','também'])


def fix_text(text):
    """Remove espaços antes de ? ! ;"""
    if not text:
        return text
    return PUNCT_FIX_RE.sub(r"\1", text)


def process_xml_bytes(xml_bytes):
    """Aplica correções seguras em w:t"""
    root = ET.fromstring(xml_bytes)
    for elem in root.iter():
        if elem.tag.endswith('}t') and elem.text:
            elem.text = fix_text(elem.text)
    return ET.tostring(root, encoding='utf-8', xml_declaration=True)


def qa_docx(docx_path: str):
    if not os.path.exists(docx_path):
        print(f"❌ Arquivo não encontrado: {docx_path}")
        return False

    print(f"🔎 QA: {docx_path}")
    temp_out = None
    try:
        with zipfile.ZipFile(docx_path, 'r') as zin:
            entries = zin.namelist()
            media_files = [f for f in entries if f.startswith('word/media/')]
            images_count = len(media_files)

            # Contagem de palavras e resquícios de PT
            def collect_texts(name):
                try:
                    xml_bytes = zin.read(name)
                except KeyError:
                    return []
                root = ET.fromstring(xml_bytes)
                texts = []
                for elem in root.iter():
                    if elem.tag.endswith('}t') and elem.text:
                        texts.append(elem.text)
                return texts

            texts = []
            for t in XML_TARGETS:
                texts.extend(collect_texts(t))
            for name in entries:
                if name.startswith(EXTRA_TARGETS_PREFIXES) and name.endswith('.xml'):
                    texts.extend(collect_texts(name))
            for name in EXTRA_TARGETS_EXACT:
                if name in entries:
                    texts.extend(collect_texts(name))

            words = re.findall(r"[\wÀ-ÖØ-öø-ÿ]+", " ".join(texts), flags=re.UNICODE)
            pt_residual = sum(1 for w in words if w.lower() in PT_WORDS)
            total_words = len(words)

        # Aplicar correções criando novo DOCX
        # Usar diretório temporário seguro dentro da pasta do arquivo para evitar problemas de caminho
        base_dir = Path(docx_path).parent
        tmp_dir = Path(tempfile.mkdtemp(prefix='qa_tmp_', dir=str(base_dir)))

        with zipfile.ZipFile(docx_path, 'r') as zin:
            zin.extractall(tmp_dir)

        # Corrigir XMLs
        targets_to_fix = []
        for t in XML_TARGETS:
            p = tmp_dir / t
            if p.exists():
                targets_to_fix.append(p)
        for p in tmp_dir.glob('word/header*.xml'):
            targets_to_fix.append(p)
        for p in tmp_dir.glob('word/footer*.xml'):
            targets_to_fix.append(p)
        for name in EXTRA_TARGETS_EXACT:
            p = tmp_dir / name
            if p.exists():
                targets_to_fix.append(p)

        for p in targets_to_fix:
            xml_bytes = p.read_bytes()
            fixed = process_xml_bytes(xml_bytes)
            p.write_bytes(fixed)

        # Gerar arquivo corrigido (arcname em formato POSIX para compatibilidade DOCX)
        out_path = Path(docx_path).with_name(Path(docx_path).stem + '-QA' + Path(docx_path).suffix)
        with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zout:
            for root, dirs, files in os.walk(tmp_dir):
                for f in files:
                    fp = Path(root) / f
                    arc = (fp.relative_to(tmp_dir)).as_posix()
                    zout.write(str(fp), arc)

        # Limpeza
        import shutil
        shutil.rmtree(tmp_dir)

        print("✅ QA aplicado com sucesso")
        print(f"🖼️ Imagens preservadas: {images_count}")
        print(f"📝 Palavras (estimado): {total_words}")
        print(f"🇧🇷 Resquícios de PT detectados: {pt_residual}")
        print(f"📄 Arquivo corrigido: {out_path}")
        return {
            'docx': docx_path,
            'images': images_count,
            'words': total_words,
            'pt_residual': pt_residual,
            'qa_output': str(out_path)
        }

    except Exception as e:
        print(f"❌ Erro no QA: {e}")
        return False


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python qa_traducao_docx.py <arquivo.docx>")
        sys.exit(1)
    qa_docx(sys.argv[1])