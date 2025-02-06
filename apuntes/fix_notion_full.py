import os
import re
import shutil

# Configuración
markdown_folder = "C:\\Users\\jpueyo\\Documents\\Github\\gitbook\\writeup-ctfs\\DockerLabs"  # Carpeta donde están los .md
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
        # Obtener el nombre del archivo de la imagen
        image_name = os.path.basename(image_path)
        new_image_path = os.path.join(image_folder, image_name)  # Ruta destino de la imagen

        # Comprobar si la imagen existe en la ubicación original
        original_image_path = os.path.join(markdown_folder, image_path)
        if os.path.exists(original_image_path):
            # Mover la imagen a la carpeta 'imagenes'
            shutil.move(original_image_path, new_image_path)
            print(f"📁 Movida: {original_image_path} ➝ {new_image_path}")

        # Actualizar el enlace en Markdown con el formato correcto (con espacios)
        new_markdown_path = f"imagenes/{image_name}"
        new_markdown_path = f"(<{new_markdown_path}>)"  # Asegura que los espacios se mantengan
        content = content.replace(f"({image_path})", new_markdown_path)
        modified = True

    # Guardar los cambios en el archivo Markdown si hubo modificaciones
    if modified:
        with open(md_file, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"✅ Enlaces corregidos en: {md_file}")

# Recorrer todos los archivos .md en la carpeta y aplicar los cambios
for root, _, files in os.walk(markdown_folder):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            move_and_update_images(file_path)

print("🎯 Todo el proceso ha sido completado.")
