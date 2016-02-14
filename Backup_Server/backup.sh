#!/bin/bash

isconn=`sudo ping -W 3 -c 1 lokiteitor | grep -c "from lokiteitor"`
fecha=$(date +%y%m%d%H%M)
log=$HOME/Backup/fail.log

# Realizar el Backup
sudo rsync -avvbh --backup-dir=/home/lokiteitor/Backup/backup_$fecha --files-from=/home/lokiteitor/bin/lista_Backup.cfg / /home/lokiteitor/Backup/latest/ 2>> $log

sudo tar cfvj  $HOME/Backup/tarball/backup_$fecha.tar.bz2 $HOME/Backup/backup_$fecha 2>> $log

if [[ $isconn == "1" ]]; then
    # si el host remoto esta conectado enviarle el tarball del ultimo backup
    echo "El host es conectado procedo a enviarle el tarball"
fi

if test -e $HOME/Backup/tarball/latest.tar.bz2; then
    # para comprimir el latest backup debo primero eliminar el anterior
    echo "Procedo a eliminar el backup anterior"
	sudo rm $HOME/Backup/tarball/latest.tar.bz2 
fi

echo "Comprimiendo Backup principal"
sudo tar cfvj  $HOME/Backup/tarball/backup_latest.tar.bz2 $HOME/Backup/latest 2>> $log
