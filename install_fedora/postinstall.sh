#!/bin/bash

cd $HOME

mkdir .firefoxdev
cp $ARCHIVOS/Install/firefox-* .firefoxdev/
tar jvxf .firefoxdev/firefox-*
mv firefox/* .firefoxdev/
rmdir firefox


mkdir $HOME/.tmplkt
cp  $ARCHIVOS/Install/Sublime\ Text\ 2.0.2\ x64.tar.bz2 $HOME/.tmplkt
tar jvxf .tmplkt/Sublime\ Text\ 2.0.2\ x64.tar.bz2
mv Sublime\ Text\ 2 Sublime_Text
sudo mv Sublime_Text /usr/bin

sudo cp $ARCHIVOS/Install/Firefox-Developer.desktop /usr/share/applications

sudo cp $ARCHIVOS/Install/Sublime\ Text.desktop /usr/share/applications

rm -rf .tmplkt



