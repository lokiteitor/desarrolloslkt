#!/bin/bash
jails=/home/users/jails


useradd -Nm $1 -s /bin/bash

#agregar directorio base si no existe

if [ -d /home/users/jails ]; then
	echo " El directorio base ya existe"
else
	mkdir -p /home/users/jails
fi

chown root:root $jails/$1
jk_init -v /home/users/jails/$1 basicshell
chmod 755 /home/users/jails/$1/bin

jk_init -v /home/users/jails/$1 netutils
jk_init -v /home/users/jails/$1 ssh
jk_init -v /home/users/jails/$1 jk_lsh
jk_init -v /home/users/jails/$1 editors
jk_init -v /home/users/jails/$1 scp
jk_init -v /home/users/jails/$1 sftp
jk_init -v /home/users/jails/$1 extendedshell
jk_init -v /home/users/jails/$1 git
jk_init -v /home/users/jails/$1 nodejs
jk_init -v /home/users/jails/$1 bower
jk_init -v /home/users/jails/$1 composer

mkdir /home/users/jails/$1/opt

jk_cp -v -f /home/users/jails/$1 /bin/bash
jk_update -j /home/users/jails/$1 -d


sed 's/\/usr\/sbin\/jk_lsh/\/bin\/bash/g' $jails/$1/etc/passwd > $jails/$1/etc/passwd.new
mv $jails/$1/etc/passwd.new $jails/$1/etc/passwd

jk_jailuser -m -j /home/users/jails/$1 $1

# Activar public_html y espacio en apache
if [ -f /etc/apache2/sites-available/$1 ]; then
	echo "El sitio ya esta disponible"
else
	mkdir /home/users/jails/$1/home/$1/public_html
#	sed 's/#ServerName\ www.example.com/ServerName\ www'
	cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/$1
	
	echo " Activar manualmente"
fi

# generar llaves privadas
if [ -d /home/users/jails/$1/home/$1/.ssh ]; then
	echo "El directorio ya exite"
else
	mkdir /home/users/jails/$1/home/$1/.ssh
	touch /home/users/jails/$1/home/$1/.ssh/authorized_keys
fi

cat /etc/passwd
echo "\n\n"
cat /home/users/jails/$1/etc/passwd
