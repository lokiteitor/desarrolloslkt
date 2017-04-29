#!/bin/bash
#configuracion del cliente freebsd
echo 'ifconfig_fxp0"="inet 10.0.0.2 netmask=255.0.0.0' >> /etc/rc.conf
echo 'defaultrouter="10.0.0.1"' >> /etc/rc.conf
echo 'nameserver 192.168.1.254' >> /etc/resolv.conf
