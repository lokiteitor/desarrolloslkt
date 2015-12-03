#!/bin/bash
DIALOG=dialog


# crea un archivo temporal donde guardar las selecciones
tempfile=`tempfile 2>/dev/null` || tempfile=/tmp/test$$
# al finalizar el script borra el archivo temporal
trap "rm -f $tempfile" 0 1 2 5 15
#tempfile=$PWD/log
paquetesid=`cat paquetes_id`
paquetes=`cat paquetes`
user=$(whoami)


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
        echo sudo apt-get install -y ${lista[$i]}
    done
fi
