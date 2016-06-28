# ejecutar como root por defecto al instalar nodejs

# common
dnf -y install curl

# paquetes de lenguajes de programacion
dnf -y install ruby
dnf -y install php
curl --silent --location https://rpm.nodesource.com/setup_6.x | bash -
dnf -y install nodejs

curl -sS https://getcomposer.org/installer | php
mv composer.phar /usr/bin/composer

# paquete php 
dnf -y install php-mcrypt
dnf -y install php-mbstring
dnf -y install php-pecl-zip php-pdo