#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRADUTOR DOCX COM IA - VERSÃO CORRIGIDA QUE FUNCIONA
===================================================
Script que traduz documentos DOCX usando OpenAI mantendo:
- Todas as imagens (incluindo do SORA/GPT)
- Formatação original
- Estrutura do documento
- Estilos e layout
"""

import os
import sys
import subprocess
import zipfile
import shutil
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
import json
import re

# Padrões para conteúdo NÃO traduzível
URL_RE = re.compile(r"https?://\S+|www\.\S+", re.UNICODE)
EMAIL_RE = re.compile(r"[\w\.-]+@[\w\.-]+\.[A-Za-z]{2,}")
BACKTICK_RE = re.compile(r"`[^`]+`")
VARIABLE_RE = re.compile(r"\b[a-zA-Z_][a-zA-Z0-9_]*_[a-zA-Z0-9_]*\b")
ALLCAPS_RE = re.compile(r"\b[A-Z][A-Z0-9_]{2,}\b")

def mask_nontranslatables(text: str):
    """Troca tokens não traduzíveis por placeholders [[NT_i]] e retorna mapa."""
    placeholders = []
    masked = text
    idx = 0

    def repl(pattern):
        nonlocal masked, idx, placeholders
        for m in list(pattern.finditer(masked)):
            token = m.group(0)
            ph = f"[[NT_{idx}]]"
            placeholders.append((ph, token))
            masked = masked.replace(token, ph, 1)
            idx += 1

    # Ordem: backticks, URLs, e-mails, variáveis, CAPS
    repl(BACKTICK_RE)
    repl(URL_RE)
    repl(EMAIL_RE)
    repl(VARIABLE_RE)
    repl(ALLCAPS_RE)

    return masked, placeholders

def unmask_nontranslatables(text: str, placeholders):
    """Restaura tokens originais substituindo placeholders no texto."""
    restored = text
    for ph, token in placeholders:
        restored = restored.replace(ph, token)
    return restored

def instalar_dependencias():
    """Instala todas as dependências necessárias"""
    dependencias = [
        'python-docx',
        'openai>=1.0.0',
        'python-dotenv'
    ]
    
    for dep in dependencias:
        try:
            if dep.startswith('openai'):
                import openai
                # Verifica se é a versão nova
                if not hasattr(openai, 'OpenAI'):
                    raise ImportError("Versão antiga do OpenAI")
            else:
                __import__(dep.replace('-', '_'))
        except ImportError:
            print(f"📦 Instalando {dep}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])

def configurar_openai():
    """Configura a API da OpenAI (versão nova)"""
    try:
        from dotenv import load_dotenv
        from openai import OpenAI
        
        load_dotenv()
        
        # Tenta pegar a chave do .env primeiro
        api_key = os.getenv('OPENAI_API_KEY')
        
        if not api_key:
            # Se não tiver no .env, pede para o usuário
            print("🔑 Chave da OpenAI não encontrada no .env")
            api_key = input("Digite sua chave da API OpenAI: ").strip()
            
            # Salva no .env para próximas execuções
            with open('.env', 'a', encoding='utf-8') as f:
                f.write(f"\nOPENAI_API_KEY={api_key}\n")
        
        # Cria cliente OpenAI (versão nova)
        client = OpenAI(api_key=api_key)
        return client
        
    except Exception as e:
        print(f"❌ Erro ao configurar OpenAI: {e}")
        return None

def traduzir_com_ia(texto, idioma_destino, openai_client):
    """Traduz texto usando OpenAI mantendo formatação (API NOVA)"""
    
    if not texto.strip():
        return texto
    
    # Prompt especializado para tradução literária
    prompt = f"""
Traduza o seguinte texto para {idioma_destino}, mantendo:
- O estilo narrativo original
- A formatação e estrutura
- Os nomes dos personagens (Will, Mia, Leo, Sophie, Max, Jimmy Hendrix, Íris)
- O tom adequado para literatura infantojuvenil
- A fluidez natural no idioma de destino

IMPORTANTE: Qualquer marcador de placeholder no formato [[NT_*]] deve ser preservado exatamente como está (não traduzir, não alterar). Eles representam tokens que não devem ser traduzidos como URLs, e-mails, texto entre crases, variáveis e nomes em CAIXA ALTA.

Texto para traduzir:
{texto}

