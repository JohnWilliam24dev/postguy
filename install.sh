#!/bin/bash
set -e  # Faz o script falhar se algum comando falhar

echo "Instalando PostGuy..."
pip install --upgrade git+https://github.com/JohnWilliam24dev/postguy.git

echo "Instalação concluída!"
