#!/bin/bash

#activar el NAT
echo "1" > /proc/sys/net/ipv4/ip_forward
iptables -A FORWARD -j ACCEPT
iptables -t nat -A POSTROUTING -s 10.0.0.0/8 -o wlan0 -j MASQUERADE
#configurar la interfaz de red
ifconfig eth0 10.0.0.1 netmask 255.0.0.0 broadcast 10.255.255.255 



