#!/bin/bash

dnf -y update kernel* selinux-policy*

echo "UUID=19283B031A3A74C5 /run/media/Archivos ntfs-3g auto,rw,users,uid=1000,gid=1000 0 0 " >> /etc/fstab


reboot

