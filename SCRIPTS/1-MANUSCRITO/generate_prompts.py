import re
import json
import os

# Character Image Mappings
CHAR_IMAGES = {
    "Mia": "C:/Users/xberi/.gemini/antigravity/brain/1843a247-94ec-4459-9a22-0f002164fd27/uploaded_image_0_1766767177607.jpg",
    "Will": "C:/Users/xberi/.gemini/antigravity/brain/1843a247-94ec-4459-9a22-0f002164fd27/uploaded_image_1_1766767177607.jpg",
    "Marino": "C:/Users/xberi/.gemini/antigravity/brain/1843a247-94ec-4459-9a22-0f002164fd27/uploaded_image_2_1766767177607.jpg",
    "Professor": "C:/Users/xberi/.gemini/antigravity/brain/1843a247-94ec-4459-9a22-0f002164fd27/uploaded_image_2_1766767177607.jpg",
    "Jimmy": "C:/Users/xberi/.gemini/antigravity/brain/1843a247-94ec-4459-9a22-0f002164fd27/uploaded_image_3_1766767177607.jpg",
    "Leo": "C:/Users/xberi/.gemini/antigravity/brain/1843a247-94ec-4459-9a22-0f002164fd27/uploaded_image_4_1766767177607.jpg"
}

def get_relevant_images(text):
    """Finds characters in text and returns their reference image paths (max 3)."""
    found_images = []
    # Weighted search: prioritize names that appear earlier or are more central? 
    # For now, simple presence.
    
    # Check distinct key words
    if "Mia" in text: found_images.append(CHAR_IMAGES["Mia"])
    if "Will" in text: found_images.append(CHAR_IMAGES["Will"])
    if "Leo" in text: found_images.append(CHAR_IMAGES["Leo"])
    if "Jimmy" in text: found_images.append(CHAR_IMAGES["Jimmy"])
    if "Marino" in text or "Professor" in text: found_images.append(CHAR_IMAGES["Marino"])
    
    # Remove duplicates if any (e.g. Marino/Professor mapping to same)
    found_images = list(dict.fromkeys(found_images))
    
    # Limit to 3 images
    return found_images[:3]

def generate_prompts(filepath, output_dir):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by chapters
    chapter_pattern = r'(CAPÍTULO \d+:.*?)(?=(CAPÍTULO \d+:|$))'
    chapters = re.findall(chapter_pattern, content, re.DOTALL)
    
    prompts = []
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, (chap_content, _) in enumerate(chapters, 1):
        lines = chap_content.strip().split('\n')
        chapter_title = lines[0].strip()
        
        # Split by separator ---
        sections = chap_content.split('---')
        
        for j, section in enumerate(sections):
            text = section.strip()
            if j == 0:
                text = text.replace(chapter_title, '').strip()

            scene_description = text[:600].replace('\n', ' ')
            
            # Determine reference images
            ref_images = get_relevant_images(text)
            
            # Refined prompt for consistency
            prompt = (
                f"Digital art style, 3D animated movie style, Pixar style. High quality render. "
                f"Scene from book chapter '{chapter_title}'. "
                f"Context: {scene_description}... "
                f"Keep character designs STRICTLY consistent with the provided reference images. "
                f"Vibrant colors, cinematic lighting."
            )
            
            image_filename = f"chapter_{i}_topic_{j+1}.png"
            prompts.append({
                "filename": image_filename,
                "prompt": prompt,
                "chapter": i,
                "topic": j+1,
                "image_paths": ref_images
            })

    output_path = os.path.join(output_dir, 'prompts_v2.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(prompts, f, indent=4, ensure_ascii=False)
    
    print(f"Generated {len(prompts)} prompts with image references in {output_path}")

if __name__ == "__main__":
    generate_prompts(
        'd:\\TRAE-PROJETOS\\livro1\\BIZANTINO\\manuscrito.txt',
        'd:\\TRAE-PROJETOS\\livro1\\BIZANTINO\\images'
    )
