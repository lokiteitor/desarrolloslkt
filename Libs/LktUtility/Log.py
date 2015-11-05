#!/usr/bin/env python2.7

import os
import datetime
# import pdb

import xdg_api

X = xdg_api.XdgConfig()

class Log(object):
    """Administrador de errores"""
    def __init__(self,name,path=None,ext='.log'):
        name += ext

        if path:
            path = os.path.join(path,'logs/'+name)
        else:
            path = os.path.join(X.get('xdg_documents_dir'),'logs/'+name)           
        
        self.LOG = path

        self.listerrors = []
        self.backup = []
        self.Logmodule = self.__class__
                
    def MakeLog(self):

        self.checkLog()

        with open(self.LOG,'a') as filelog:

            now = datetime.datetime.now().strftime('%d/%m/%Y'+'  %H:%M')

            filelog.write('\n\n'+str(self.Logmodule)+'\n')

            filelog.write(now+'\n')

            for i in self.listerrors:

                filelog.write(str(i)+'\n')

        # vaciar la pila y hacer un respaldo
        for i in self.listerrors:
            self.backup.append(i)

        self.listerrors = []

    def checkLog(self):
        
        if not os.path.exists(os.path.dirname(self.LOG)):

            os.mkdir(os.path.dirname(self.LOG))

    def add(self,mensaje):
        if str(type(mensaje)) == "<type 'str'":
            self.listerrors.append(mensaje)

        else:
            raise TypeError

    # TODO : funcion que recorra un iterador recursivamente

    def additem(self,iterar=False,*argvc):
        # agregar eventos a la pila de eventos independientemente del tipo de
        # dato y maneja los iterables

        if len(argvc) > 0 and iterar == False:
            # pdb.set_trace()
            pass

        for i in argvc:
            if str(type(i)) == "<type 'list'>" or str(type(i)) == "<type 'tuple'>":
                if iterar:
                    for x in i:
                        self.add(False,x)
                else:
                    self.listerrors.append(i)

            elif str(type(i)) == "<type 'str'>" and iterar:
                for x in i:
                    self.listerrors.append(x)

            elif str(type(i)) == "<type 'dict'>" and iterar:
                for x in i.items():
                    self.add(False,x)
            else:

                self.listerrors.append(str(i))

    def space(self,num=1):
        for x in xrange(1,num):
            self.listerrors.append('\n')

    def division(self,num=1,char="#"):
        line = char * 78

        while num > 0:
            self.listerrors.append(line+'\n')
            num -= 1





