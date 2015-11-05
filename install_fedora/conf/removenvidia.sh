#!/bin/bash
dnf -y remove xorg-x11-drv-nvidia-340xx nvidia-settings nvidia-xconfig
rm /boot/initramfs-$(uname -r).img 
dracut /boot/initramfs-$(uname -r).img $(uname -r)
