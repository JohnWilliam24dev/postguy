#!/bin/bash
set -e  # Faz o script falhar se algum comando falhar

echo "Instalando PostGuy..."

pip install --user --upgrade git+https://github.com/JohnWilliam24dev/postguy.git

# Adiciona ~/.local/bin ao PATH se necessário
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
    source ~/.bashrc
fi

echo "Instalação concluída! Tente rodar 'postguy --help'"