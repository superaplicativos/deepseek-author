#!/usr/bin/env python3
import zipfile
import sys
import xml.etree.ElementTree as ET

NS = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
    'v': 'urn:schemas-microsoft-com:vml',
}

CONTENT_MAX_W_IN = 5.375
CONTENT_MAX_H_IN = 8.5
CONTENT_MAX_W_PT = CONTENT_MAX_W_IN * 72
CONTENT_MAX_H_PT = CONTENT_MAX_H_IN * 72

def parse_style(style: str):
    d = {}
    if not style:
        return d
    for part in style.split(';'):
        part = part.strip()
        if not part or ':' not in part:
            continue
        k, v = part.split(':', 1)
        d[k.strip()] = v.strip()
    return d

def to_pt(val: str):
    if not val:
        return None
    s = val.strip().lower()
    try:
        if s.endswith('pt'):
            return float(s[:-2])
        if s.endswith('px'):
            return float(s[:-2]) * 0.75
        if s.endswith('in'):
            return float(s[:-2]) * 72.0
        return float(s)
    except Exception:
        return None

def inspect(path: str):
    with zipfile.ZipFile(path, 'r') as z:
        xml = z.read('word/document.xml')
    root = ET.fromstring(xml)
    inlines = root.findall('.//wp:inline', NS)
    anchors = root.findall('.//wp:anchor', NS)
    picts = root.findall('.//w:pict', NS)
    shapes = root.findall('.//v:shape', NS)

    # extents (wp:extent and a:ext under pic:spPr)
    cxs = []
    cys = []
    for p in root.findall('.//w:p', NS):
        for inline in p.findall('.//wp:inline', NS):
            e = inline.find('wp:extent', NS)
            if e is not None:
                cx = e.get(f"{{{NS['wp']}}}cx")
                cy = e.get(f"{{{NS['wp']}}}cy")
                if cx:
                    try:
                        cxs.append(int(cx))
                    except Exception:
                        pass
                if cy:
                    try:
                        cys.append(int(cy))
                    except Exception:
                        pass
            for aext in inline.findall('.//pic:pic/pic:spPr/a:xfrm/a:ext', NS):
                cx = aext.get(f"{{{NS['a']}}}cx")
                cy = aext.get(f"{{{NS['a']}}}cy")
                if cx:
                    try:
                        cxs.append(int(cx))
                    except Exception:
                        pass
                if cy:
                    try:
                        cys.append(int(cy))
                    except Exception:
                        pass

    # VML oversize check
    overs_w = 0
    overs_h = 0
    for s in shapes:
        d = parse_style(s.get('style'))
        wpt = to_pt(d.get('width'))
        hpt = to_pt(d.get('height'))
        if wpt and wpt > CONTENT_MAX_W_PT:
            overs_w += 1
        if hpt and hpt > CONTENT_MAX_H_PT:
            overs_h += 1

    print('wp:inline:', len(inlines))
    print('wp:anchor:', len(anchors))
    print('w:pict:', len(picts))
    print('v:shape:', len(shapes))
    print('max cx (emu):', (max(cxs) if cxs else 'N/A'))
    print('max cy (emu):', (max(cys) if cys else 'N/A'))
    print('VML oversize width count:', overs_w)
    print('VML oversize height count:', overs_h)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python inspecionar_imagens.py <arquivo.docx>')
        sys.exit(1)
    inspect(sys.argv[1])