#!/usr/bin/env python2.7
import sys
import os
import datetime
import xml.etree.ElementTree as ET


class Normalize():
    """identifica, registra y normaliza las rutas adecuandolas para el 
       grabado de CD/DVD"""
    def __init__(self):
        self.LOG = os.environ['HOME']+'/Documentos/mis_logs/normpath.log'
        self.listerrors = []

        # self.recorrer
        # permitir la entrada a travez de la interfaz de BraseroProject
    def Check(self):

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

        # revisar si el archivo:
        # existe
        # es un enlace simbolico
        # es un archivo oculto

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

class BraseroProject():
    """parsea un proyecto guardado con brasero para poder suplir de rutas
       al normalizador de rutas"""
    def __init__(self, proyect):
        
        self.proyect = proyect

        self.xml = ET.parse(self.proyect)

        self.root = self.xml.getroot()

        self.objetives = []

        self.getGraft()
        self.iterPath()

    def getGraft(self):
        
        self.data = self.root.find('track').find('data')

        self.graft = self.data.findall('graft')

    def iterPath(self):
        
        for i in self.graft:
            path = i.find('path').text
            uri = i.find('uri').text

            path = path.encode('utf-8')

            uri = uri.replace('file%3A%2F%2F%2F','/')
            uri = uri.replace('%2F','/')
            uri = uri.replace('%2520',' ')

            uri = self.replaceLastPatch(uri,path)

            self.objetives.append((path,uri))



    def replaceLastPatch(self,uri,path):
        # TODO : revisar la existencia de la ruta producto de no existir someter
        # a un proceso de revision o registro de error
        
        sep = uri[0:10].encode('utf-8')

        tuplesep = uri.partition(sep)

        uri = tuplesep[0] + path
        uri.encode('utf-8')

        return uri



if __name__ == '__main__':
    main(sys.argv[1])