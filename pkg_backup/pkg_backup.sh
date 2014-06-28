#/bin/bash

# este script permite realizar un backup de los paquetes de instalacion de 
# pacman en caso de querer hacer downgrade de un paquete conflictivo se puede
# recurrir a este backup el cual hace una copia de manera local y en caso de 
# encontrarse el dispositivo de backup externo realiza una actualizacion del 
# contenido que este aloja recurriendo a rsync para reducir transferencia de
# datos, tiempo y espacio.

# dependencias:
# rsync

# issue 28-06-2014-a1:
# existe un error en los nombres de archivo que contengan : en la fase 
# de tranferencia a dispositivo extraible

rsync  -avv /var/cache/pacman/pkg/ $HOME/Documentos/pkgbackup/pkg/
rsync -vv /etc/pacman.conf $HOME/Documentos/pkgbackup/pkg
LISTA=`ls  $HOME/Documentos/pkgbackup/pkg/`


for i in $LISTA; do
    
    # separamos la cadena en paquete | version
    INDEX=`expr index $i "."`
    SUB=${i:0:$INDEX}

    # retiramos el numero correspondiente a la version mayor de cada paquete

    VERSIONINDEX=`expr index $SUB [0..9]`

    PAQUETE=${SUB:0:$VERSIONINDEX}

    # buscamos paquetes que coincidan con el nombre de la cadena

    COINCIDEN=`ls $HOME/Documentos/pkgbackup/pkg/${PAQUETE}* | grep -c $PAQUETE`
    QUIEN=`ls -1 -t $HOME/Documentos/pkgbackup/pkg/${PAQUETE}*`
    

    if [[ COINCIDEN -gt 1 ]]; then

        # ya encontramos el paquete ahora debemos comprobar cual es menor que
        # el otro y eliminarlo
        BASURA=`ls -1 -t $HOME/Documentos/pkgbackup/pkg/${PAQUETE}* | tail -n 1`

        echo "Eliminando $BASURA"
        rm $BASURA 2> errores.log
    fi
done
# ahora debemos de comprobar que el dispositivo donde se guadara el backup
# este montado

if [[ -w /run/media/lokiteitor/backup/pkgbackup ]]; then
    echo "el dispositivo de backup esta montado"
    echo "actualizando backup en dispositivo"
    rsync  -avv --delete $HOME/Documentos/pkgbackup/pkg/ /run/media/lokiteitor/backup/pkgbackup/

    echo "finalizado"


    


    # echo "desea actualizar el backup de paquetes"
    # echo '[S/n]'

    # read $RESPUESTA
    # echo $RESPUESTA

    # if [[ "$RESPUESTA" = "s" ]]; then 
    #     echo "respondio si"
    # else
    #     echo "respondio no"
    # fi


fi