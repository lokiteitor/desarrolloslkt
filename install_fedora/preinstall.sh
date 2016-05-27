#!/bin/bash

# configuraciones previas

dnf -y install curl wget

dnf -y install --nogpgcheck http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
wget -P /etc/yum.repos.d/ https://raw.github.com/kuboosoft/postinstallerf/master/postinstallerf.repo
dnf -y update kernel* selinux-policy*


# configuracion de repositorios
cd /etc/yum.repos.d/

wget http://download.virtualbox.org/virtualbox/rpm/fedora/virtualbox.repo

# Instalacion de paquetes externos
dnf -y install /run/media/Archivos/Install/nautilus-dropbox-2015.02.12-1.fedora.x86_64.rpm
dnf -y install /run/media/Archivos/Install/google-chrome-stable_current_x86_64.rpm
dnf -y install /run/media/Archivos/Install/variety-0.5.3-1.fc22.noarch.rpm



#echo "UUID=19283B031A3A74C5 /run/media/Archivos ntfs-3g auto,rw,users,uid=1000,gid=1000 0 0 " >> /etc/fstab


reboot

