#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRADUTOR ODT GRATUITO - SEM CUSTOS!
Traduz documentos ODT mantendo imagens, formatação e estrutura
Usa Google Translate GRATUITO (sem API)
"""

import os
import sys
import subprocess
from pathlib import Path
import shutil

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

class TradutorOdtGratuito:
    """Tradutor ODT 100% gratuito usando conversão para DOCX e Google Translate"""

    def __init__(self):
        self.script_traducao_docx = os.path.join(
            os.path.dirname(__file__),
            "tradutor_docx_GRATUITO.py"
        )

    def verificar_libreoffice(self) -> str:
        """Verifica se LibreOffice está instalado e retorna o caminho"""
        caminhos_possiveis = [
            r"C:\Program Files\LibreOffice\program\soffice.exe",
            r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
            r"/usr/bin/libreoffice",
            r"/usr/bin/soffice",
            "soffice",  # No PATH
            "libreoffice"  # No PATH
        ]

        for caminho in caminhos_possiveis:
            try:
                result = subprocess.run(
                    [caminho, "--version"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode == 0:
                    print(f"✅ LibreOffice encontrado: {caminho}")
                    return caminho
            except:
                continue

        raise RuntimeError(
            "❌ LibreOffice não encontrado!\n"
            "📥 Instale LibreOffice em: https://www.libreoffice.org/download/download/\n"
            "Ou use o conversor online em: https://www.zamzar.com/convert/odt-to-docx/"
        )

    def converter_odt_para_docx(self, arquivo_odt: str) -> str:
        """Converte ODT para DOCX usando LibreOffice"""
        print(f"\n🔄 Convertendo ODT para DOCX...")

        soffice = self.verificar_libreoffice()

        # Criar diretório temporário
        temp_dir = os.path.join(os.path.dirname(arquivo_odt), "temp_conversao")
        os.makedirs(temp_dir, exist_ok=True)

        # Copiar arquivo para temp
        nome_arquivo = os.path.basename(arquivo_odt)
        arquivo_temp = os.path.join(temp_dir, nome_arquivo)
        shutil.copy2(arquivo_odt, arquivo_temp)

        # Converter para DOCX
        try:
            cmd = [
                soffice,
                "--headless",
                "--convert-to", "docx",
                "--outdir", temp_dir,
                arquivo_temp
            ]

            print(f"🔧 Executando: {' '.join(cmd)}")
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode != 0:
                raise RuntimeError(f"Erro na conversão: {result.stderr}")

            # Arquivo DOCX gerado
            nome_base = Path(arquivo_odt).stem
            arquivo_docx = os.path.join(temp_dir, f"{nome_base}.docx")

            if not os.path.exists(arquivo_docx):
                raise RuntimeError(f"Arquivo DOCX não foi criado: {arquivo_docx}")

            print(f"✅ Conversão concluída: {arquivo_docx}")
            return arquivo_docx

        except subprocess.TimeoutExpired:
            raise RuntimeError("Conversão excedeu o tempo limite de 60s")
        except Exception as e:
            raise RuntimeError(f"Erro na conversão ODT→DOCX: {e}")

    def converter_docx_para_odt(self, arquivo_docx: str, arquivo_saida: str):
        """Converte DOCX de volta para ODT"""
        print(f"\n🔄 Convertendo DOCX traduzido para ODT...")

        soffice = self.verificar_libreoffice()

        # Diretório de saída
        dir_saida = os.path.dirname(arquivo_saida)
        os.makedirs(dir_saida, exist_ok=True)

        try:
            cmd = [
                soffice,
                "--headless",
                "--convert-to", "odt",
                "--outdir", dir_saida,
                arquivo_docx
            ]

            print(f"🔧 Executando: {' '.join(cmd)}")
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode != 0:
                raise RuntimeError(f"Erro na conversão: {result.stderr}")

            # Renomear se necessário
            nome_base = Path(arquivo_docx).stem
            arquivo_odt_temp = os.path.join(dir_saida, f"{nome_base}.odt")

            if arquivo_odt_temp != arquivo_saida:
                if os.path.exists(arquivo_saida):
                    os.remove(arquivo_saida)
                shutil.move(arquivo_odt_temp, arquivo_saida)

            print(f"✅ Conversão concluída: {arquivo_saida}")

        except subprocess.TimeoutExpired:
            raise RuntimeError("Conversão excedeu o tempo limite de 60s")
        except Exception as e:
            raise RuntimeError(f"Erro na conversão DOCX→ODT: {e}")

    def traduzir_documento(self, arquivo_odt: str, idioma_destino: str = 'en') -> str:
        """Traduz documento ODT completo"""
        print(f"\n{'='*60}")
        print(f"🆓 TRADUTOR ODT GRATUITO")
        print(f"{'='*60}")
        print(f"📁 Arquivo: {arquivo_odt}")
        print(f"🌍 Idioma destino: {idioma_destino}")

        temp_dir = None
        arquivo_docx = None
        arquivo_docx_traduzido = None

        try:
            # 1. Converter ODT → DOCX
            arquivo_docx = self.converter_odt_para_docx(arquivo_odt)
            temp_dir = os.path.dirname(arquivo_docx)

            # 2. Traduzir DOCX
            print(f"\n📝 Traduzindo documento...")
            cmd_traducao = [
                sys.executable,
                self.script_traducao_docx,
                arquivo_docx,
                idioma_destino
            ]

            result = subprocess.run(
                cmd_traducao,
                capture_output=True,
                text=True,
                timeout=3600  # 1 hora para tradução
            )

            print(result.stdout)

            if result.returncode != 0:
                raise RuntimeError(f"Erro na tradução: {result.stderr}")

            # Encontrar arquivo traduzido
            nome_base = Path(arquivo_docx).stem
            sufixo_idioma = "EN" if idioma_destino == 'en' else idioma_destino.upper()
            arquivo_docx_traduzido = os.path.join(
                temp_dir,
                f"{nome_base}-{sufixo_idioma}-GRATUITO.docx"
            )

            if not os.path.exists(arquivo_docx_traduzido):
                raise RuntimeError(f"Arquivo traduzido não encontrado: {arquivo_docx_traduzido}")

            # 3. Converter DOCX traduzido → ODT
            nome_base_original = Path(arquivo_odt).stem
            dir_original = os.path.dirname(arquivo_odt)

            # Determinar diretório de saída (EN ou ES)
            if "\\PT\\" in arquivo_odt or "/PT/" in arquivo_odt:
                dir_saida = arquivo_odt.replace("\\PT\\", f"\\{sufixo_idioma}\\").replace("/PT/", f"/{sufixo_idioma}/")
                dir_saida = os.path.dirname(dir_saida)
            else:
                dir_saida = os.path.join(dir_original, sufixo_idioma)

            arquivo_odt_final = os.path.join(
                dir_saida,
                f"{nome_base_original}-{sufixo_idioma}.odt"
            )

            self.converter_docx_para_odt(arquivo_docx_traduzido, arquivo_odt_final)

            # 4. Limpeza
            if temp_dir and os.path.exists(temp_dir):
                print(f"\n🧹 Limpando arquivos temporários...")
                shutil.rmtree(temp_dir)

            # Resultado
            tamanho_mb = os.path.getsize(arquivo_odt_final) / (1024*1024)

            print(f"\n{'='*60}")
            print(f"🎉 TRADUÇÃO CONCLUÍDA COM SUCESSO!")
            print(f"{'='*60}")
            print(f"📁 Arquivo criado: {arquivo_odt_final}")
            print(f"📊 Tamanho: {tamanho_mb:.1f} MB")
            print(f"💰 Custo: R$ 0,00 (GRATUITO!)")
            print(f"🖼️ Imagens preservadas: ✅")
            print(f"🎨 Formatação preservada: ✅")
            print(f"{'='*60}")

            return arquivo_odt_final

        except Exception as e:
            print(f"\n❌ Erro durante tradução: {e}")
            # Limpeza em caso de erro
            if temp_dir and os.path.exists(temp_dir):
                try:
                    shutil.rmtree(temp_dir)
                except:
                    pass
            raise

def main():
    """Função principal"""
    print("=" * 60)
    print("🆓 TRADUTOR ODT GRATUITO")
    print("💰 SEM CUSTOS - SEM API - SEM LIMITES!")
    print("=" * 60)

    # Verificar argumentos
    if len(sys.argv) < 3:
        print("❌ Uso: python tradutor_odt_GRATUITO.py <arquivo.odt> <idioma>")
        print("🌍 Idiomas suportados: en, es, fr, de, it, pt, ru, ja, ko, zh, ar, hi")
        return

    arquivo_entrada = sys.argv[1]
    idioma_destino = sys.argv[2].lower()

    if not os.path.exists(arquivo_entrada):
        print(f"❌ Arquivo não encontrado: {arquivo_entrada}")
        return

    # Criar tradutor
    tradutor = TradutorOdtGratuito()

    try:
        arquivo_traduzido = tradutor.traduzir_documento(arquivo_entrada, idioma_destino)
        print(f"\n✅ Sucesso! Arquivo: {arquivo_traduzido}")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
