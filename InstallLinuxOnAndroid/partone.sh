#!/bin/bash

#TODO : debe de pedirme el directorio donde guardar la imagen .img
cd $ARCHIVOS

#TODO : Revisar que el paquete pv este instalado en caso contrario instarlo
#       Personalizar el nombre del archivo
#       No se limita correctamente el tamaño de la imagen        
dd if=/dev/zero  | pv | dd of=Linux.img bs=1024 count=3048M


mount archlinux.img archlinux/
mount -o bind /dev/ /sdcard/archlinux/dev/
mount -t proc proc /sdcard/archlinux/proc/
mount -t sysfs sysfs /sdcard/archlinux/sys/
mount -t devpts devpts /sdcard/archlinux/dev/pts/
echo "nameserver 8.8.8.8" > /sdcard/archlinux/etc/resolv.conf