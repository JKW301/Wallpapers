import os
from PIL import Image
import shutil

SOURCE_FOLDER = os.path.expandvars(r"%localappdata%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets")
DEST_FOLDER = os.path.join("..", "all_images")
CURRENT_DIR = os.getcwd()

# Créer le dossier destination s'il n'existe pas
if not os.path.exists(DEST_FOLDER):
    os.makedirs(DEST_FOLDER)

# Copier et filtrer les images
for filename in os.listdir(SOURCE_FOLDER):
    source_path = os.path.join(SOURCE_FOLDER, filename)
    if os.path.isfile(source_path):
        try:
            with Image.open(source_path) as img:
                width, height = img.size
                # Vérifier l'orientation paysage et la résolution minimale
                if width >= 1920 and height >= 1080:
                    dest_path = os.path.join(DEST_FOLDER, f"{os.path.basename(filename)}.png")
                    img.save(dest_path, format="PNG")
                    print(f"Image déplacée : {dest_path}")
        except Exception as e:
            print(f"Erreur avec le fichier {filename}: {e}")
