#!/bin/bash
#Copyright 2015 David Delgado Hernandez

    # This file is part of install_server.

    # install_server is free software: you can redistribute it and/or modify
    # it under the terms of the GNU Lesser General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # install_server is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU Lesser General Public License for more details.

    # You should have received a copy of the GNU Lesser General Public License
    # along with install_server.  If not, see <http://www.gnu.org/licenses/>.
# revisar si las dependencias estan instaladas

tempfile=`tempfile 2>/dev/null` || tempfile=/tmp/test$$
trap "rm -f $tempfile" 0 1 2 5 15


if [[ `dpkg -l | cut -d " " -f3 | grep dialog` ]]; then
    echo "ok"
else
    if [ "$user" == "root" ]; then
        apt-get -y install dialog
    else
        echo "Necesitas estar logueado como root"
        sudo apt-get install -y dialog
    fi
fi

DIALOG=dialog

$DIALOG --clear --title "Que accion desea realizar" \
        --menu "Elige la opcion" 20 51 4 \
        "install"  "Instalar Paquetes" \
        "dockercfg" "Configurar docker" \
        "openssh" "Configurar Openssh"\
        "apache" "Configurar Apache" 2> $tempfile

retval=$?

choice=`cat $tempfile`

case $retval in
  1)
    echo "Cancel pressed.";;
  255)
    echo "ESC pressed.";;
esac

if [[ $choice == "install" ]]; then
    ./install_pkg.sh
elif [[ $choice == "dockercfg" ]]; then

    if [[ `service docker status | grep start` ]]; then
        ./install_docker.sh
    else

        if [ "$user" == "root" ]; then
            service docker start
        else
            echo "Necesitas estar logueado como root"
            sudo service docker start
        fi
    fi
    
elif [[ $choice == "openssh" ]]; then
    echo "openssh"
elif [[ $choice == "apache" ]]; then
    echo "apache"

fi