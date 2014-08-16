#!/bin/bash

pacman -S apache php php-apache mysql

systemctl start mysqld 

mysql_secure_installation

# configurar apache

echo "IncludeOptional conf/sites-enabled/*.conf" >> /etc/httpd/conf/httpd.conf
echo "IncludeOptional conf/mods-enabled/*.conf" >> /etc/httpd/conf/httpd.conf


mkdir /etc/httpd/conf/sites-available
mkdir /etc/httpd/conf/sites-enabled
mkdir /etc/httpd/conf/mods-enabled


chmod +x a2ensite a2dissite
cp a2ensite a2dissite /usr/local/bin/



touch /etc/httpd/conf/mods-enabled/php.conf


echo "LoadModule mpm_prefork_module modules/mod_mpm_prefork.so" >> /etc/httpd/conf/mods-enabled/php.conf
echo "LoadModule php5_module modules/libphp5.so" >> /etc/httpd/conf/mods-enabled/php.conf

echo "Include conf/extra/php5_module.conf"  >> /etc/httpd/conf/mods-enabled/php.conf

systemctl start httpd
systemctl enable httpd

#encontrar la forma de hacer esto automaticamente
echo "comenta la siguiente linea en /etc/httpd/conf/httpd.conf"
echo "#LoadModule mpm_event_module modules/mod_mpm_event.so"

#activar modulos de php