#!/bin/bash
# Busca archivos requirements.txt e instala los requisitos de cada uno
find  /mnt/extra-addons -type f -name 'requirements.txt' -exec pip install -r '$0' {} \;