#!/usr/bin/env python2.7
import sys
import os
import shutil


def main(path):
    path = path[0]
    errors = []

    for root, dirs, files in os.walk(path):
        print path
        if not os.path.exists(os.environ['HOME']+'/Musica/convertidos/'):
            os.mkdir(os.environ['HOME']+'/Musica/convertidos')

        if not os.path.exists(os.environ['HOME']+'Videos/listos/'):
        	os.mkdir(os.environ['HOME']+'Videos/listos/')
            # revisamos el tamano
            # convertimos el archivo
            # lo movemos a convertidos 
            # el archivo original lo movemos a listo
        for f in files:
     		
     		if os.path.getsize(os.path.join(root,f)) >= 1000:
                    print 'hola'
                    ruta = os.path.join(os.path.root,f)
                    comando = 'ffmpeg -i %s -vn -ar 44100 -ac 2 -ab 128 -f mp3'%ruta
                    comando = comando + ' '+ os.path.splitext(f)[0]+'.mp3'
                    os.system(comando)

                    shutil.move(ruta,os.environ['HOME']+'/Videos/listos')
                    shutil.move(os.path.splitext(ruta)[0]+'.mp3',os.environ['HOME']+'/Musica/convertidos')

                else:
                # registramos los archivos con errores
                    errors.append(f)

    if len(errors):
        log = open(os.environ['HOME']+'/Documentos/mis_logs')
        for i in errors:
            log.write(f+'\n')



if __name__ == '__main__':
	main(sys.argv[1:])