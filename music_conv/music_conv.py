#!/usr/bin/env python2.7
import sys
import os
import shutil
import glob
import getopt

from LktUtility import xdg_api
from LktUtility import Log

# sencillo script que permite la conversion por lotes de archivos .3gp a .mp3
# haciendo uso de FFMPEG

# TODO : utilizar ordenamiento inteligente

###########################################################################
# Codigo en Funcion
X = xdg_api.XdgConfig()
L = Log.Log('music_conv.log')

SALIDA = os.path.join(X.get("xdg_music_dir"),'convertidos/')
LISTOS = os.path.join(X.get("xdg_videos_dir"),"listos/")
# TODO : definir mediante una constante el dispositivo externo en el que se
#        almacena

DISP = os.path.join(xdg_api.getMountDirectory,'LOKITEITOR/Musica/anime')


def main(argv):
    # crear un menu de entrada
    # -C: --clean= : limpiar archivos repetidos -> CleanRepeat
    #       @requiere un directorio sobre el que actuar
    # -c:--convert= : convertir de video a audio -> Convert
    #       @directorio donde se encuentran los videos

    try:
        options , arg = getopt.getopt(argv, "C:c:",["clean=:","convert="])
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
    #   TODO : Definir esto en una constante
    # @other : es un directorio definido por el usuario y que por default es SALIDA

    for root, dirs, files in os.walk(original, topdown=False):

        for dirs in i:

            



    lista1 = os.listdir(original)
    lista2 = os.listdir(other)

    for i in lista1:

        for x in lista2:

            if i == x:
                tami = os.path.getsize(os.path.join(original,i))
                tamx = os.path.getsize(os.path.join(other,x))

                if tami >= tamx and os.path.exists(os.path.join(other,x)):

                    os.remove(os.path.join(other,x))

                elif os.path.exists(os.path.join(original,i)):

                    os.remove(os.path.join(original,i))

                    shutil.move(os.path.join(other,x),os.path.join(original,x))
                  
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

