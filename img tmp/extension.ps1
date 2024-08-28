# Chemin du dossier contenant les fichiers
$dossier = "C:\Users\julie\OneDrive\Images\windows a la une\img tmp"

# Obtenir la liste des fichiers sans extension dans le dossier
$fichiersSansExtension = Get-ChildItem -Path $dossier | Where-Object { $_.Extension -eq '' }

# Ajouter l'extension ".png" aux fichiers sans extension
foreach ($fichier in $fichiersSansExtension) {
    $nouveauChemin = $fichier.FullName + ".png"
    Rename-Item -Path $fichier.FullName -NewName $nouveauChemin
}

Write-Host "Extension .png ajoutée aux fichiers sans extension dans le dossier $dossier."
