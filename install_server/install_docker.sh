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
paquetesid=`cat dockerpkg`
paquete="dockerpkg"
user=$(whoami)


$DIALOG --output-separator "," --title "Instalar Contenedores" --checklist \
  "Selecciona los Contenedores que quieres instalar" 50 40 7 \
 $paquetesid 2> $tempfile;

resp=`cat $tempfile`

len=`cat $tempfile | sed "s/,/\n/g" | grep -e [0-9]* -c`

# ahora que sabemos el numero id del paquete a instalar tenemos que buscarlo en la lista
echo "Paquetes que instalare:"

for (( i = 1; i < len; i++ )); do

    idpkg=`cut -b 2- $tempfile | cut -d "," -f $i`
    pkg=`cat $paquete| grep -e "^"$idpkg | cut -d " " -f2`
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

if [ "$user" == "root" ]; then
    for (( i = 0; i < ${#lista[@]}; i++ )); do
        docker pull ${lista[$i]}
    done
else
    echo "Necesitas estar logueado como root"
    for (( i = 0; i < ${#lista[@]}; i++ )); do
        sudo docker pull ${lista[$i]}
    done
fi
