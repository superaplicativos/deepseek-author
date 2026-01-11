#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QA Fixer for DOCX punctuation spacing (en-US)
- Removes spaces before ?, !, ;, : across document, headers, footers, footnotes, endnotes, and comments
- Preserves all images and formatting by operating at the XML text node level
"""

import os
import sys
import zipfile
import shutil
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
import re

TARGET_XML_FILES = [
    'word/document.xml',
    'word/footnotes.xml',
    'word/endnotes.xml',
    'word/comments.xml',
]

# Headers/Footers processed dynamically (header*.xml, footer*.xml)

PUNCT_FIX_PATTERN = re.compile(r"\s+([\?\!\;\:])")


def fix_text(text: str) -> str:
    if not text:
        return text
    # Remove spaces before ? ! ; :
    fixed = PUNCT_FIX_PATTERN.sub(r"\1", text)
    return fixed


def process_xml_file(xml_path: str) -> int:
    """Process one XML file, return number of changes."""
    if not os.path.exists(xml_path):
        return 0
    tree = ET.parse(xml_path)
    root = tree.getroot()
    changes = 0
    for elem in root.iter():
        if elem.tag.endswith('}t') and elem.text:
            new_text = fix_text(elem.text)
            if new_text != elem.text:
                elem.text = new_text
                changes += 1
    if changes:
        tree.write(xml_path, encoding='utf-8', xml_declaration=True)
    return changes


def main():
    if len(sys.argv) < 2:
        print("Uso: python qa_fix_punctuation_docx.py <arquivo.docx>")
        sys.exit(1)

    docx_path = sys.argv[1]
    if not os.path.exists(docx_path):
        print(f"❌ Arquivo não encontrado: {docx_path}")
        sys.exit(1)

    tmp_dir = tempfile.mkdtemp(prefix="qa_docx_")
    extract_dir = os.path.join(tmp_dir, "extract")
    os.makedirs(extract_dir)

    # Extract DOCX
    with zipfile.ZipFile(docx_path, 'r') as zf:
        zf.extractall(extract_dir)

    # Discover headers and footers
    word_dir = os.path.join(extract_dir, 'word')
    header_footer_files = []
    if os.path.exists(word_dir):
        for fname in os.listdir(word_dir):
            if fname.startswith('header') and fname.endswith('.xml'):
                header_footer_files.append(os.path.join(word_dir, fname))
            if fname.startswith('footer') and fname.endswith('.xml'):
                header_footer_files.append(os.path.join(word_dir, fname))

    total_changes = 0

    # Process main targets
    for rel in TARGET_XML_FILES:
        xml_path = os.path.join(extract_dir, rel)
        total_changes += process_xml_file(xml_path)

    # Process headers/footers
    for xml_path in header_footer_files:
        total_changes += process_xml_file(xml_path)

    # Repack DOCX (overwrite original)
    tmp_out = os.path.join(tmp_dir, Path(docx_path).name)
    with zipfile.ZipFile(tmp_out, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arc_name = os.path.relpath(file_path, extract_dir)
                zf.write(file_path, arc_name)

    # Replace original
    shutil.copy2(tmp_out, docx_path)

    # Cleanup
    shutil.rmtree(tmp_dir, ignore_errors=True)

    print("✅ QA de pontuação aplicado")
    print(f"🔧 Alterações em nós de texto: {total_changes}")
    print(f"📁 Arquivo atualizado: {docx_path}")


if __name__ == "__main__":
    main()