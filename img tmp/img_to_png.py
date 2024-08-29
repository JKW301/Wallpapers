import os
from PIL import Image

# Chemin du répertoire parent
directory = '../'

# Parcourir tous les fichiers du répertoire parent
for filename in os.listdir(directory):
    if filename.endswith('.img'):
        # Chemin complet du fichier .img
        img_path = os.path.join(directory, filename)
        
        # Ouvrir le fichier .img
        with Image.open(img_path) as img:
            # Chemin complet pour le fichier .png
            png_path = os.path.splitext(img_path)[0] + '.png'
            
            # Sauvegarder l'image en .png
            img.save(png_path)
            print(f'Converti : {filename} en {os.path.basename(png_path)}')
