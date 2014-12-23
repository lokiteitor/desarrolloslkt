#!/usr/bin/env python2.7

import os
import sys
import datetime
import re



class Log(object):
    """Administrador de errores"""
    def __init__(self):

        self.LOG = os.environ['HOME']+'/Documentos/mis_logs/backup.log'

        self.listerrors = []
        # self.Logmodule = self.__class__
                
    def MakeLog(self):

        self.checkLog()

        with open(self.LOG,'a') as filelog:

            now = datetime.datetime.now().strftime('%d/%m/%Y'+'  %H:%M')

            filelog.write('\n\n'+str(self.Logmodule)+'\n')
            filelog.write(now+'\n')

            for i in self.listerrors:

                filelog.write(i+'\n')

    def checkLog(self):
        
        if not os.path.exists(os.path.dirname(self.LOG)):

            os.mkdir(os.path.dirname(self.LOG))

class PackTarball(object):
    """Encargada de empaquetar los paquetes que haci se requieran"""
    def __init__(self, finalpath):
        self.finalpath = finalpath

    def function(self):
        pass

        
def FilterUsb(listdir):

    excep = []

    # filtrar los paths para dispositivos usb
    for i in listdir:

        if i.find(':') > 0:

            menexp = ['la ruta es invalida para un USB',i,'empaquetando:',i]
            # TODO : Definir regError
            excep.append(i)
            Log.regError(menexp)

    # TODO : Agregar soporte para enlaces simbolicos

    return excep


def MakeBackup():
    # hacer el backup desde rsync capturar los errores
    pass

###########################################################################
# codigo actualmente en funcionamiento

def filterVersion(path,repo):
    # filtrar los paquetes por version
    # retorna una diccionario que contiene todas las repeticiones

    # por razones de eficiencia debe de: 
    # @path : debe de ser el directorio con la menor cantidad de archivos
    # @repo : debe de ser el directorio con la mayor cantidad de archivos

    lista = os.listdir(path)

    listrepo = os.listdir(repo)

    matchlist = {}

    pat = re.compile('\d')

    for i in lista:

        sub1 = pat.sub('',i)

        # obtener entero de i

        sinnum = re.compile('\D')
        # asignarlo como el mayor
        mayor = i
        versionmayor = sinnum.sub('',i)

        rest = []

        for x in listrepo:

            sub2 = pat.sub('',x)

            if sub2 == sub1 and x != i:

                rest.append(x)
                # comprobar si es el mayor

                if sinnum.sub('',x) > versionmayor:

                    mayor = x

        if rest:
            if mayor != i:
                rest.append(i)

                rest.remove(mayor)

            matchlist[mayor] = rest

    return matchlist





def RemoveGarbage(dirname,pack):

    # TODO : agregar registros de cambios

    for i in pack.keys():

        objetive = pack[i]

        for x in objetive:

            # TODO : agregar filtro contra errores
            try:
                os.remove(os.path.join(dirname,x))
            except Exception,e:

                error = os.path.join(dirname,x) + '\t' + str(e)
                Register.listerrors.append(error)



##############
# globals
##############

Register = Log() 



def main():
    
    DIR = '/run/media/lokiteitor/lkt/pkg/'

    REPO = '/var/cache/pacman/pkg/'

    ls1 = len(os.listdir(DIR))
    ls2 = len(os.listdir(REPO))

    if ls1 >= ls2:

        listobjetive = filterVersion(DIR,REPO)
    else:
        listobjetive = filterVersion(REPO,DIR)


    RemoveGarbage(DIR,listobjetive)



if __name__ == '__main__':
    main()

    Register.MakeLog

