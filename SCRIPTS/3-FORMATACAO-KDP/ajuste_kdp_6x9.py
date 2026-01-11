#!/usr/bin/env python3
"""
Ajuste de DOCX para compatibilidade KDP (6" x 9"):
- Define tamanho da página para 6x9 polegadas
- Define margens mínimas KDP: externas/topo/rodapé 0.25" e medianiz (interna) 0.375"
- Ativa margens espelhadas (mirrorMargins) e aplica gutter
- Redimensiona imagens para caber na área útil (largura máxima ~5.375")

Uso:
  python ajuste_kdp_6x9.py "caminho/arquivo.docx" [saida.docx]
Se não fornecer saída, gera ao lado com sufixo -KDP-6x9.docx
"""

import os
import sys
import zipfile
import xml.etree.ElementTree as ET

# Namespaces
NS = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
}
for pfx, uri in NS.items():
    ET.register_namespace(pfx, uri)


def inches_to_twips(inches: float) -> int:
    return int(round(inches * 1440))


def inches_to_emus(inches: float) -> int:
    return int(round(inches * 914400))


PAGE_W_IN = 6.0
PAGE_H_IN = 9.0
MARGIN_EXT_IN = 0.25  # externo, topo, inferior
GUTTER_IN = 0.125     # adicional para atingir 0.375" interno (0.25 + 0.125)
HEADER_DIST_IN = 0.2
FOOTER_DIST_IN = 0.2

# Área útil máxima de largura (em polegadas)
CONTENT_MAX_W_IN = PAGE_W_IN - (MARGIN_EXT_IN + (MARGIN_EXT_IN + GUTTER_IN))  # 6 - (0.25 + 0.375) = 5.375
CONTENT_MAX_W_EMU = inches_to_emus(CONTENT_MAX_W_IN)
CONTENT_MAX_H_IN = PAGE_H_IN - (MARGIN_EXT_IN + MARGIN_EXT_IN)  # 9 - (0.25 + 0.25) = 8.5
CONTENT_MAX_H_EMU = inches_to_emus(CONTENT_MAX_H_IN)
STRICT_SHRINK_FACTOR = 0.97  # encolhe ligeiramente para garantir folga visual


def ensure_child(parent: ET.Element, tag: str) -> ET.Element:
    child = parent.find(tag, NS)
    if child is None:
        child = ET.SubElement(parent, tag)
    return child


def patch_sections_for_kdp(root: ET.Element) -> None:
    # Padrão: localizar todos sectPr
    for sect in root.findall('.//w:sectPr', NS):
        # page size
        pgSz = ensure_child(sect, f"{{{NS['w']}}}pgSz")
        pgSz.set(f"{{{NS['w']}}}w", str(inches_to_twips(PAGE_W_IN)))
        pgSz.set(f"{{{NS['w']}}}h", str(inches_to_twips(PAGE_H_IN)))
        pgSz.set(f"{{{NS['w']}}}orient", 'portrait')

        # page margins
        pgMar = ensure_child(sect, f"{{{NS['w']}}}pgMar")
        pgMar.set(f"{{{NS['w']}}}top", str(inches_to_twips(MARGIN_EXT_IN)))
        pgMar.set(f"{{{NS['w']}}}bottom", str(inches_to_twips(MARGIN_EXT_IN)))
        pgMar.set(f"{{{NS['w']}}}left", str(inches_to_twips(MARGIN_EXT_IN)))
        pgMar.set(f"{{{NS['w']}}}right", str(inches_to_twips(MARGIN_EXT_IN)))
        pgMar.set(f"{{{NS['w']}}}gutter", str(inches_to_twips(GUTTER_IN)))
        pgMar.set(f"{{{NS['w']}}}header", str(inches_to_twips(HEADER_DIST_IN)))
        pgMar.set(f"{{{NS['w']}}}footer", str(inches_to_twips(FOOTER_DIST_IN)))

        # mirror margins
        mm = sect.find('w:mirrorMargins', NS)
        if mm is None:
            ET.SubElement(sect, f"{{{NS['w']}}}mirrorMargins")


def scale_container_images(container: ET.Element) -> bool:
    """Redimensiona imagem dentro de um container wp:inline/wp:anchor.
    Ajusta wp:extent e também pic:spPr/a:xfrm/a:ext correspondente.
    """
    extent = container.find('wp:extent', NS)
    if extent is None:
        return False
    # atributos cx/cy não são namespaced
    cx = extent.get('cx')
    cy = extent.get('cy')
    if not cx or not cy:
        return False
    try:
        cx_val = int(cx)
        cy_val = int(cy)
    except Exception:
        return False
    # Escala proporcional para caber em largura e altura da área útil
    max_w = int(CONTENT_MAX_W_EMU * STRICT_SHRINK_FACTOR)
    max_h = int(CONTENT_MAX_H_EMU * STRICT_SHRINK_FACTOR)
    ratio_w = max_w / float(cx_val)
    ratio_h = max_h / float(cy_val)
    ratio = min(ratio_w, ratio_h)
    if ratio >= 1.0:
        # encolher levemente mesmo quando já cabe
        ratio = STRICT_SHRINK_FACTOR
    new_cx = int(round(cx_val * ratio))
    new_cy = int(round(cy_val * ratio))
    extent.set('cx', str(new_cx))
    extent.set('cy', str(new_cy))
    # Ajustar a:ext dentro do mesmo container
    for xfrm_ext in container.findall('.//pic:pic/pic:spPr/a:xfrm/a:ext', NS):
        # atributos cx/cy em a:ext também não são namespaced
        xfrm_ext.set('cx', str(new_cx))
        xfrm_ext.set('cy', str(new_cy))
    return True


