#!/bin/bash
DIALOG=dialog

# crea un archivo temporal donde guardar las selecciones
tempfile=`tempfile 2>/dev/null` || tempfile=/tmp/test$$
#archivo donde se almacena la informacion
info=info/info_$$

# al finalizar el script borra el archivo temporal
trap "rm -f $tempfile" 0 1 2 5 15

getUserDataFromTTY (){
    
  echo "" > $tempfile

  $DIALOG --title "Recuperacion de datos del cliente" --clear \
          --inputbox $2 16 51 2> $tempfile

  retval=$?

  case $retval in
    0)
      dato=`cat $tempfile`
      echo $1'='$dato >> $info ;;
    1)
      echo "Cancel pressed.";;
    255)
      if test -s $tempfile ; then
        cat $tempfile
      else
        echo "ESC pressed."
      fi
      ;;
  esac
}

getUserDataFromTTY "nombre" "Ingrese_el_nombre_del_usuario"
getUserDataFromTTY "usuario" "Ingrese_el_nombre_de_usuario"
# mas adelante generamos la contrasena
getUserDataFromTTY "correo" "Ingrese_el_correo_del_usuario"
getUserDataFromTTY "dominio" "Ingrese_el_dominio"

#imprimo los datos capturados
echo ""
while read line
do 
   echo -e $line
done < $info



