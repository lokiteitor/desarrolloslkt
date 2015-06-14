#/bin/bash


# configuramos el lenguaje
echo "es_MX.UTF-8 UTF-8" >> /etc/locale.gen

locale-gen

echo "LANG=es_MX.UTF-8 > /etc/locale.conf"

export LANG=es_MX.UTF-8

ln -s /usr/share/zoneinfo/America/Mexico_City /etc/localtime

hwclock --systohc --utc

echo "lokiteitor" > /etc/hostname


#mkdir /root/base
#mount /dev/sdb1 /root/base

pacman -S iw wpa_supplicant dialog wpa_actiond --noconfirm

pacman -S grub os-prober --noconfirm

grub-install --target=i386-pc --recheck /dev/sda

grub-mkconfig -o /boot/grub/grub.cfg

useradd -m -G users -s /bin/bash lokiteitor

pacman -S xorg-server xorg-xinit --noconfirm

pacman -S xf86-video-vesa xf86-video-intel mesa mesa-libgl --noconfirm

cp /etc/X11/xinit/xinitrc /home/lokiteitor/.xinitrc

sed -i "51,55d" /home/lokiteitor/.xinitrc

pacman -S xfce4 xfce4-goodies --noconfirm

pacman -Rsn xfburn mousepad xfburn ristretto --noconfirm

echo "exec startxfce4" >> /home/lokiteitor/.xinitrc

pacman -S alsa-utils ttf-dejavu xdg-user-dirs --noconfirm

pacman -S ffmpeg gst-libav gst-plugins-bad gst-plugins-base gst-plugins-good  --noconfirm
pacman -S gst-plugins-ugly gstreamer0.10-good-plugins --noconfirm

pacman -S gst-vaapi gstreamer0.10-bad-plugins gstreamer0.10-base-plugins gstreamer0.10-ffmpeg --noconfirm

pacman -S gstreamer0.10-ugly-plugins --noconfirm

pacman -S jdk7-openjdk --noconfirm

pacman -S openssh --noconfirm

systemctl enable sshd 
systemctl start enable sshd

pacman -S unrar htop evince gvfs leafpad brasero --noconfirm

pacman -S unzip rsync file-roller dosfstools --noconfirm

pacman -S cups ghostscript gsfonts gutenprint --noconfirm


pacman -S pulseaudio pavucontrol pulseaudio-alsa --noconfirm

pacman -S chromium --noconfirm

pacman -S git meld terminator moc --noconfirm

pacman -S libreoffice --noconfirm

