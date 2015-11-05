#!/bin/bash

cd /etc/yum.repos.d/
wget http://download.opensuse.org/repositories/home:Horst3180/Fedora_22/home:Horst3180.repo
dnf -y install ceti-2-theme