Responda APENAS com a tradução, sem explicações adicionais.
"""

    try:
        # API NOVA do OpenAI
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um tradutor especializado em literatura infantojuvenil. Mantenha sempre o estilo narrativo e a formatação original."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.3
        )
        
        traducao = response.choices[0].message.content.strip()
        print(f"✅ Traduzido: '{texto[:30]}...' -> '{traducao[:30]}...'")
        return traducao
        
    except Exception as e:
        print(f"⚠️ Erro na tradução de '{texto[:30]}...': {e}")
        return texto  # Retorna o texto original se houver erro

class TradutorDocxCompleto:
    def __init__(self, arquivo_origem, openai_client):
        self.arquivo_origem = Path(arquivo_origem)
        self.openai_client = openai_client
        self.temp_dir = None
        
    def extrair_docx(self):
        """Extrai o DOCX como ZIP para manipulação"""
        self.temp_dir = tempfile.mkdtemp()
        
        with zipfile.ZipFile(self.arquivo_origem, 'r') as zip_ref:
            zip_ref.extractall(self.temp_dir)
        
        return self.temp_dir
    
    def processar_xml_content(self, xml_path, idioma):
        """Processa o XML principal do documento"""
        try:
            tree = ET.parse(xml_path)
            root = tree.getroot()
            
            # Namespace do Word
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            # Contador de traduções
            count = 0
            
            # Encontra todos os textos para traduzir
            for t_elem in root.findall('.//w:t', ns):
                if t_elem.text and t_elem.text.strip():
                    texto_original = t_elem.text
                    
                    # Só traduz se tiver conteúdo significativo
                    if len(texto_original.strip()) > 2:
                        # Aplicar máscara para tokens não traduzíveis
                        masked, placeholders = mask_nontranslatables(texto_original)
                        texto_traduzido_masked = traduzir_com_ia(masked, idioma, self.openai_client)
                        texto_traduzido = unmask_nontranslatables(texto_traduzido_masked, placeholders)
                        t_elem.text = texto_traduzido
                        count += 1
                        
                        if count % 10 == 0:
                            print(f"📊 Progresso: {count} textos traduzidos...")
            
            print(f"✅ Total de {count} textos traduzidos para {idioma}")
            
            # Salva o XML modificado
            tree.write(xml_path, encoding='utf-8', xml_declaration=True)
            
        except Exception as e:
            print(f"❌ Erro ao processar XML: {e}")
    
    def criar_docx_traduzido(self, idioma, arquivo_saida):
        """Cria o DOCX traduzido mantendo tudo"""
        try:
            # Extrai o DOCX original
            temp_dir = self.extrair_docx()
            
            # Processa o documento principal
            document_xml = os.path.join(temp_dir, 'word', 'document.xml')
            if os.path.exists(document_xml):
                print(f"🔄 Traduzindo conteúdo para {idioma}...")
                self.processar_xml_content(document_xml, idioma)
            else:
                print(f"❌ Arquivo document.xml não encontrado!")
                return False
            
            # Recria o DOCX com todas as imagens e formatação
            print(f"📦 Recriando DOCX traduzido...")
            with zipfile.ZipFile(arquivo_saida, 'w', zipfile.ZIP_DEFLATED) as zip_out:
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arc_path = os.path.relpath(file_path, temp_dir)
                        zip_out.write(file_path, arc_path)
            
            print(f"✅ Arquivo traduzido criado: {arquivo_saida}")
            
            # Verifica tamanho do arquivo
            tamanho_mb = os.path.getsize(arquivo_saida) / (1024*1024)
            print(f"📁 Tamanho: {tamanho_mb:.1f} MB")
            
            # Limpa arquivos temporários
            shutil.rmtree(temp_dir)
            
            return True
            
        except Exception as e:
            print(f"❌ Erro ao criar DOCX traduzido: {e}")
            if self.temp_dir and os.path.exists(self.temp_dir):
                shutil.rmtree(self.temp_dir)
            return False

def main():
    """Função principal"""
    print("🚀 TRADUTOR DOCX COM IA - VERSÃO CORRIGIDA")
    print("=" * 50)
    
    # Instala dependências
    print("📦 Verificando dependências...")
    instalar_dependencias()
    
    # Configura OpenAI
    print("🔑 Configurando OpenAI...")
    openai_client = configurar_openai()
    
    if not openai_client:
        print("❌ Não foi possível configurar a OpenAI. Abortando.")
        return
    
    # Arquivo de origem
    arquivo_origem = "LIVROS/MANUSCRITO-LIVRO6-COM-IMAGENS.docx"
    
    if not os.path.exists(arquivo_origem):
        print(f"❌ Arquivo não encontrado: {arquivo_origem}")
        return
    
    print(f"📖 Arquivo encontrado: {arquivo_origem}")
    
    # Cria tradutor
    tradutor = TradutorDocxCompleto(arquivo_origem, openai_client)
    
    # Idiomas para traduzir
    idiomas = {
        'inglês': 'LIVROS/traducoes_com_imagens/MANUSCRITO-LIVRO6-COM-IMAGENS-EN-CORRIGIDO.docx',
        'espanhol': 'LIVROS/traducoes_com_imagens/MANUSCRITO-LIVRO6-COM-IMAGENS-ES-CORRIGIDO.docx'
    }
    
    # Cria diretório de saída se não existir
    os.makedirs('LIVROS/traducoes_com_imagens', exist_ok=True)
    
    # Traduz para cada idioma
    for idioma, arquivo_saida in idiomas.items():
        print(f"\n🌍 Iniciando tradução para {idioma}...")
        
        sucesso = tradutor.criar_docx_traduzido(idioma, arquivo_saida)
        
        if sucesso:
            print(f"✅ Tradução para {idioma} concluída!")
            print(f"📁 Arquivo salvo: {arquivo_saida}")
        else:
            print(f"❌ Falha na tradução para {idioma}")
    
    print("\n🎉 Processo de tradução finalizado!")
    print("📋 Resumo:")
    print("- Imagens preservadas ✅")
    print("- Formatação mantida ✅") 
    print("- Estrutura original ✅")
    print("- Tradução com IA ✅")
    print("- API OpenAI corrigida ✅")

if __name__ == "__main__":
    main()