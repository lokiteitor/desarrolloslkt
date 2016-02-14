#!/bin/bash
pacman -S xf86-input-synaptics --noconfirm

pacman -S alsa-utils ttf-dejavu xdg-user-dirs --noconfirm

pacman -S ffmpeg gst-libav gst-plugins-bad gst-plugins-base gst-plugins-good  --noconfirm
pacman -S gst-plugins-ugly gstreamer0.10-good-plugins --noconfirm

pacman -S gst-vaapi gstreamer0.10-bad-plugins gstreamer0.10-base-plugins gstreamer0.10-ffmpeg --noconfirm

pacman -S gstreamer0.10-ugly-plugins --noconfirm

pacman -S jdk7-openjdk --noconfirm

pacman -S openssh --noconfirm

pacman -S unrar htop evince gvfs leafpad brasero --noconfirm

pacman -S unzip rsync file-roller dosfstools --noconfirm

pacman -S cups ghostscript gsfonts gutenprint --noconfirm

pacman -S pulseaudio pavucontrol pulseaudio-alsa --noconfirm

pacman -S chromium --noconfirm

pacman -S git terminator moc vim --noconfirm

pacman -S docker virtualbox eclipse-java
