#!/bin/bash

echo "Se instalara la version 10.1 de MariaDB"

sleep 3


if [[ $(id -u) == "0" ]]; then

    echo "agregando repositorios"
    sleep 2
    apt-get install software-properties-common
    apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
    add-apt-repository 'deb http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.0/ubuntu trusty main'
    apt-get update

    echo "instalando MariaDB"
    apt-get install mariadb-server

else
    echo "Necesita ser superusuario para ejecutar esta accion"

fi


