#!/bin/bash
# Busca archivos requirements.txt e instala los requisitos de cada uno
find /mnt/extra-addons -type f -name 'requirements.txt' -exec sh -c 'echo "Instalando... $1"; pip install -r $1' _ {} \;
