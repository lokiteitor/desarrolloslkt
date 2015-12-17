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

DIALOG=dialog


# crea un archivo temporal donde guardar las selecciones
tempfile=`tempfile 2>/dev/null` || tempfile=/tmp/test$$

# al finalizar el script borra el archivo temporal
trap "rm -f $tempfile" 0 1 2 5 15
#tempfile=$PWD/log
paquetesid=`cat paquetes_id`
paquetes=`cat paquetes`
user=$(whoami)


# Revisar Arquitectura y version de distribucion

# TODO : Para mayor compatibilidad agregar los id de mas distros

iddistro=`lsb_release -i | cut -f2`
codename=`lsb_release -c | cut -f2`
release=`lsb_release -r | cut -f2`
arch=`uname -m`

# TODO : que pasa con las arquitecturas i386 , las marca igual a las i586 e i686
# Codigo cutre se puede mejorar
if [ $iddistro == "Debian" ]; then
    iddistro="debian"
    if [ $arch == "x86_64" ]; then
        arch="amd64"
    fi

elif [ $iddistro == "Ubuntu" ]; then
    iddistro="ubuntu"
    if [ $arch == "x86_64" ]; then
        arch="amd64"
    fi
fi

# Funcion para instalar la version indicada de MariaDB

install_MariaDB (){
    tempfileaux=`tempfileaux 2>/dev/null` || tempfileaux=/tmp/testaux$$

    trap "rm -f $tempfileaux" 0 1 2 5 15


    $DIALOG --output-separator "," --title "MariaDB" --radiolist  "Seleccione la version de MariaDB" 10 40 7 \
    1 "MariaDB 10.1" on 2 "MariaDB 10.0" off 3 "MariaDB 5.5" off 2> "$tempfileaux";

    idversion=`cut -b 2- $tempfileaux | cut -d "," -f 1`

    if [ $idversion == "1" ]; then
        # Instalar la version 10.1
        repo='deb '$arch' http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.1/'$iddistro" "$codename" main"
        
    fi
    if [ $idversion = "2" ]; then
        repo='deb '$arch' http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.0/'$iddistro" "$codename" main"            
    fi
    if [ $idversion = "3" ]; then
        repo='deb '$arch' http://nyc2.mirrors.digitalocean.com/mariadb/repo/5.5/'$iddistro" "$codename" main"
    fi
    echo $repo
    if [ "$user" == "root" ]; then
        apt-get install software-properties-common
        apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
        add-apt-repository $repo

        sleep 2

    else
        echo "Necesitas estar logueado como root"

        sudo apt-get install software-properties-common
        sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
        sudo add-apt-repository $repo
        sleep 2
    fi

}

$DIALOG --title "install server" --infobox  "A continuacion podra elegir los paquetes que \
                                requiere su servidor" 10 30; sleep 2

$DIALOG --output-separator "," --title "install server" --checklist  "Seleccione los paquetes que desea instalar" 10 40 7 \
 $paquetesid 2> $tempfile;

resp=`cat $tempfile`

# la longitud menos uno por la , inicial
len=`cat $tempfile | sed "s/,/\n/g" | grep -e [0-9]* -c`
# ahora que sabemos el numero id del paquete a instalar tenemos que buscarlo en la lista

echo "Paquetes que instalare:"

for (( i = 1; i < len; i++ )); do
    idpkg=`cut -b 2- $tempfile | cut -d "," -f $i`
    # Revisar si la opcion es la base de datos MariaDB
    if [ $idpkg == "5" ]; then
       install_MariaDB
    fi

    pkg=`cat paquetes | grep -e "^"$idpkg | cut -b 3-`
    lista[$i-1]=$pkg

    echo "      $pkg"
done

sleep 2
$DIALOG --title "Confirmacion" --yesno "Deseas continuar?" 6 30

case $? in

  1)
    exit;;
  255)
    exit;;
esac

# Procede a instalar los paquetes
if [ "$user" == "root" ]; then
    for (( i = 0; i < ${#lista[@]}; i++ )); do
        apt-get -y install ${lista[$i]}
    done
else
    echo "Necesitas estar logueado como root"
    for (( i = 0; i < ${#lista[@]}; i++ )); do
        sudo apt-get install -y ${lista[$i]}
    done
fi


# TODO: instrucciones especiales para por ejemplo
# Guest additions