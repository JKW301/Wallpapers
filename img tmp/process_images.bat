@echo off

:: Étape 1 : Nettoyage des anciens PNG
echo Suppression des fichiers PNG existants...
for %%f in (*.png) do del "%%f"

:: Étape 2 : Exécution du script Python pour filtrer et déplacer les images
python filter_landscape.py

pause
