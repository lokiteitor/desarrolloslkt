#!/bin/bash
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
