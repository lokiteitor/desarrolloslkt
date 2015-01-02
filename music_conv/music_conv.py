#!/usr/bin/env python2.7
import sys
import os
import shutil
import glob
import getopt
import re

from LktUtility import xdg_api
from LktUtility import Log

# sencillo script que permite la conversion por lotes de archivos .3gp a .mp3
# haciendo uso de FFMPEG

# TODO : utilizar ordenamiento inteligente

###########################################################################
# Codigo en Funcion
X = xdg_api.XdgConfig()
L = Log.Log('music_conv.log')

# SALIDA = os.path.join(X.get("xdg_music_dir"),'convertidos/')
# LISTOS = os.path.join(X.get("xdg_videos_dir"),"listos/")
# DISP = os.path.join(xdg_api.getMountDirectory,'LOKITEITOR/Musica/anime')
# debug constantes
DISP = '/home/lokiteitor/Laboratorio/anime'
SALIDA = '/home/lokiteitor/Laboratorio/opend'
LISTOS = '/home/lokiteitor/Laboratorio/listos'

def main(argv):
    # crear un menu de entrada
    # -C: --clean= : limpiar archivos repetidos -> CleanRepeat
    #       @requiere un directorio sobre el que actuar
    # -c:--convert= : convertir de video a audio -> Convert
    #       @directorio donde se encuentran los videos

    try:
        options , arg = getopt.getopt(argv, "Cc:",["clean=:","convert="])
    except getopt.GetoptError:
        print "el argumento no es valido"

    for opt , arg in options:
        if opt in ("-C" , "--clean"):
            if arg:
                CleanRepeat(other=arg)
            else:
                CleanRepeat()

        if opt in ("-c" , "--convert"):
            if arg:
                Convert(arg)
            else:
                mens = 'Se requiere la ruta hacia los videos'
                print mens

                L.listerrors.append(mens)



def CleanRepeat(original=DISP,other=SALIDA):

    # TODO : funcion de momento inservible
    # recorrer directorios


    # limpiar los archivos repetidos basandose en la calidad para 
    # eliminarlos

    # dar por obvio que @original es el dispositivo de destino Final
    # @other : es un directorio definido por el usuario y que por default es SALIDA
    files = getAllFiles(other)

    commonfiles = []
    filesok = []
    nofiles = []

    for i in os.listdir(original):
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
                commonfiles.append((files[x][1],i))
                filesok.append(x)
            
    for i in commonfiles:
        # devolver los resultados y realizar limpieza

        CleanFile(os.path.join(other,i[0]),os.path.join(original,i[1]))

    # testear que archivos no coincidieron con algun directorio

    for i in files.keys():
        if filesok.count(i):
            continue
        else:
            nofiles.append(i)

    L.listerrors.append('\n\n')
    for i in nofiles:
        L.listerrors.append(i)

    print "limpieza Finalizada"

    L.MakeLog()



############################Funciones de limpieza############################
def CleanFile(path,dirpath):

    filenameother = os.path.basename(path)
    # print filenameother
    R = re.compile('_low')

    deletecandidate = []
    movecandidate = []
    error = []


    for i in os.listdir(dirpath):
        name = R.sub('',os.path.splitext(i)[0])



        if name == os.path.splitext(filenameother)[0]:
            if i.count('_low'):
                deletecandidate.append(i)
                movecandidate.append((dirpath,path))

            elif os.path.getsize(os.path.join(dirpath,i)) >= os.path.getsize(path):
                deletecandidate.append(i)
                movecandidate.append((dirpath,path))
            else:
                error.append(i)

    return deletecandidate,movecandidate,error


##########################funciones de filtraje############################

def getPrimaryPattern(name):
    # obtener cuanto vale cada letra dentro del patron
    # extraer caracteres no alfabeticos
    # extraer la extencion del archivo

    R = re.compile('[^a-z ]',re.IGNORECASE)

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

        index[filename] = (getProbability(i),i)

    return index
##########################terminan funciones de filtraje######################

# TODO : implentar funcion para guardar y restaurar datos en xml

def Convert(path):

    os.chdir(path)
    
    lista = glob.glob('*.3gp') + glob.glob('*.mp4')

    if not os.path.exists(SALIDA):
        os.mkdir(SALIDA)

    if not os.path.exists(LISTOS):
        os.mkdir(LISTOS)

    for i in lista:

        if os.path.getsize(i) >= 1000:

            other_i = i.replace(' ','\\ ')
            other_i = other_i.replace('(','\\(')
            other_i = other_i.replace(')','\\)')
            other_i = other_i.replace('&','\\&')
            other_i = other_i.replace('\'','\\\'')
            other_i = other_i.replace('`','\\`')

            out = os.path.splitext(other_i)[0] + '.mp3'
            orden = 'ffmpeg -i %s -vn -ar 44100 -ac 2 -ab 256k -f mp3 '%other_i
            orden = orden + out
            os.system(orden)

            if os.path.exists(os.path.splitext(i)[0] + '.mp3'):
                if os.path.getsize(os.path.splitext(i)[0] + '.mp3') >= 1000:
                    #agregar validacion de existencia en SALIDA
                    try:
                        shutil.move(os.path.splitext(i)[0]+'.mp3',SALIDA)
                        shutil.move(i,LISTOS)
                    except:
                        L.listerrors.append('el archivo %s ya existe\n'%SALIDA)
                        #TODO : remover el archivo duplicado

        else:

            L.listerrors.append(i+'\n')
            L.listerrors.append(orden+'\n')
            L.listerrors.append(other_i+'\n')
            L.listerrors.append(out+'\n')
            L.listerrors.append('################################################'+'\n')


def CheckError():
    error = [[],[],[]]
    # [['error de tamano'],['error de conversion'],['faltantes']]
    neverconvert = os.listdir(os.getcwd())
    error[1].append(neverconvert)

    os.chdir(SALIDA)

    now = os.listdir(os.getcwd())

    for i in now:
        if os.path.getsize(i) <= 1000:
            error[0].append(i)

    os.chdir(LISTOS)

    listos = os.listdir(os.getcwd())
    for i in listos:
        if os.path.getsize(i) <= 1000:
            error[0].append(i)

        new_i = os.path.splitext(i)[0] + '.mp3'

        if not new_i in now:
            error[2].append(new_i)

    # Registrar los errores

    if len(error[0]):
        L.listerrors.append('error de tamano\n')

        for x in error[0]:
            L.listerrors.append(x+'\n')

    if len(error[1]):
        L.listerrors.append('error de conversion\n')
        for x in error[1]:
            for y in x:
                L.listerrors.append(y+'\n')

    if len(error[2]):
        L.listerrors.append('faltantes\n')
        for x in error[2]:
            L.listerrors.append(x+'\n')

    L.listerrors.append('FIN\n')

    L.MakeLog()
    

if __name__ == '__main__':
    main(sys.argv[1:])
    CheckError()
