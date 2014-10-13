#!/usr/bin/env python2.7
import sys
import os
import datetime


class Normalize():
    """identifica, registra y normaliza las rutas adecuandolas para el 
       grabado de CD/DVD"""
    def __init__(self):
        self.LOG = os.environ['HOME']+'/Documentos/mis_logs/music_conv.log'
        self.listerrors = []

        self.recorrer

        if len(self.listerrors) > 0:
            self.checkLog
            self.MakeLog

    def recorrer(self,path):

        for root, dirs, files in os.walk(path):

            for i in files:

                self.filter(i)

    def filterAlert(self,path,error):

        print "el archivo %s necesita atencion"
        print "     " + error

        regerror = path + ' : ' + error

        self.listerrors.append(regerror)

    def checkLog(self):
        
        if not os.exists(self.LOG):

            os.mkdir(self.LOG)
        
    def filter(self,path):
        
        if len(path) > 63:
            error = "el path excede los 64 caracteres"
            self.filterAlert(path,error)

    def MakeLog(self):

        with open(self.LOG,'a') as filelog:

            now = datetime.datetime.now().strftime('%d/%m/%Y'+'  %H:%M')

            filelog.write(now+'\n')

            for i in self.listerrors:

                filelog.write(i+'\n')

    def Exit(self):
        print 'se encontraron ' + len(self.listerrors) + 'problemas'


def main(path,arg):
    
    filter = Normalize()

    filter.Exit()
    

if __name__ == '__main__':
    main(sys.argv[1])