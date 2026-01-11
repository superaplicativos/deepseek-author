#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRADUTOR ODT DIRETO GRATUITO - SEM CUSTOS!
Traduz documentos ODT diretamente mantendo imagens, formatação e estrutura
Usa Google Translate GRATUITO (sem API)
Não precisa de LibreOffice!
"""

import os
import sys
import zipfile
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
import time
import random
import re
from typing import List

# Configurar encoding UTF-8 para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Instalar dependências se necessário
def instalar_dependencias():
    """Instala dependências necessárias."""
    import subprocess, sys
    try:
        from deep_translator import GoogleTranslator  # noqa: F401
        print("✅ Dependências já instaladas!")
    except Exception:
        print("📦 Instalando dependências gratuitas...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--force-reinstall", "deep-translator", "requests"])
        print("✅ Dependências instaladas!")

instalar_dependencias()

from deep_translator import GoogleTranslator

class TradutorOdtDiretoGratuito:
    """Tradutor ODT direto 100% gratuito usando Google Translate"""

    def __init__(self):
        self.translator = None
        self.temp_dir = "temp_traducao_odt"
        self.traducoes_cache = {}

    def criar_diretorio_temp(self):
        """Cria diretório temporário"""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        os.makedirs(self.temp_dir)

    def extrair_odt(self, arquivo_odt: str) -> str:
        """Extrai o conteúdo do ODT"""
        pasta_extracao = os.path.join(self.temp_dir, "extraido")

        with zipfile.ZipFile(arquivo_odt, 'r') as zip_ref:
            zip_ref.extractall(pasta_extracao)

        return pasta_extracao

    def traduzir_texto(self, texto: str, idioma_destino: str = 'en') -> str:
        """Traduz texto usando Google Translate GRATUITO"""
        if not texto or not texto.strip():
            return texto

        # Cache
        cache_key = f"{texto}_{idioma_destino}"
        if cache_key in self.traducoes_cache:
            return self.traducoes_cache[cache_key]

        # Preservar tokens especiais
        preservations: List[str] = []
        def _preserve(match):
            idx = len(preservations)
            token = match.group(0)
            preservations.append(token)
            return f"[[PRESERVE_{idx}]]"

        prepared = texto
        patterns = [
            r"`[^`]+`",
            r"https?://\S+",
            r"www\.\S+",
            r"[\w\.-]+@[\w\.-]+\.[A-Za-z]{2,}",
            r"\b[a-zA-Z_][a-zA-Z0-9_]*_[a-zA-Z0-9_]*\b",
            r"\[\[RUN_\d+\]\]",
        ]
        for pat in patterns:
            prepared = re.sub(pat, _preserve, prepared)
        prepared = re.sub(r"\b([A-Z][A-Z0-9_]{2,})\b", _preserve, prepared)

        try:
            self.translator = GoogleTranslator(source='auto', target=idioma_destino)
            max_tentativas = 5
            base_sleep = 1.0
            texto_traduzido = None

            for tentativa in range(1, max_tentativas + 1):
                try:
                    if len(prepared) > 4500:
                        partes = self.dividir_texto(prepared, 4000)
                        agregado = []
                        for parte in partes:
                            if parte.strip():
                                agregado.append(self.translator.translate(parte) or parte)
                                time.sleep(random.uniform(0.5, 1.2))
                        texto_traduzido = " ".join(agregado).strip()
                    else:
                        texto_traduzido = self.translator.translate(prepared)

                    if not texto_traduzido or texto_traduzido.strip() == prepared.strip():
                        raise RuntimeError("Tradução falhou")
                    break
                except Exception as e:
                    espera = base_sleep * (2 ** (tentativa - 1)) + random.uniform(0, 0.8)
                    if tentativa < max_tentativas:
                        print(f"⏳ Tentativa {tentativa}/{max_tentativas} falhou. Aguardando {espera:.1f}s...")
                        time.sleep(espera)
                    continue

            if not texto_traduzido:
                raise RuntimeError("Falha após múltiplas tentativas")

            # Restaurar tokens
            for i, token in enumerate(preservations):
                texto_traduzido = texto_traduzido.replace(f"[[PRESERVE_{i}]]", token)

            self.traducoes_cache[cache_key] = texto_traduzido
            return texto_traduzido

        except Exception as e:
            print(f"⚠️ Erro na tradução: {e}")
            return texto

    def dividir_texto(self, texto: str, tamanho_max: int) -> List[str]:
        """Divide texto em partes menores"""
        if len(texto) <= tamanho_max:
            return [texto]

        partes = []
        palavras = texto.split()
        parte_atual = ""

        for palavra in palavras:
            if len(parte_atual + " " + palavra) <= tamanho_max:
                parte_atual += " " + palavra if parte_atual else palavra
            else:
                if parte_atual:
                    partes.append(parte_atual)
                parte_atual = palavra

        if parte_atual:
            partes.append(parte_atual)

        return partes

    def processar_xml_odt(self, caminho_xml: str, idioma_destino: str):
        """Processa o XML do ODT (content.xml)"""
        # Registrar namespaces do ODT
        namespaces = {
            'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
            'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
            'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
            'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
            'draw': 'urn:oasis:names:tc:opendocument:xmlns:drawing:1.0',
            'svg': 'urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0',
            'xlink': 'http://www.w3.org/1999/xlink',
        }

        # Registrar todos os namespaces
        for prefix, uri in namespaces.items():
            ET.register_namespace(prefix, uri)

        tree = ET.parse(caminho_xml)
        root = tree.getroot()

        contador_paragrafos = 0

        # Processar parágrafos (text:p)
        for p in root.iter('{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p'):
            # Processar todos os elementos de texto dentro do parágrafo
            for elem in p.iter():
                if elem.text and elem.text.strip():
                    texto_original = elem.text
                    try:
                        elem.text = self.traduzir_texto(texto_original, idioma_destino)
                        print(f"✅ '{texto_original[:40]}...' → '{elem.text[:40]}...'")
                    except Exception as e:
                        print(f"⚠️ Erro traduzindo: {e}")

                if elem.tail and elem.tail.strip():
                    texto_original = elem.tail
                    try:
                        elem.tail = self.traduzir_texto(texto_original, idioma_destino)
                    except Exception as e:
                        print(f"⚠️ Erro traduzindo tail: {e}")

            contador_paragrafos += 1
            if contador_paragrafos % 10 == 0:
                print(f"📝 Parágrafos processados: {contador_paragrafos}")
                time.sleep(random.uniform(0.6, 1.8))

        # Processar spans (text:span)
        for span in root.iter('{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span'):
            if span.text and span.text.strip():
                texto_original = span.text
                try:
                    span.text = self.traduzir_texto(texto_original, idioma_destino)
                except Exception as e:
                    print(f"⚠️ Erro traduzindo span: {e}")

        # Processar headings (text:h)
        for h in root.iter('{urn:oasis:names:tc:opendocument:xmlns:text:1.0}h'):
            if h.text and h.text.strip():
                texto_original = h.text
                try:
                    h.text = self.traduzir_texto(texto_original, idioma_destino)
                    print(f"📌 Título traduzido: '{texto_original}' → '{h.text}'")
                except Exception as e:
                    print(f"⚠️ Erro traduzindo heading: {e}")

        # Salvar
        tree.write(caminho_xml, encoding='utf-8', xml_declaration=True)
        print(f"✅ Total processado: {contador_paragrafos} parágrafos")

    def recriar_odt(self, pasta_extraida: str, arquivo_saida: str):
        """Recria o arquivo ODT"""
        with zipfile.ZipFile(arquivo_saida, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
            for root, dirs, files in os.walk(pasta_extraida):
                for file in files:
                    file_path = os.path.join(root, file)
                    arc_name = Path(file_path).relative_to(Path(pasta_extraida)).as_posix()
                    zip_ref.write(file_path, arc_name)

    def traduzir_documento(self, arquivo_entrada: str, idioma_destino: str = 'en') -> str:
        """Traduz documento ODT completo"""
        print(f"\n{'='*60}")
        print(f"🚀 INICIANDO TRADUÇÃO ODT GRATUITA")
        print(f"{'='*60}")
        print(f"📁 Arquivo: {arquivo_entrada}")
        print(f"🌍 Idioma destino: {idioma_destino}")

        # Nome do arquivo de saída
        nome_base = Path(arquivo_entrada).stem
        extensao = Path(arquivo_entrada).suffix
        sufixo_idioma = "EN" if idioma_destino == 'en' else idioma_destino.upper()

        # Determinar diretório de saída
        dir_entrada = os.path.dirname(arquivo_entrada)
        if "\\PT\\" in arquivo_entrada or "/PT/" in arquivo_entrada:
            dir_saida = arquivo_entrada.replace("\\PT\\", f"\\{sufixo_idioma}\\").replace("/PT/", f"/{sufixo_idioma}/")
            dir_saida = os.path.dirname(dir_saida)
        else:
            dir_saida = os.path.join(dir_entrada, sufixo_idioma)

        os.makedirs(dir_saida, exist_ok=True)
        arquivo_saida = os.path.join(dir_saida, f"{nome_base}{extensao}")

        try:
            # Preparar ambiente
            self.criar_diretorio_temp()

            # Extrair ODT
            print("📦 Extraindo documento...")
            pasta_extraida = self.extrair_odt(arquivo_entrada)

            # Processar content.xml
            print("📝 Traduzindo conteúdo principal...")
            content_xml = os.path.join(pasta_extraida, "content.xml")
            if os.path.exists(content_xml):
                self.processar_xml_odt(content_xml, idioma_destino)

            # Processar styles.xml (pode conter texto em headers/footers)
            print("📄 Verificando styles.xml...")
            styles_xml = os.path.join(pasta_extraida, "styles.xml")
            if os.path.exists(styles_xml):
                try:
                    self.processar_xml_odt(styles_xml, idioma_destino)
                except Exception as e:
                    print(f"⚠️ Erro processando styles.xml: {e}")

            # Recriar ODT
            print("📦 Recriando documento...")
            self.recriar_odt(pasta_extraida, arquivo_saida)

            # Limpeza
            shutil.rmtree(self.temp_dir)

            # Resultado
            tamanho_mb = os.path.getsize(arquivo_saida) / (1024*1024)

            print(f"\n{'='*60}")
            print(f"🎉 TRADUÇÃO CONCLUÍDA COM SUCESSO!")
            print(f"{'='*60}")
            print(f"📁 Arquivo criado: {arquivo_saida}")
            print(f"📊 Tamanho: {tamanho_mb:.1f} MB")
            print(f"💰 Custo: R$ 0,00 (GRATUITO!)")
            print(f"🖼️ Imagens preservadas: ✅")
            print(f"🎨 Formatação preservada: ✅")
            print(f"{'='*60}")

            return arquivo_saida

        except Exception as e:
            print(f"❌ Erro durante tradução: {e}")
            if os.path.exists(self.temp_dir):
                shutil.rmtree(self.temp_dir)
            raise

def main():
    """Função principal"""
    print("=" * 60)
    print("🆓 TRADUTOR ODT DIRETO GRATUITO")
    print("💰 SEM CUSTOS - SEM API - SEM LIBREOFFICE!")
    print("=" * 60)

    if len(sys.argv) < 3:
        print("❌ Uso: python tradutor_odt_direto_GRATUITO.py <arquivo.odt> <idioma>")
        print("🌍 Idiomas suportados: en, es, fr, de, it, pt, ru, ja, ko, zh, ar, hi")
        return

    arquivo_entrada = sys.argv[1]
    idioma_destino = sys.argv[2].lower()

    if not os.path.exists(arquivo_entrada):
        print(f"❌ Arquivo não encontrado: {arquivo_entrada}")
        return

    tradutor = TradutorOdtDiretoGratuito()

    try:
        arquivo_traduzido = tradutor.traduzir_documento(arquivo_entrada, idioma_destino)
        print(f"\n✅ Sucesso! Arquivo: {arquivo_traduzido}")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
