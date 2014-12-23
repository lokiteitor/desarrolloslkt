#!/usr/bin/env python2.7

# El objetivo es reconocer en base en una lista de archivos en cual 
# directorio es mas probable encontrar un objetivo 
# ademas de almacernar los archivos de esta lista basandonos en el nombre 
# del archivo y el patron que muestran 


import os
import re

from LktUtility import Log

FILES = os.path.join(os.getcwd(),"sandbox/Patrones/files")
DIRS = os.path.join(os.getcwd(),"sandbox/Patrones/dirs")
LOGS = os.path.join(os.getcwd(),"sandbox/Patrones/")

# FILES es un directorio con los archivos 
# DIRS es el lugar donde se guardaran y buscaran los archivos

L = Log.Log('Patrones.log',LOGS)

# TODO : Encontrar la forma de ignorar espacios vacios sin afectar el resultado
R = re.compile('[^a-z ]',re.IGNORECASE)

def getPrimaryPattern(name):
    # obtener cuanto vale cada letra dentro del patron
    # extraer caracteres no alfabeticos
    # extraer la extencion del archivo

    name = name.replace(os.path.splitext(name)[1],'')
    name = name.replace('-',' ')
    name = name.replace('~',' ')

    name = R.sub('',name)

    res = name.split(' ')

    return res

def getProbability(pathsplit):

    # recibe una lista con la cadena divida

    for i in pathsplit:
        if i == '':

            index = pathsplit.index(i)

            pathsplit.pop(index)



    print pathsplit

#


for i in os.listdir(FILES):

    r = getPrimaryPattern(i)

    # getProbability(r)

    L.listerrors.append(r) 
    L.listerrors.append(i+'\n')

L.MakeLog()







