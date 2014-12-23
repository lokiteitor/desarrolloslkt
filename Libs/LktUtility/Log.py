#!/usr/bin/env python2.7

import os
import datetime

import xdg_api

X = xdg_api.XdgConfig()

class Log(object):
    """Administrador de errores"""
    def __init__(self,name,path=None):

        if path:
            path = os.path.join(path,'mis_logs/'+name)
        else:
            path = os.path.join(X.get('xdg_documents_dir'),'mis_logs/'+name)           
        
        self.LOG = path

        self.listerrors = []
        self.Logmodule = self.__class__
                
    def MakeLog(self):

        self.checkLog()

        with open(self.LOG,'a') as filelog:

            now = datetime.datetime.now().strftime('%d/%m/%Y'+'  %H:%M')

            filelog.write('\n\n'+str(self.Logmodule)+'\n')

            filelog.write(now+'\n')

            for i in self.listerrors:

                # TODO : agregar metodo capaz de agregar eventos a la pila de
                #       eventos y manejar eventualidades como errores de tipo 
                #       e iteracion de listas

                filelog.write(str(i)+'\n')

    def checkLog(self):
        
        if not os.path.exists(os.path.dirname(self.LOG)):

            os.mkdir(os.path.dirname(self.LOG))


