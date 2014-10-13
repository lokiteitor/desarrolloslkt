#!/usr/bin/env python2.7
import sys
import os
import shutil
import glob

# sencillo script que permite la conversion por lotes de archivos .3gp a .mp3
# haciendo uso de FFMPEG


SALIDA = os.environ['HOME']+'/convertidos/'
LISTOS = os.environ['HOME']+'/listos/'
LOG = os.environ['HOME']+'/mis_logs/music_conv.log'

def main(path):
    os.chdir(path)

    
    lista = glob.glob('*.3gp') + glob.glob('*.mp4')

    if not os.path.exists(os.environ['HOME']+'/Musica/convertidos/'):
        os.mkdir(os.environ['HOME']+'/Musica/convertidos')

    if not os.path.exists(os.environ['HOME']+'/Videos/listos/'):
        os.mkdir(os.environ['HOME']+'/Videos/listos/')

    if not os.path.exists(os.environ['HOME']+'/Documentos/mis_logs'):
        os.mkdir(os.environ['HOME']+'/Documentos/mis_logs')



    log = open(LOG,'a')

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
                        log.write('el archivo %s ya existe\n'%SALIDA)
                        #TODO : remover el archivo duplicado


        else:
            

            log.write(i+'\n')
            log.write(orden+'\n')
            log.write(other_i+'\n')
            log.write(out+'\n')
            log.write('################################################'+'\n')

    log.close()


def CheckError():
    log = open(LOG,'a')
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

    log.write('lista de errores\n')
    log.write('error de tamano\n')
    for x in error[0]:
        log.write(x+'\n')

    log.write('error de conversion\n')
    for x in error[1]:
        for y in x:
            log.write(y+'\n')

    log.write('faltantes\n')
    for x in error[2]:
        log.write(x+'\n')

    log.write('FIN\n')
    
    log.close()




if __name__ == '__main__':
    main(sys.argv[1])
    CheckError()

