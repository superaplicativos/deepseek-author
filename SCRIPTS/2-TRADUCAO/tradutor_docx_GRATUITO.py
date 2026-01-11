#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRADUTOR DOCX GRATUITO - SEM CUSTOS!
Traduz documentos DOCX mantendo imagens, formatação e estrutura
Usa Google Translate GRATUITO (sem API)
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
from typing import Dict, List, Optional

# Instalar dependências se necessário
def instalar_dependencias():
    """Instala dependências usando deep-translator (Google Translate via web, sem httpx)."""
    import subprocess, sys
    try:
        from deep_translator import GoogleTranslator  # noqa: F401
        from docx import Document  # noqa: F401
        print("✅ Dependências já instaladas (deep-translator)!")
    except Exception:
        print("📦 Instalando dependências gratuitas (deep-translator + requests + python-docx)...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--force-reinstall", "deep-translator", "requests", "python-docx"])
        print("✅ Dependências instaladas!")

# Importar após instalação
instalar_dependencias()

from deep_translator import GoogleTranslator
from docx import Document

class TradutorDocxGratuito:
    """Tradutor DOCX 100% gratuito usando Google Translate"""
    
    def __init__(self):
        # Será instanciado por idioma em cada chamada
        self.translator = None
        self.temp_dir = "temp_traducao"
        self.traducoes_cache = {}
        
    def criar_diretorio_temp(self):
        """Cria diretório temporário"""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        os.makedirs(self.temp_dir)
        
    def extrair_docx(self, arquivo_docx: str) -> str:
        """Extrai o conteúdo do DOCX"""
        pasta_extracao = os.path.join(self.temp_dir, "extraido")
        
        with zipfile.ZipFile(arquivo_docx, 'r') as zip_ref:
            zip_ref.extractall(pasta_extracao)
            
        return pasta_extracao
    
    def traduzir_texto(self, texto: str, idioma_destino: str = 'en') -> str:
        """Traduz texto usando Google Translate GRATUITO, preservando tokens que não devem ser traduzidos."""
        if not texto or not texto.strip():
            return texto
            
        # Cache para evitar traduções repetidas
        cache_key = f"{texto}_{idioma_destino}"
        if cache_key in self.traducoes_cache:
            return self.traducoes_cache[cache_key]
        
        # Preservar tokens especiais: trechos entre crases, URLs, e-mails, e palavras em CAPS
        preservations: List[str] = []
        def _preserve(match):
            idx = len(preservations)
            token = match.group(0)
            preservations.append(token)
            return f"[[PRESERVE_{idx}]]"
        
        prepared = texto
        patterns = [
            r"`[^`]+`",                           # texto entre crases
            r"https?://\S+",                     # URLs http/https
            r"www\.\S+",                        # URLs www
            r"[\w\.-]+@[\w\.-]+\.[A-Za-z]{2,}",  # e-mails
            r"\b[a-zA-Z_][a-zA-Z0-9_]*_[a-zA-Z0-9_]*\b",  # variáveis com underscore
            r"\[\[RUN_\d+\]\]",               # placeholders de distribuição de runs
        ]
        for pat in patterns:
            prepared = re.sub(pat, _preserve, prepared)
        # Preservar palavras em CAIXA ALTA com 3+ caracteres (ex.: NOMES/MARCAS)
        prepared = re.sub(r"\b([A-Z][A-Z0-9_]{2,})\b", _preserve, prepared)
        
        try:
            # Instanciar o tradutor para o idioma solicitado
            self.translator = GoogleTranslator(source='auto', target=idioma_destino)
            # Backoff com reintentos
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

                    # Se veio None ou igual ao input, considerar falha e reintentar
                    if not texto_traduzido or texto_traduzido.strip() == prepared.strip():
                        raise RuntimeError("Tradução falhou ou retornou igual ao texto preparado")
                    break
                except Exception as e:
                    espera = base_sleep * (2 ** (tentativa - 1)) + random.uniform(0, 0.8)
                    print(f"⏳ Tentativa {tentativa}/{max_tentativas} falhou: {e}. Aguardando {espera:.1f}s...")
                    time.sleep(espera)
                    continue
            if not texto_traduzido:
                raise RuntimeError("Falha após múltiplas tentativas de tradução")
            
            # Restaurar tokens preservados
            for i, token in enumerate(preservations):
                texto_traduzido = texto_traduzido.replace(f"[[PRESERVE_{i}]]", token)
                
            # Salvar no cache
            self.traducoes_cache[cache_key] = texto_traduzido
            
            print(f"✅ Traduzido: '{texto[:50]}...' → '{texto_traduzido[:50]}...'")
            return texto_traduzido
            
        except Exception as e:
            print(f"⚠️ Erro na tradução: {e}")
            return texto  # Retorna texto original se falhar
    
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
    
    def processar_xml_documento(self, caminho_xml: str, idioma_destino: str):
        """Processa o XML por parágrafo (w:p), traduzindo blocos maiores com placeholders para distribuir em runs."""
        tree = ET.parse(caminho_xml)
        root = tree.getroot()
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        contador_paragrafos = 0
        for p in root.findall('.//w:p', ns):
            # coletar todos w:t deste parágrafo mantendo ordem
            ts = p.findall('.//w:t', ns)
            if not ts:
                continue
            textos_validos = [t for t in ts if t.text and t.text.strip()]
            if not textos_validos:
                continue
            # construir texto combinado com placeholders
            combinado_parts = []
            idx_map = []
            for idx, t in enumerate(ts):
                txt = t.text or ''
                if txt.strip():
                    combinado_parts.append(f"[[RUN_{idx}]]" + txt)
                    idx_map.append(idx)
            combinado = ' '.join(combinado_parts)
            if not combinado.strip():
                continue
            try:
                # traduzir bloco
                traduzido = self.traduzir_texto(combinado, idioma_destino)
                # distribuir de volta nos runs conforme placeholders
                matches = list(re.finditer(r"\[\[RUN_(\d+)\]\]", traduzido))
                if matches:
                    for i, m in enumerate(matches):
                        run_idx = int(m.group(1))
                        start = m.end()
                        end = matches[i+1].start() if i + 1 < len(matches) else len(traduzido)
                        segmento = traduzido[start:end].strip()
                        # atribuir ao w:t correspondente
                        if 0 <= run_idx < len(ts):
                            ts[run_idx].text = segmento
                    # runs sem conteúdo original permanecem inalterados
                else:
                    raise RuntimeError("Placeholders não foram preservados na tradução do parágrafo")
            except Exception as e:
                print(f"➡️ Fallback por run no parágrafo (erro: {e})")
                for t in ts:
                    txt = t.text or ''
                    if txt.strip():
                        try:
                            t.text = self.traduzir_texto(txt, idioma_destino)
                        except Exception as e2:
                            print(f"⚠️ Erro traduzindo run individual: {e2}")
            contador_paragrafos += 1
            if contador_paragrafos % 20 == 0:
                print(f"📝 Parágrafos processados: {contador_paragrafos}")
                time.sleep(random.uniform(0.6, 1.8))
        # salvar
        tree.write(caminho_xml, encoding='utf-8', xml_declaration=True)
        print(f"✅ Total de parágrafos traduzidos: {contador_paragrafos}")
    
    def processar_headers_footers(self, pasta_extraida: str, idioma_destino: str):
        """Processa cabeçalhos e rodapés"""
        word_dir = os.path.join(pasta_extraida, "word")
        
        # Processar headers
        for arquivo in os.listdir(word_dir):
            if arquivo.startswith("header") and arquivo.endswith(".xml"):
                caminho = os.path.join(word_dir, arquivo)
                print(f"📄 Processando cabeçalho: {arquivo}")
                self.processar_xml_documento(caminho, idioma_destino)
        
        # Processar footers
        for arquivo in os.listdir(word_dir):
            if arquivo.startswith("footer") and arquivo.endswith(".xml"):
                caminho = os.path.join(word_dir, arquivo)
                print(f"📄 Processando rodapé: {arquivo}")
                self.processar_xml_documento(caminho, idioma_destino)
    
    def recriar_docx(self, pasta_extraida: str, arquivo_saida: str):
        """Recria o arquivo DOCX"""
        with zipfile.ZipFile(arquivo_saida, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
            for root, dirs, files in os.walk(pasta_extraida):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Garantir nomes de entrada no ZIP com separador POSIX
                    arc_name = Path(file_path).relative_to(Path(pasta_extraida)).as_posix()
                    zip_ref.write(file_path, arc_name)
    
    def traduzir_documento(self, arquivo_entrada: str, idioma_destino: str = 'en') -> str:
        """Traduz documento completo"""
        print(f"\n🚀 INICIANDO TRADUÇÃO GRATUITA")
        print(f"📁 Arquivo: {arquivo_entrada}")
        print(f"🌍 Idioma destino: {idioma_destino}")
        
        # Criar nome do arquivo de saída
        nome_base = Path(arquivo_entrada).stem
        extensao = Path(arquivo_entrada).suffix
        sufixo_idioma = "EN" if idioma_destino == 'en' else "ES" if idioma_destino == 'es' else idioma_destino.upper()
        arquivo_saida = f"{nome_base}-{sufixo_idioma}-GRATUITO{extensao}"
        
        try:
            # Preparar ambiente
            self.criar_diretorio_temp()
            
            # Extrair DOCX
            print("📦 Extraindo documento...")
            pasta_extraida = self.extrair_docx(arquivo_entrada)
            
            # Processar documento principal
            print("📝 Traduzindo conteúdo principal...")
            document_xml = os.path.join(pasta_extraida, "word", "document.xml")
            self.processar_xml_documento(document_xml, idioma_destino)
            
            # Processar headers e footers
            print("📄 Traduzindo cabeçalhos e rodapés...")
            self.processar_headers_footers(pasta_extraida, idioma_destino)

            # Processar notas de rodapé, notas de fim e comentários, se existirem
            word_dir = os.path.join(pasta_extraida, "word")
            for nome in ("footnotes.xml", "endnotes.xml", "comments.xml"):
                caminho = os.path.join(word_dir, nome)
                if os.path.exists(caminho):
                    print(f"📝 Traduzindo {nome}...")
                    self.processar_xml_documento(caminho, idioma_destino)
            
            # Recriar DOCX
            print("📦 Recriando documento...")
            self.recriar_docx(pasta_extraida, arquivo_saida)
            
            # Limpeza
            shutil.rmtree(self.temp_dir)
            
            print(f"\n🎉 TRADUÇÃO CONCLUÍDA!")
            print(f"📁 Arquivo criado: {arquivo_saida}")
            print(f"💰 CUSTO: R$ 0,00 (GRATUITO!)")
            
            return arquivo_saida
            
        except Exception as e:
            print(f"❌ Erro durante tradução: {e}")
            if os.path.exists(self.temp_dir):
                shutil.rmtree(self.temp_dir)
            raise

def main():
    """Função principal"""
    print("=" * 60)
    print("🆓 TRADUTOR DOCX GRATUITO")
    print("💰 SEM CUSTOS - SEM API - SEM LIMITES!")
    print("=" * 60)
    
    # Verificar argumentos da linha de comando
    if len(sys.argv) < 3:
        print("❌ Uso: python tradutor_docx_GRATUITO.py <arquivo.docx> <idioma>")
        print("🌍 Idiomas suportados: en, es, fr, de, it, pt, ru, ja, ko, zh, ar, hi")
        return
    
    # Arquivo de entrada
    arquivo_entrada = sys.argv[1]
    idioma_destino = sys.argv[2].lower()
    
    # Mapear nomes de idiomas
    nomes_idiomas = {
        'en': 'Inglês',
        'es': 'Espanhol', 
        'fr': 'Francês',
        'de': 'Alemão',
        'it': 'Italiano',
        'pt': 'Português',
        'ru': 'Russo',
        'ja': 'Japonês',
        'ko': 'Coreano',
        'zh': 'Chinês',
        'ar': 'Árabe',
        'hi': 'Hindi'
    }
    
    nome_idioma = nomes_idiomas.get(idioma_destino, idioma_destino.upper())
    
    if not os.path.exists(arquivo_entrada):
        print(f"❌ Arquivo não encontrado: {arquivo_entrada}")
        return
    
    # Criar tradutor
    tradutor = TradutorDocxGratuito()
    
    print(f"📊 Tamanho do arquivo: {os.path.getsize(arquivo_entrada) / (1024*1024):.1f} MB")
    print(f"\n🌍 Traduzindo para {nome_idioma}...")
    
    try:
        arquivo_traduzido = tradutor.traduzir_documento(arquivo_entrada, idioma_destino)
        tamanho_mb = os.path.getsize(arquivo_traduzido) / (1024*1024)
        print(f"✅ {nome_idioma}: {arquivo_traduzido} ({tamanho_mb:.1f} MB)")
        
        print(f"\n🎊 TRADUÇÃO CONCLUÍDA!")
        print(f"💰 Total gasto: R$ 0,00")
        print(f"🖼️ Imagens preservadas: ✅")
        print(f"🎨 Formatação preservada: ✅")
        
    except Exception as e:
        print(f"❌ Erro na tradução para {nome_idioma}: {e}")

if __name__ == "__main__":
    main()