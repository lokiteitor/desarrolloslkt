#!/bin/bash


# configuraciones previas

exec /run/media/Archivos/Install/Oxygen/install.sh

dnf -y install curl wget

dnf -y install --nogpgcheck http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm


# configuracion de repositorios
cd /etc/yum.repos.d/

wget http://download.virtualbox.org/virtualbox/rpm/fedora/virtualbox.repo

usermod -a -G vboxusers lokiteitor


# paquetes basicos

dnf -y install kernel-headers
dnf -y install kernel-devel
dnf -y groupinstall "Development Tools"
dnf -y groupinstall "Development Libraries"
dnf -y install gstreamer-plugins-bad gstreamer-plugins-bad-free-extras 
dnf -y install gstreamer-plugins-bad-nonfree gstreamer-plugins-ugly gstreamer-ffmpeg
dnf -y install gstreamer1-libav gstreamer1-plugins-bad-free-extras 
dnf -y install gstreamer1-plugins-bad-freeworld gstreamer1-plugins-base-tools 
dnf -y install gstreamer1-plugins-good-extras gstreamer1-plugins-ugly gstreamer1-plugins-bad-free
dnf -y install gstreamer1-plugins-good gstreamer1-plugins-base gstreamer1

dnf -y install ffmpeg
dnf -y install unrar p7zip p7zip-plugins
dnf -y install java
dnf -y install icedtea-web

dnf -y install evince
dnf -y install blueman
dnf -y install gnome-tweak-tool


# Paquetes basicos
dnf -y install terminator
dnf -y install vim
dnf -y install git


# paquetes multimedia

dnf -y install gimp
dnf -y install gmusicbrowser moc


# Desinstalacion de paquetes no utiles

dnf -y remove firefox*
dnf -y remove evolution

# paquetes de virtualizacion
dnf -y install binutils gcc make patch libgomp glibc-headers glibc-devel kernel-headers kernel-devel dkms
dnf -y install VirtualBox-4.3

service vboxdrv setup

dnf -y install docker docker-vim
groupadd docker
usermod -aG docker lokiteitor

# Mensajes post-instalacion

echo "VirtualBox\n"
echo "configura virtualbox extencion pack manualmente"

# Configuracion Grub
mv grub /etc/default/grub
cp /boot/grub2/grub.cfg /boot/grub2/grub.cfg.bak

grub2-mkfont --output=/boot/grub2/fonts/LiberationMono-Regular.pf2 --size=24 /usr/share/fonts/liberation/LiberationMono-Regular.ttf
grub2-mkconfig -o /boot/grub2/grub.cfg

dnf -y install plymouth-theme-solar
plymouth-set-default-theme solar
/usr/libexec/plymouth/plymouth-update-initrd



# Instalacion del controlador grafico 
dnf -y kmod-nvidia-340xx xorg-x11-drv-nvidia-340xx acpid
mv /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r)-nouveau.img
dracut /boot/initramfs-$(uname -r).img $(uname -r)


# Instalacion de paquetes externos
dnf -y install /run/media/Archivos/Install/nautilus-dropbox-2015.02.12-1.fedora.x86_64.rpm
dnf -y install /run/media/Archivos/Install/google-chrome-stable_current_x86_64.rpm
dnf -y install /run/media/Archivos/Install/variety-0.5.3-1.fc22.noarch.rpm


# Mover los .desktop de Sublime y Firefox

exec gitconfig.sh












