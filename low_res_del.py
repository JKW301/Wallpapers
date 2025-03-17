import os
from collections import defaultdict
from PIL import Image

# Extensions d'images courantes
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}

def delete_low_resolution_images(directory, min_width=1920, min_height=1080):
    """
    Supprime les images ayant une résolution inférieure à 1920x1080 et affiche les statistiques des résolutions.

    :param directory: Répertoire contenant les images.
    :param min_width: Largeur minimale requise.
    :param min_height: Hauteur minimale requise.
    """
    if not os.path.isdir(directory):
        print(f"Le répertoire {directory} n'existe pas.")
        return

    resolution_count = defaultdict(int)
    deleted_count = 0

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Vérifier si le fichier a une extension d'image valide
        if not any(filename.lower().endswith(ext) for ext in IMAGE_EXTENSIONS):
            continue

        try:
            with Image.open(filepath) as img:
                width, height = img.size
                resolution = f"{width}x{height}"
                resolution_count[resolution] += 1

                # Supprimer si résolution inférieure à 1920x1080
                if width < min_width or height < min_height:
                    os.remove(filepath)
                    deleted_count += 1
                    resolution_count[resolution] -= 1  # Retirer du comptage

        except Exception as e:
            print(f"Impossible de traiter {filename}: {e}")

    # Affichage du résumé des résolutions
    print("\nRésumé des résolutions restantes :")
    for res, count in sorted(resolution_count.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            print(f"{res} : {count} fichiers")

    print(f"\nTotal des fichiers supprimés : {deleted_count}")

if __name__ == "__main__":
    directory = input("Entrez le chemin du répertoire contenant les images : ")
    delete_low_resolution_images(directory)

