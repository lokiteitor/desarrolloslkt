#!/bin/bash

cd $HOME

echo "set number" >> .vimrc

# Mover tema de Install a carpeta temas

mkdir .theme

cp $ARCHIVOS/Install/167652-AfterDark.tar.gz $HOME/.theme
tar xzvf $HOME/.theme/167652-AfterDark.tar.gz
