#!/bin/bash

# De forma manual se tiene que ejecutar raspi-config y configurar una ip 
# estatica 

# Dar de alta usuario lokiteitor manualmente

# Modificar sudoers

# fijar los alias

paquetes=`cat pkg.cfg`
user=$(whoami)

# versiones : por si llegara a necesitarlo
iddistro=`lsb_release -i | cut -f2`
codename=`lsb_release -c | cut -f2`
release=`lsb_release -r | cut -f2`
arch=`uname -m`

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




# Procede a instalar los paquetes
if [ "$user" == "root" ]; then
    while read line
    do 
       pkg=`echo -e "$line"`
       apt-get install $pkg
    done < pkg.cfg
done

else
    echo "Necesitas estar logueado como root"
    done
fi