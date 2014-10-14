#!/usr/bin/env python2.7
import sys
import os
import datetime
import xml.etree.ElementTree as ET

import getopt

import pdb

class Log(object):
    """Administrador de errores"""
    def __init__(self):

        self.LOG = os.environ['HOME']+'/Documentos/mis_logs/normpath.log'

        self.listerrors = []
        self.Logmodule = self.__class__
                
    def MakeLog(self):

        self.checkLog()

        with open(self.LOG,'a') as filelog:

            now = datetime.datetime.now().strftime('%d/%m/%Y'+'  %H:%M')

            filelog.write(str(self.Logmodule)+'\n')
            filelog.write(now+'\n')

            for i in self.listerrors:

                filelog.write(i+'\n')

    def checkLog(self):
        
        if not os.path.exists(os.path.dirname(self.LOG)):

            os.mkdir(os.path.dirname(self.LOG))


class Normalize(Log):
    """identifica, registra y normaliza las rutas adecuandolas para el 
       grabado de CD/DVD"""
    def __init__(self,lst=False):
        super(Normalize, self).__init__()

        self.lst = []

        if lst:
            self.lst = lst

            for i in self.lst:
                self.filter(i)

    def Check(self):

        if len(self.listerrors) > 0:

            self.MakeLog()

    def recorrer(self,path):

        for root, dirs, files in os.walk(path):

            for i in files:

                self.filter(i)

    def filterAlert(self,path,error):

        # TODO : Ordenar por fallas e imprimir en orden clasificado

        print "el archivo %s necesita atencion"
        print "     " + error

        regerror = path + ' : ' + error

        self.listerrors.append(regerror)
        
    def filter(self,path,isuri=False):
        
        if isuri:
            if not os.path.exists(path):

                error = "la ruta no existe"
                self.filterAlert(path,error)

                if os.path.islink(path):

                    error = "la ruta es un enlace simbolico"    
                    self.filterAlert(path,error)

                if os.path.basename(path)[0] == '.':
                    
                    error = "la ruta esta oculta"
                    self.filterAlert(path,error)

        else:

            if len(path) > 63:
                error = "el path excede los 64 caracteres"
                self.filterAlert(path,error)

    def Exit(self):
        self.Check()
        print 'se encontraron ' + str(len(self.listerrors)) + 'problemas'


class BraseroProject(Log):
    """parsea un proyecto guardado con brasero para poder suplir de rutas
       al normalizador de rutas"""
    def __init__(self, proyect):

        super(BraseroProject,self).__init__()

        self.proyect = proyect

        self.xml = ET.parse(self.proyect)

        self.root = self.xml.getroot()
        self.getGraft()

        self.objetives = []
        self.onlyPath = []
        self.onlyUri = []
        self.badfiles =[]


        self.iterPath()

        self.Check()


    def getGraft(self):
        
        self.data = self.root.find('track').find('data')

        self.graft = self.data.findall('graft')

    def iterPath(self):

        for i in self.graft:
            try:
                path = i.find('path').text
                uri = i.find('uri').text
            
                path = path.encode('utf-8')

                uri = uri.replace('file%3A%2F%2F%2F','/')
                uri = uri.replace('%2F','/')
                uri = uri.replace('%2520',' ')

                uri = self.replaceLastPatch(uri,path)

                self.objetives.append((path,uri))

                self.onlyPath.append(path)

                self.onlyUri.append(uri)
            except:
                self.badfiles.append((path,uri))

                path = None
                uri = None

    def replaceLastPatch(self,uri,path):
        # TODO : revisar la existencia de la ruta producto de no existir someter
        # a un proceso de revision o registro de error
        
        sep = uri[0:10].encode('utf-8')

        tuplesep = uri.partition(sep)

        uri = tuplesep[0] + path

        return uri

    def Check(self):

        if len(self.badfiles) > 0:

            print "Se han encontrado errores en durante el analizis del proyecto"
            print "Revise su archivo de LOG"

            for i in self.badfiles:

                regerror = i[0] + " : " + i[1]

                self.listerrors.append(regerror)

            self.MakeLog()

def main(argv):
    
    optionSingle = "p:"
    listOptions = ["proyect="]
    try:
        options , arg = getopt.getopt(argv,optionSingle,listOptions)
    
    except getopt.GetoptError:
        print "el argumento no es valido"        

    for opt , arg in options:

        proyect = arg if (opt  in ("-p","--proyect")) else False


    ##########################################################

    if proyect:

        brasero = BraseroProject(proyect)

        lst = brasero.onlyUri

        filterpath = Normalize(lst)

        for i in brasero.onlyPath:

            filterpath.filter(i)

        filterpath.Exit()

if __name__ == '__main__':
    main(sys.argv[1:])
