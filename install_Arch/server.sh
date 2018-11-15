#!/bin/bash
git config --global user.name "lokiteitor"
git config --global user.email lokiteitor513@gmail.com
git config --global core.editor vim
docker pull httpd:latest
docker pull mariadb:latest
docker pull node:latest
docker pull php:apache
docker pull jenkins:latest
docker pull owncloud:latest
