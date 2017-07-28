#!/bin/bash

# configuramos el lenguaje
echo "es_MX.UTF-8 UTF-8" >> /etc/locale.gen

locale-gen

echo "LANG=es_MX.UTF-8 > /etc/locale.conf"

export LANG=es_MX.UTF-8

echo "KEYMAP=es" > /etc/vconsole.conf

ln -s /usr/share/zoneinfo/America/Mexico_City /etc/localtime


pacman -Syu --noconfirm
pacman -S openssh vim python python2 --noconfirm
pacman -S python-setuptools python2-setuptools python-pip python2-pip --noconfirm
pacman -S jdk8-openjdk --noconfirm
pacman -S htop unrar unzip rsync --noconfirm
pacman -S moc git

pacman -S ffmpeg gst-libav gst-plugins-bad gst-plugins-base gst-plugins-good  --noconfirm
pacman -S gst-plugins-ugly --noconfirm


git config --global user.name "lokiteitor"
git config --global user.email lokiteitor513@gmail.com
git config --global core.editor vim


systemctl enable sshd 
systemctl start enable sshd

pacman -S docker docker-composer --noconfirm
pacman -S bind bind-tools --noconfirm
pacman -S transmission-cli --noconfirm
#pacman -S docker docker-compose --noconfirm
#pacman -S fail2ban ffmpeg youtube-dl transmission-cli screen --noconfirm

docker pull httpd:latest
docker pull mariadb:latest
docker pull node:latest
docker pull php:apache
docker pull jenkins:latest
docker pull owncloud:latest