def fix_anchor_position(container: ET.Element) -> None:
    """Garante que imagens ancoradas não fiquem coladas na borda.
    - Alinha horizontalmente ao centro relativo às margens
    - Define pequenas distâncias laterais/topo/rodapé
    """
    if container.tag != f"{{{NS['wp']}}}anchor":
        return
    # distâncias mínimas
    dist_small = inches_to_emus(0.05)
    # atributos de distância não são namespaced
    container.set('distL', str(dist_small))
    container.set('distR', str(dist_small))
    container.set('distT', str(dist_small))
    container.set('distB', str(dist_small))

    posH = container.find('wp:positionH', NS)
    if posH is None:
        posH = ET.SubElement(container, f"{{{NS['wp']}}}positionH")
    posH.set('relativeFrom', 'margin')
    # Remover offsets e garantir align center
    for child in list(posH):
        if child.tag == f"{{{NS['wp']}}}posOffset":
            posH.remove(child)
    align = posH.find('wp:align', NS)
    if align is None:
        align = ET.SubElement(posH, f"{{{NS['wp']}}}align")
    align.text = 'center'

    posV = container.find('wp:positionV', NS)
    if posV is None:
        posV = ET.SubElement(container, f"{{{NS['wp']}}}positionV")
    # Evitar posicionamento fora da área de parágrafo
    posV.set('relativeFrom', 'paragraph')
    # Não definimos align vertical para preservar fluxo; removemos offsets negativos
    for child in list(posV):
        if child.tag == f"{{{NS['wp']}}}posOffset":
            # clamp a não-negativo
            try:
                val = int(child.text or '0')
            except Exception:
                val = 0
            if val < 0:
                child.text = '0'


def scale_image_extents(tree: ET.ElementTree) -> int:
    root = tree.getroot()
    changed = 0
    # Processar containers inline e anchor
    for container in root.findall('.//wp:inline', NS):
        if scale_container_images(container):
            changed += 1
    for container in root.findall('.//wp:anchor', NS):
        if scale_container_images(container):
            changed += 1
        fix_anchor_position(container)
    return changed


def process_xml_bytes(name: str, data: bytes) -> bytes:
    # Apenas processar document.xml e cabeçalhos/rodapés para imagens
    try:
        xml = data.decode('utf-8')
    except Exception:
        return data

    tree = ET.ElementTree(ET.fromstring(xml))

    if name == 'word/document.xml':
        # ajustar seções e redimensionar/alinha imagens
        root = tree.getroot()
        patch_sections_for_kdp(root)
        changed_imgs = scale_image_extents(tree)
        try:
            print(f"[ajuste_kdp] Imagens redimensionadas no corpo: {changed_imgs}")
        except Exception:
            pass
        # Centralizar parágrafos que contém imagens inline/anchor e normalizar recuos
        for p in root.findall('.//w:p', NS):
            has_img = (p.find('.//wp:inline', NS) is not None) or (p.find('.//wp:anchor', NS) is not None)
            if has_img:
                pPr = p.find('w:pPr', NS)
                if pPr is None:
                    pPr = ET.SubElement(p, f"{{{NS['w']}}}pPr")
                jc = pPr.find('w:jc', NS)
                if jc is None:
                    jc = ET.SubElement(pPr, f"{{{NS['w']}}}jc")
                jc.set(f"{{{NS['w']}}}val", 'center')
                # remover recuos para não ultrapassar margens
                ind = pPr.find('w:ind', NS)
                if ind is None:
                    ind = ET.SubElement(pPr, f"{{{NS['w']}}}ind")
                ind.set(f"{{{NS['w']}}}left", '0')
                ind.set(f"{{{NS['w']}}}right", '0')
                ind.set(f"{{{NS['w']}}}firstLine", '0')
    elif name.startswith('word/header') or name.startswith('word/footer'):
        # redimensionar/alinha imagens em cabeçalhos/rodapés
        changed_hdrftr = scale_image_extents(tree)
        try:
            print(f"[ajuste_kdp] Imagens redimensionadas em header/footer: {changed_hdrftr}")
        except Exception:
            pass

    new_xml = ET.tostring(tree.getroot(), encoding='utf-8', xml_declaration=True)
    return new_xml


def ajustar_docx_kdp(in_path: str, out_path: str) -> None:
    with zipfile.ZipFile(in_path, 'r') as zin, zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zout:
        for name in zin.namelist():
            data = zin.read(name)
            if name == 'word/document.xml' or name.startswith('word/header') or name.startswith('word/footer'):
                try:
                    data = process_xml_bytes(name, data)
                except Exception:
                    # Se falhar, mantém original
                    pass
            zout.writestr(name, data)


def main():
    if len(sys.argv) < 2:
        print("Uso: python ajuste_kdp_6x9.py <arquivo.docx> [saida.docx]")
        sys.exit(1)
    in_path = sys.argv[1]
    if not os.path.exists(in_path):
        print(f"Arquivo não encontrado: {in_path}")
        sys.exit(1)
    if len(sys.argv) >= 3:
        out_path = sys.argv[2]
    else:
        base, ext = os.path.splitext(in_path)
        out_path = base + "-KDP-6x9" + ext

    ajustar_docx_kdp(in_path, out_path)
    print(f"✅ Ajuste KDP 6x9 concluído: {out_path}")


if __name__ == '__main__':
    main()