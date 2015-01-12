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
        if len(i) == 0:

            index = pathsplit.index(i)

            pathsplit.pop(index)
            
    # Obtiene el porcentaje de valor para la frase
    # ademas de obtener el minimo de palabras suficientes para validar(50%)
    # obtiene la cadena minima
    tam = len(pathsplit)

    porc = 100/tam

    minimo = 50 / porc

    minimo += 1

    minpath = " ".join(pathsplit[:minimo])


    return minpath


def getAllFiles(path):
    # precarga todas las direcciones a evaluar

    index = {}
    for i in os.listdir(path):
        filename = " ".join(getPrimaryPattern(i))

        index[filename] = getProbability(i)

    return index

def main():
    files = getAllFiles(FILES)

    commonfiles = []
    filesok = []
    nofiles = []

    for i in os.listdir(DIRS):
        # listar los directorios que seran evaluados 
        # sobre los archivos debido a que estos contiene una definicion mas 
        # clara

        r = getPrimaryPattern(i)

        porcion = getProbability(r)

        # ignorar palabras de longitud menor a 4
        if len(porcion) >= 4:
            common = re.compile(porcion,re.IGNORECASE)
        else:
            continue


        for x in files.keys():
            # compilar un patron y analizar

            if common.search(x):
                commonfiles.append( x + '\n\t' + i)
                filesok.append(x)
            
        L.listerrors.append(r) 
        L.listerrors.append(i)
        L.listerrors.append(porcion+'\n')


    for i in commonfiles:
        L.listerrors.append(i)

    # testear que archivos no coincidieron con algun directorio

    for i in files.keys():
        if filesok.count(i):
            continue
        else:
            nofiles.append(i)

    L.listerrors.append('\n\n')
    for i in nofiles:
        L.listerrors.append(i)


if __name__ == '__main__':
    main()
    L.MakeLog()