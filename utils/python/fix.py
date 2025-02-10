import os
import re
import shutil
import urllib.parse

# Configuración
markdown_folder = r"C:\Users\jpueyo\Documents\Github\Notion\Hack"  # Carpeta donde están los .md
image_folder = os.path.join(markdown_folder, "imagenes")  # Carpeta destino para imágenes

# Asegurar que la carpeta imagenes exista
os.makedirs(image_folder, exist_ok=True)

# Expresión regular para encontrar imágenes en los archivos .md
image_pattern = re.compile(r'!\[(.*?)\]\(([^)]+)\)')

def move_and_update_images(md_file):
    with open(md_file, "r", encoding="utf-8") as file:
        content = file.read()

    modified = False  # Para saber si hay cambios en el archivo

    # Buscar imágenes en el contenido del archivo
    matches = image_pattern.findall(content)
    for alt_text, image_path in matches:
        # Decodificar %20 y otros caracteres especiales en la ruta de la imagen
        decoded_image_path = urllib.parse.unquote(image_path).strip()  
        image_name = os.path.basename(decoded_image_path)  
        original_image_path = os.path.join(markdown_folder, decoded_image_path)
        new_image_path = os.path.join(image_folder, image_name)

        # Verificar si la imagen existe antes de moverla
        if os.path.exists(original_image_path):
            try:
                shutil.copy2(original_image_path, new_image_path)  # Copiar en lugar de mover
                os.remove(original_image_path)  # Eliminar el original solo si la copia fue exitosa
                print(f"📁 Movida: {original_image_path} ➝ {new_image_path}")
            except Exception as e:
                print(f"❌ ERROR al mover {original_image_path}: {e}")
        else:
            print(f"⚠️ Imagen no encontrada: {original_image_path}")

        # Construir el nuevo enlace con el formato correcto
        new_markdown_path = f"imagenes/{image_name}"
        new_markdown_link = f"![{alt_text}](<{new_markdown_path}>)"  

        # Reemplazar en el contenido
        old_markdown_link = f"![{alt_text}]({image_path})"
        content = content.replace(old_markdown_link, new_markdown_link)
        modified = True

    # Guardar los cambios en el archivo Markdown si hubo modificaciones
    if modified:
        with open(md_file, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"✅ Enlaces corregidos en: {md_file}")

# Procesar todos los archivos .md en la carpeta
for file in os.listdir(markdown_folder):
    if file.endswith(".md"):
        file_path = os.path.join(markdown_folder, file)
        move_and_update_images(file_path)

print("🎯 Todo el proceso ha sido completado correctamente.")
