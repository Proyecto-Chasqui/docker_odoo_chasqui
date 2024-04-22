#!/bin/bash
ADDONS_DIR="./custom_addons"

find "$ADDONS_DIR" -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} +

# Leer cada nea de folders.txt y copiar las carpetas al directorio temporal
while IFS= read -r folder
do
  echo "Copiando carpeta: $folder"
  cp -R "./partials_addons/$folder" "$ADDONS_DIR/"
done < ./partials_addons/selected_folders.txt