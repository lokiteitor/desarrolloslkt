#/bin/bash


#realizar el chroot manualmente

pacstrap /mnt base base-devel

genfstab -U -p /mnt >> /mnt/etc/fstab

cp inchroot.sh /mnt/root

#arch-chroot /mnt /mnt/root/inchroot.sh
