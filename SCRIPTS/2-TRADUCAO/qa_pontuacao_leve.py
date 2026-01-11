#!/usr/bin/env python3
"""
QA leve de pontuação para DOCX:
- Remove espaços antes de sinais: ? ! ; : , .
- Aplica somente dentro de nós <w:t> para não afetar atributos/estrutura.
- Mantém imagens e formatação ao reempacotar o DOCX.

Uso:
  python qa_pontuacao_leve.py "caminho/arquivo.docx"
"""

import sys
import os
import zipfile
import re


def fix_text_punctuation(text: str) -> str:
    # Espaços antes de ?, !, ;, :
    text = re.sub(r"\s+([\?\!\;\:])", r"\1", text)
    # Espaços antes de vírgula e ponto
    text = re.sub(r"\s+,", ",", text)
    text = re.sub(r"\s+\.", ".", text)
    return text


def fix_xml_wt_blocks(xml: str) -> str:
    # Corrige apenas conteúdo dentro de w:t
    def repl(m: re.Match) -> str:
        start, inner, end = m.group(1), m.group(2), m.group(3)
        return start + fix_text_punctuation(inner) + end

    return re.sub(r"(<w:t[^>]*>)(.*?)(</w:t>)", repl, xml, flags=re.DOTALL)


def qa_docx_inplace(docx_path: str) -> None:
    tmp_path = docx_path + ".tmp"
    targets_prefixes = ("word/header", "word/footer")
    targets_names = {
        "word/document.xml",
        "word/footnotes.xml",
        "word/endnotes.xml",
        "word/comments.xml",
    }

    with zipfile.ZipFile(docx_path, "r") as zin, zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
        modified = 0
        for name in zin.namelist():
            data = zin.read(name)
            if name in targets_names or name.startswith(targets_prefixes):
                try:
                    xml = data.decode("utf-8")
                    fixed = fix_xml_wt_blocks(xml).encode("utf-8")
                    data = fixed
                    modified += 1
                except Exception:
                    # Se não decodificar como UTF-8, mantém como está
                    pass
            zout.writestr(name, data)

    os.replace(tmp_path, docx_path)
    print(f"QA leve aplicado com sucesso. Partes alteradas: {modified}")


def main():
    if len(sys.argv) < 2:
        print("Uso: python qa_pontuacao_leve.py <arquivo.docx>")
        sys.exit(1)
    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"Arquivo não encontrado: {path}")
        sys.exit(1)
    qa_docx_inplace(path)


if __name__ == "__main__":
    main()