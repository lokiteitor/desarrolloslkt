#!/usr/bin/env python2.7
import os
import datetime
import sys

# pasar como argumento una path
# si no existe recorrera la carpeta musica en home
# y la carpeta musica del celular las cuales estan definidas en dirs funcion
# main

# TODO : adaptarlo a rutas en otros dispositivos


def searching(path,log):

    for root, dirs, files in os.walk(path):

        for i in dirs:
            if i == 'n7p_art':
                delete = os.path.join(root,i)
                log.append(delete)
                deletedir(delete)

def deletedir(dirs):

    for root, dirs, files in os.walk(dirs,topdown=False):
        for name in files:
            obj =  os.path.join(root, name)
            os.remove(obj)
        for name in dirs:
            if not os.path.islink(name):
                os.rmdir(os.path.join(root, name))

        os.rmdir(root)

class logs():

    def __init__(self):

        self.f = open('/home/lokiteitor/Documentos/n7p_logs.txt','a')

        now = datetime.datetime.now().strftime('%d/%m/%Y'+'  %H:%M')

        self.f.write(now+'\n'+'\n')

        self.candidate = []

    def append(self,path):

        self.candidate.append(path)

        print path

    def writecandidate(self):

        for i in self.candidate:

            self.f.write(i+'\n')
        self.f.close()


def main(other_dir = None):
    history = logs()

    dirs = ['/home/lokiteitor/Musica','/run/media/lokiteitor/LOKITEITOR/musica']

    if other_dir != None:
        other_dir = str(other_dir)
        searching(other_dir,history)

    for i in dirs:
        searching(i,history)

    history.writecandidate()

if __name__ == '__main__':
    main(sys.argv[1:])