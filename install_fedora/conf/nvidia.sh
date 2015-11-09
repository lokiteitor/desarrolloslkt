#!/bin/bash
#dnf -y install akmod-nvidia-340xx xorg-x11-drv-nvidia-340xx acpid kernel-devel
#rm /boot/initramfs-$(uname -r).img
#dracut /boot/initramfs-$(uname -r).img $(uname -r)

#grub2-mkconfig -o /boot/grub2/grub.cfg

plymouth-set-default-theme solar
/usr/libexec/plymouth/plymouth-update-initrd

