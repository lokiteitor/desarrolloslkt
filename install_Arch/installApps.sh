#!/bin/bash

# comprobar en varias opciones donde puede estar disponible los
# paquetes

cd $HOME/Descargas

wget repo.desarrolloslkt.tk/extern/Sublime.tar.bz2
wget repo.desarrolloslkt.tk/extern/firefox_dev.tar.bz2

tar jvxf Sublime.tar.bz2
tar jvxf firefox_dev.tar.bz2

# descargar los iconos

wget repo.desarrolloslkt.tk/accessapp/Firefox.desktop
wget repo.desarrolloslkt.tk/accessapp/Sublime\ Text.desktop

mv firefox/* $HOME/.firefox_dev/


# ejecutar lo siguiente como root

mv Sublime\ Text\ 2/ /usr/bin/sublime_text
mv Sublime\ Text.desktop /usr/bin/share/applications/
mv Firefox.desktop  /usr/bin/share/applications/

