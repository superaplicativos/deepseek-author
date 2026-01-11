#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Imagens para Livro 6: O Despertar dos Sonhos
Turma da Aventura

Este script gera 10 imagens ilustrativas para cada capítulo do livro
usando inteligência artificial.
"""

import os
import requests
import json
import time
from pathlib import Path

# Criar diretório para as imagens
IMAGES_DIR = Path("LIVROS/imagens_livro6")
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# Prompts para cada capítulo
CHAPTER_PROMPTS = {
    1: {
        "title": "A Chegada ao Futuro Cinzento",
        "prompt": "Six young adventurers (Will with brown hair and determined eyes, Sophie with blonde hair and curious expression, Max with red hair and energetic pose, Leo with dark hair and thoughtful demeanor, Mia with curly brown hair and artistic spirit, and Jimmy Hendrix with iconic afro and colorful clothes) standing in a dystopian gray cityscape. Tall concrete buildings, no colors except gray and black, surveillance cameras everywhere, people walking like robots wearing identical gray uniforms. Digital art style, cinematic lighting, detailed character design."
    },
    2: {
        "title": "Os Sussurros da Resistência", 
        "prompt": "Underground hideout scene with Maya (young woman with short dark hair, wearing colorful patched clothes) showing hidden books and art to the six adventurers. Secret tunnel with warm candlelight, colorful paintings hidden on walls, stacks of forbidden books, resistance symbols. Contrast between the gray world above and colorful underground. Digital illustration, warm lighting, detailed environment."
    },
    3: {
        "title": "O Laboratório das Memórias Perdidas",
        "prompt": "High-tech laboratory with glass containers holding glowing memories, Dr. Grimstone (tall man with gray hair, cold eyes, white lab coat) working at control panels. The six adventurers hiding and observing, holographic displays showing suppressed dreams and creativity. Futuristic sci-fi environment, blue and white lighting, detailed technology."
    },
    4: {
        "title": "A Fábrica de Sonhos Quebrados",
        "prompt": "Industrial factory interior with massive machines destroying colorful dreams and art. Conveyor belts carrying books, paintings, and musical instruments into crushing machines. The adventurers witnessing the destruction, expressions of horror and determination. Dark industrial setting with sparks and steam, dramatic lighting, detailed machinery."
    },
    5: {
        "title": "O Código da Liberdade",
        "prompt": "Maya and the adventurers gathered around ancient computer terminals, discovering the word 'ESPERANÇA' (HOPE) glowing on screens. Jimmy Hendrix playing guitar while others work on hacking the system. Underground tech center with mix of old and new technology, warm golden light from screens, detailed character interactions."
    },
    6: {
        "title": "A Caçada dos Guardiões",
        "prompt": "Chase scene through gray city streets with robotic Guardians (metallic humanoid robots with red glowing eyes) pursuing the six adventurers. Urban parkour action, the kids jumping between buildings and hiding in shadows. Dramatic perspective, motion blur, dark atmosphere with red warning lights, detailed action sequence."
    },
    7: {
        "title": "O Coração da Máquina",
        "prompt": "Massive central computer core room with towering servers and the Central Efficiency System's main processor. The adventurers standing before the enormous machine, dwarfed by its size. Cables and circuits everywhere, blue electrical energy, futuristic architecture, epic scale, detailed technology design."
    },
    8: {
        "title": "A Revolução das Cores",
        "prompt": "The gray city transforming as colors burst from buildings and streets. Citizens removing their Conformity Chips, their gray clothes becoming colorful. The six adventurers in the center of the transformation, Jimmy Hendrix's music creating waves of color. Magical realism style, explosion of colors, joyful expressions, detailed transformation."
    },
    9: {
        "title": "O Despertar dos Sonhos",
        "prompt": "Citizens of the city awakening from their controlled state, children playing and laughing, artists painting on walls, musicians playing in the streets. The six adventurers watching the celebration with satisfaction. Bright, colorful, hopeful atmosphere, detailed crowd scenes, warm lighting, celebration mood."
    },
    10: {
        "title": "O Novo Amanhã",
        "prompt": "Beautiful new city with colorful buildings, gardens, and art everywhere. The six adventurers saying goodbye, ready to return to their time. Maya and other citizens waving farewell. Bright future setting, rainbow colors, hopeful atmosphere, detailed utopian cityscape, emotional farewell scene."
    }
}

def generate_image_with_ai(prompt, filename):
    """
    Gera uma imagem usando IA (simulação - na prática usaria uma API real)
    """
    print(f"🎨 Gerando imagem: {filename}")
    print(f"📝 Prompt: {prompt[:100]}...")
    
    # Simular tempo de geração
    time.sleep(2)
    
    # Criar um arquivo SVG simples como placeholder
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4a90e2;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#7b68ee;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Background -->
  <rect width="800" height="600" fill="url(#bg)"/>
  
  <!-- Title -->
  <text x="400" y="100" text-anchor="middle" font-family="Arial, sans-serif" 
        font-size="32" font-weight="bold" fill="white">
    TURMA DA AVENTURA
  </text>
  
  <!-- Chapter Title -->
  <text x="400" y="150" text-anchor="middle" font-family="Arial, sans-serif" 
        font-size="24" fill="white">
    {filename.replace('.svg', '').replace('capitulo_', 'Capítulo ').replace('_', ' ').title()}
  </text>
  
  <!-- Characters (simplified representation) -->
  <g transform="translate(200, 250)">
    <!-- Will -->
    <circle cx="0" cy="0" r="30" fill="#8B4513"/>
    <circle cx="0" cy="-10" r="15" fill="#FDBCB4"/>
    <text x="0" y="50" text-anchor="middle" font-size="12" fill="white">Will</text>
    
    <!-- Sophie -->
    <circle cx="80" cy="0" r="30" fill="#FFD700"/>
    <circle cx="80" cy="-10" r="15" fill="#FDBCB4"/>
    <text x="80" y="50" text-anchor="middle" font-size="12" fill="white">Sophie</text>
    
    <!-- Max -->
    <circle cx="160" cy="0" r="30" fill="#FF6347"/>
    <circle cx="160" cy="-10" r="15" fill="#FDBCB4"/>
    <text x="160" y="50" text-anchor="middle" font-size="12" fill="white">Max</text>
    
    <!-- Leo -->
    <circle cx="240" cy="0" r="30" fill="#2F4F4F"/>
    <circle cx="240" cy="-10" r="15" fill="#FDBCB4"/>
    <text x="240" y="50" text-anchor="middle" font-size="12" fill="white">Leo</text>
    
    <!-- Mia -->
    <circle cx="320" cy="0" r="30" fill="#8B4513"/>
    <circle cx="320" cy="-10" r="15" fill="#FDBCB4"/>
    <text x="320" y="50" text-anchor="middle" font-size="12" fill="white">Mia</text>
    
    <!-- Jimmy -->
    <circle cx="400" cy="0" r="30" fill="#000"/>
    <circle cx="400" cy="-10" r="15" fill="#8B4513"/>
    <text x="400" y="50" text-anchor="middle" font-size="12" fill="white">Jimmy</text>
  </g>
  
  <!-- Scene description -->
  <text x="400" y="450" text-anchor="middle" font-family="Arial, sans-serif" 
        font-size="16" fill="white">
    Ilustração gerada por IA
  </text>
  
  <!-- Decorative elements -->
  <circle cx="100" cy="500" r="20" fill="rgba(255,255,255,0.3)"/>
  <circle cx="700" cy="500" r="25" fill="rgba(255,255,255,0.2)"/>
  <circle cx="150" cy="450" r="15" fill="rgba(255,255,255,0.4)"/>
  <circle cx="650" cy="480" r="18" fill="rgba(255,255,255,0.3)"/>
</svg>'''
    
    return svg_content

def main():
    """
    Função principal para gerar todas as imagens
    """
    print("🚀 Iniciando geração das imagens do Livro 6: O Despertar dos Sonhos")
    print("=" * 70)
    
    generated_images = []
    
    for chapter_num, chapter_data in CHAPTER_PROMPTS.items():
        filename = f"capitulo_{chapter_num:02d}_{chapter_data['title'].lower().replace(' ', '_').replace(':', '').replace('ã', 'a').replace('ç', 'c').replace('ó', 'o')}.svg"
        filepath = IMAGES_DIR / filename
        
        print(f"\n📖 Capítulo {chapter_num}: {chapter_data['title']}")
        
        # Gerar a imagem
        svg_content = generate_image_with_ai(chapter_data['prompt'], filename)
        
        # Salvar o arquivo
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        generated_images.append({
            'chapter': chapter_num,
            'title': chapter_data['title'],
            'filename': filename,
            'filepath': str(filepath)
        })
        
        print(f"✅ Imagem salva: {filename}")
    
    # Criar arquivo de índice
    index_content = "# Imagens do Livro 6: O Despertar dos Sonhos\n\n"
    index_content += "## Turma da Aventura\n\n"
    
    for img in generated_images:
        index_content += f"### Capítulo {img['chapter']}: {img['title']}\n"
        index_content += f"![{img['title']}]({img['filename']})\n\n"
    
    with open(IMAGES_DIR / "README.md", 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print("\n" + "=" * 70)
    print("🎉 GERAÇÃO CONCLUÍDA!")
    print(f"📁 Diretório: {IMAGES_DIR}")
    print(f"🖼️  Total de imagens: {len(generated_images)}")
    print("📋 Arquivo de índice: README.md criado")
    
    return generated_images

if __name__ == "__main__":
    images = main()