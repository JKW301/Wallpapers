import os

# Extensions des fichiers image à supprimer
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

# Parcourir tous les fichiers du répertoire courant
for filename in os.listdir('.'):
    # Vérifier si le fichier a une extension d'image
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        os.remove(filename)
        print(f'Supprimé : {filename}')
