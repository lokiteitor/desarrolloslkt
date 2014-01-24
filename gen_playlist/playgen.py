#!/usr/bin/env python2.7

#Copyright (C) 2014  David Delgado Hernandez 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import getopt
import glob
import re


def main(argv):

    """maneja los argumentos y los asigna a variables para su posterior manejo"""
    try:
        options , arg = getopt.getopt(argv, "d:R:",["directorio:","recursivo="])
    except getopt.GetoptError:
        print "el argumento no es valido"
    

    for opt , arg in options:
        if opt in ("-R" , "--recursivo"):
            Go_dir(arg,'R')
        if opt in ("-d" , "--directorio"):
            Go_dir(arg,None)


def Go_dir(usr_path,data=None):

    """funcion de entrada, busca los directorios y lo envia a su respectiva funcion"""

    if os.path.exists(usr_path):

        if data == 'R':
            Recursive_dir(usr_path)
        else:
            Make_list(usr_path)

    else:

        obj = os.path.basename(usr_path)

        root = os.path.dirname(usr_path)

        candidates = os.listdir(root)

        for i in candidates:
            if re.search(obj,i):

                if data == 'R':
                    Recursive_dir(os.path.join(root,i))
                else:
                    Make_list(os.path.join(root,i))


def Recursive_dir(path):
    """crea listas de forma recursiva"""

    origin = os.getcwd()
    os.chdir(path)

    for root, dirs, files in os.walk(path, topdown=False):
        if len(dirs) <= 0:
            Make_list(path)

        for name in dirs:

            Make_list(os.path.join(root,name))

    os.chdir(origin)


def Make_list(path):

    """funcion principal,crea las listas """


    origin = os.getcwd()
    os.chdir(path)

    titulo =os.path.basename(path)

    

    audio = glob.glob('*.mp3')

    if len(audio) <= 0:
        return 0
        
    print "creando la lista %s" %titulo
    playlist = open(titulo + '.m3u','w')

    audio.sort()


    for i in audio:
        playlist.write(i+'\n')

    print "la lista se guardo en %s" %path + titulo + '.m3u'
    playlist.close()

    os.chdir(origin)


if __name__ == '__main__':
    main(sys.argv[1:])