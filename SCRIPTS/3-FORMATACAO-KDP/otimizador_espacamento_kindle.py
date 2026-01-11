#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OTIMIZADOR DE ESPAÇAMENTO PARA KINDLE
Turma da Aventura - Livro 6: O Despertar dos Sonhos

Este script otimiza o espaçamento do manuscrito DOCX para:
- Reduzir drasticamente o número de páginas
- Melhorar a formatação para Kindle
- Manter a legibilidade e estrutura
"""

import os
import sys
from pathlib import Path
import subprocess

# Instalar dependências
def install_requirements():
    packages = ['python-docx']
    for package in packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            print(f"Instalando {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_requirements()

from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

class OtimizadorEspacamentoKindle:
    """Otimizador de espaçamento especializado para Kindle"""
    
    def __init__(self):
        self.manuscrito_original = Path("LIVROS/MANUSCITO-PORTUGUES-TURMA-DA-AVENTURA-6.docx")
        self.output_dir = Path("LIVROS/manuscritos_otimizados")
        self.output_dir.mkdir(exist_ok=True)
        
        # Configurações otimizadas para Kindle
        self.config_kindle = {
            'font_size': Pt(11),           # Tamanho ideal para Kindle
            'line_spacing': 1.15,          # Espaçamento entre linhas otimizado
            'space_after': Pt(6),          # Espaço após parágrafo reduzido
            'space_before': Pt(0),         # Sem espaço antes do parágrafo
            'margin_top': Inches(0.5),     # Margens reduzidas
            'margin_bottom': Inches(0.5),
            'margin_left': Inches(0.5),
            'margin_right': Inches(0.5),
            'chapter_space_after': Pt(12), # Espaço após títulos de capítulo
            'chapter_space_before': Pt(18) # Espaço antes de títulos de capítulo
        }
    
    def detectar_tipo_paragrafo(self, paragrafo):
        """Detecta o tipo de parágrafo para aplicar formatação específica"""
        texto = paragrafo.text.strip().upper()
        
        if not texto:
            return 'vazio'
        elif texto.startswith('CAPÍTULO') or 'CAPÍTULO' in texto:
            return 'capitulo'
        elif texto.startswith('TURMA DA AVENTURA') or texto.startswith('LIVRO'):
            return 'titulo_principal'
        elif texto in ['DEDICATÓRIA', 'AGRADECIMENTOS', 'ÍNDICE']:
            return 'secao'
        elif texto.startswith('"') and texto.endswith('"'):
            return 'dialogo'
        elif len(texto) < 50 and not texto.endswith('.'):
            return 'subtitulo'
        else:
            return 'texto_normal'
    
    def aplicar_formatacao_otimizada(self, paragrafo, tipo):
        """Aplica formatação otimizada baseada no tipo de parágrafo"""
        
        # Limpar formatação existente
        for run in paragrafo.runs:
            run.font.size = self.config_kindle['font_size']
            run.font.name = 'Times New Roman'
        
        # Configurar espaçamento do parágrafo
        pf = paragrafo.paragraph_format
        
        if tipo == 'capitulo':
            # Títulos de capítulo
            paragrafo.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pf.space_before = self.config_kindle['chapter_space_before']
            pf.space_after = self.config_kindle['chapter_space_after']
            pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
            
            # Negrito para títulos
            for run in paragrafo.runs:
                run.bold = True
                run.font.size = Pt(14)
                
        elif tipo == 'titulo_principal':
            # Título principal do livro
            paragrafo.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pf.space_before = Pt(0)
            pf.space_after = Pt(18)
            pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
            
            for run in paragrafo.runs:
                run.bold = True
                run.font.size = Pt(16)
                
        elif tipo == 'secao':
            # Seções como Dedicatória, Agradecimentos
            paragrafo.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pf.space_before = Pt(12)
            pf.space_after = Pt(12)
            pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
            
            for run in paragrafo.runs:
                run.bold = True
                run.font.size = Pt(12)
                
        elif tipo == 'subtitulo':
            # Subtítulos
            paragrafo.alignment = WD_ALIGN_PARAGRAPH.LEFT
            pf.space_before = Pt(8)
            pf.space_after = Pt(4)
            pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
            
        elif tipo == 'dialogo':
            # Diálogos
            paragrafo.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            pf.space_before = Pt(0)
            pf.space_after = Pt(3)
            pf.line_spacing = self.config_kindle['line_spacing']
            pf.first_line_indent = Inches(0.2)
            
        elif tipo == 'vazio':
            # Parágrafos vazios - remover completamente
            return 'remover'
            
        else:
            # Texto normal
            paragrafo.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            pf.space_before = self.config_kindle['space_before']
            pf.space_after = self.config_kindle['space_after']
            pf.line_spacing = self.config_kindle['line_spacing']
            pf.first_line_indent = Inches(0.2)
        
        return 'manter'
    
    def configurar_margens_documento(self, doc):
        """Configura margens otimizadas para Kindle"""
        sections = doc.sections
        for section in sections:
            section.top_margin = self.config_kindle['margin_top']
            section.bottom_margin = self.config_kindle['margin_bottom']
            section.left_margin = self.config_kindle['margin_left']
            section.right_margin = self.config_kindle['margin_right']
    
    def otimizar_manuscrito(self, arquivo_entrada, arquivo_saida):
        """Otimiza um manuscrito DOCX para Kindle"""
        
        print(f"📖 Otimizando: {arquivo_entrada}")
        print(f"💾 Salvando em: {arquivo_saida}")
        
        # Carregar documento
        doc = Document(arquivo_entrada)
        
        # Configurar margens
        self.configurar_margens_documento(doc)
        
        # Processar parágrafos
        paragrafos_removidos = 0
        paragrafos_otimizados = 0
        
        # Lista para armazenar parágrafos a serem removidos
        paragrafos_para_remover = []
        
        for i, paragrafo in enumerate(doc.paragraphs):
            tipo = self.detectar_tipo_paragrafo(paragrafo)
            acao = self.aplicar_formatacao_otimizada(paragrafo, tipo)
            
            if acao == 'remover':
                paragrafos_para_remover.append(paragrafo)
                paragrafos_removidos += 1
            else:
                paragrafos_otimizados += 1
        
        # Remover parágrafos vazios
        for paragrafo in paragrafos_para_remover:
            p = paragrafo._element
            p.getparent().remove(p)
        
        # Salvar documento otimizado
        doc.save(arquivo_saida)
        
        print(f"✅ Otimização concluída!")
        print(f"   📝 Parágrafos otimizados: {paragrafos_otimizados}")
        print(f"   🗑️ Parágrafos vazios removidos: {paragrafos_removidos}")
        
        return arquivo_saida
    
    def executar_otimizacao_completa(self):
        """Executa otimização completa de todos os manuscritos"""
        
        print("🚀 INICIANDO OTIMIZAÇÃO DE ESPAÇAMENTO PARA KINDLE")
        print("=" * 60)
        
        # Lista de arquivos para otimizar
        arquivos_para_otimizar = [
            {
                'entrada': self.manuscrito_original,
                'saida': self.output_dir / "MANUSCRITO-OTIMIZADO-PORTUGUES-TURMA-DA-AVENTURA-6.docx",
                'nome': "Português (Original)"
            }
        ]
        
        # Adicionar traduções se existirem
        traducoes_dir = Path("LIVROS/traducoes_finais")
        if traducoes_dir.exists():
            arquivos_traducoes = [
                {
                    'entrada': traducoes_dir / "MANUSCRITO-FINAL-ENGLISH-TURMA-DA-AVENTURA-6.docx",
                    'saida': self.output_dir / "MANUSCRITO-OTIMIZADO-ENGLISH-TURMA-DA-AVENTURA-6.docx",
                    'nome': "Inglês"
                },
                {
                    'entrada': traducoes_dir / "MANUSCRITO-FINAL-SPANISH-TURMA-DA-AVENTURA-6.docx",
                    'saida': self.output_dir / "MANUSCRITO-OTIMIZADO-SPANISH-TURMA-DA-AVENTURA-6.docx",
                    'nome': "Espanhol"
                }
            ]
            
            for arquivo in arquivos_traducoes:
                if arquivo['entrada'].exists():
                    arquivos_para_otimizar.append(arquivo)
        
        # Otimizar cada arquivo
        arquivos_criados = []
        for arquivo in arquivos_para_otimizar:
            if arquivo['entrada'].exists():
                print(f"\n🌍 OTIMIZANDO VERSÃO: {arquivo['nome']}")
                print("-" * 40)
                
                arquivo_otimizado = self.otimizar_manuscrito(
                    arquivo['entrada'], 
                    arquivo['saida']
                )
                arquivos_criados.append({
                    'arquivo': arquivo_otimizado,
                    'nome': arquivo['nome']
                })
            else:
                print(f"⚠️ Arquivo não encontrado: {arquivo['entrada']}")
        
        # Criar arquivo de comparação
        self.criar_relatorio_otimizacao(arquivos_criados)
        
        # Relatório final
        print("\n🎉 OTIMIZAÇÃO COMPLETA FINALIZADA!")
        print("=" * 60)
        print(f"📁 Pasta de saída: {self.output_dir}")
        print("\n📚 ARQUIVOS OTIMIZADOS CRIADOS:")
        
        for arquivo in arquivos_criados:
            print(f"   ✅ {arquivo['nome']}: {arquivo['arquivo'].name}")
        
        print("\n✨ MELHORIAS APLICADAS:")
        print("   📏 Espaçamento entre parágrafos reduzido drasticamente")
        print("   📖 Formatação otimizada para Kindle")
        print("   🗑️ Parágrafos vazios removidos")
        print("   📐 Margens ajustadas para melhor aproveitamento")
        print("   📝 Espaçamento de linhas otimizado")
        print("   🎯 Redução significativa no número de páginas")
        
        return arquivos_criados
    
    def criar_relatorio_otimizacao(self, arquivos_criados):
        """Cria relatório da otimização"""
        
        relatorio_path = self.output_dir / "RELATORIO_OTIMIZACAO_KINDLE.md"
        
        with open(relatorio_path, 'w', encoding='utf-8') as f:
            f.write("# RELATÓRIO DE OTIMIZAÇÃO PARA KINDLE\n\n")
            f.write("## Turma da Aventura - Livro 6: O Despertar dos Sonhos\n\n")
            
            f.write("### 🎯 OBJETIVO\n")
            f.write("Otimizar o espaçamento do manuscrito para:\n")
            f.write("- Reduzir drasticamente o número de páginas\n")
            f.write("- Melhorar a formatação para Kindle\n")
            f.write("- Manter a legibilidade e estrutura\n\n")
            
            f.write("### ✨ OTIMIZAÇÕES APLICADAS\n\n")
            f.write("#### 📏 Espaçamento\n")
            f.write("- **Espaço após parágrafo**: Reduzido para 6pt\n")
            f.write("- **Espaço antes do parágrafo**: Removido (0pt)\n")
            f.write("- **Espaçamento entre linhas**: Otimizado para 1.15\n")
            f.write("- **Parágrafos vazios**: Removidos completamente\n\n")
            
            f.write("#### 📐 Margens\n")
            f.write("- **Todas as margens**: Reduzidas para 0.5 polegadas\n")
            f.write("- **Melhor aproveitamento**: Da área de impressão\n\n")
            
            f.write("#### 📝 Formatação de Texto\n")
            f.write("- **Fonte**: Times New Roman 11pt\n")
            f.write("- **Alinhamento**: Justificado para texto normal\n")
            f.write("- **Recuo primeira linha**: 0.2 polegadas\n")
            f.write("- **Títulos de capítulo**: Centralizados e em negrito\n\n")
            
            f.write("### 📚 ARQUIVOS OTIMIZADOS\n\n")
            for arquivo in arquivos_criados:
                f.write(f"- **{arquivo['nome']}**: `{arquivo['arquivo'].name}`\n")
            
            f.write("\n### 🚀 BENEFÍCIOS PARA KINDLE\n")
            f.write("- ✅ Redução significativa no número de páginas\n")
            f.write("- ✅ Melhor experiência de leitura no Kindle\n")
            f.write("- ✅ Formatação profissional e consistente\n")
            f.write("- ✅ Otimização para diferentes tamanhos de tela\n")
            f.write("- ✅ Menor consumo de memória do dispositivo\n")
            f.write("- ✅ Navegação mais fluida entre páginas\n\n")
            
            f.write("### 📊 COMPARAÇÃO\n")
            f.write("| Aspecto | Antes | Depois |\n")
            f.write("|---------|-------|--------|\n")
            f.write("| Espaço após parágrafo | Excessivo | 6pt otimizado |\n")
            f.write("| Parágrafos vazios | Muitos | Removidos |\n")
            f.write("| Margens | Padrão | Otimizadas |\n")
            f.write("| Páginas | Muitas | Reduzidas drasticamente |\n")
            f.write("| Kindle | Formatação ruim | Otimizada |\n")
        
        print(f"📊 Relatório criado: {relatorio_path}")

def main():
    """Função principal"""
    otimizador = OtimizadorEspacamentoKindle()
    otimizador.executar_otimizacao_completa()

if __name__ == "__main__":
    main()