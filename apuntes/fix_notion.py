import os
import re

# Configuración
markdown_folder = "C:\\Users\\jpueyo\\Documents\\Github\\gitbook\\writeup-ctfs\\tryhackme"  # Carpeta donde están los .md

# Expresión regular para encontrar enlaces de imágenes en Markdown
image_pattern = re.compile(r'!\[(.*?)\]\((imagenes/[^\)]+)\)')

def fix_markdown_links(md_file):
    with open(md_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Reemplazar los enlaces de imágenes para que estén entre <>
    updated_content = image_pattern.sub(r'![\1](<\2>)', content)

    with open(md_file, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print(f"✅ Enlaces corregidos en: {md_file}")

# Recorrer todos los archivos .md en la carpeta y aplicar la corrección
for root, _, files in os.walk(markdown_folder):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            fix_markdown_links(file_path)

print("🎯 Todos los enlaces han sido corregidos.")
