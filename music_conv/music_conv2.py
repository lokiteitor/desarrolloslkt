#!/usr/bin/env python2.7
import sys
import os
import shutil
import glob
import getopt
import re
from ConfigParse import ConfigParse


from LktUtility import xdg_api
from LktUtility import Log

# sencillo script que permite la conversion por lotes de archivos .3gp a .mp3
# haciendo uso de FFMPEG

# TODO : utilizar ordenamiento inteligente

###########################################################################
# Codigo en Funcion
X = xdg_api.XdgConfig()
L = Log.Log('music_conv')

# lista de seguimiento de archivos modificados

seglist = []



config = ConfigParse("dirs.conf")

SALIDA = config.get("DIRS","salida")
LISTOS = config.set("DIRS","terminados")
DISP = config.set("DIRS","entrada_default")

def main(argv):
    # crear un menu de entrada
    # -C: --clean= : limpiar archivos repetidos -> CleanRepeat
    #       @requiere un directorio sobre el que actuar
    # -c:--convert= : convertir de video a audio -> Convert
    #       @directorio donde se encuentran los videos

    try:
        options , arg = getopt.getopt(argv, "Cc:",["clean=:","convert="])
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

                L.add(mens)



def CleanRepeat(original=DISP,other=SALIDA):
    # limpiar los archivos repetidos basandose en la calidad para 
    # eliminarlos

    # dar por obvio que @original es el dispositivo de destino Final
    # @other : es un directorio definido por el usuario y que por default es SALIDA
    files = getAllFiles(other)

    commonfiles = []
    filesok = []
    nofiles = []



    for i in os.listdir(original):
        # listar los directorios que seran evaluados 
        # sobre los archivos debido a que estos contiene una definicion mas 
        # clara

        r = getPrimaryPattern(i)
        porcion = getProbability(r)

        # ignorar palabras de longitud menor a 4
        if len(porcion) >= 4:
            common = re.compile(porcion,re.IGNORECASE)
        else:
            continue

        for x in files.keys():
            # compilar un patron y analizar

            if common.search(x):
                commonfiles.append((files[x][1],i))
                filesok.append(x)
            
    for i in commonfiles:
        # devolver los resultados y realizar limpieza
        # deletecandidate,movecandidate,error
        # archivo a borrar, a mover y error presentado

        Selectfile(os.path.join(other,i[0]),os.path.join(original,i[1]))

    G = GarbageCollector(seglist)
    G.InfoLog()
    # testear que archivos no coincidieron con algun directorio

    for i in files.keys():
        if filesok.count(i):
            continue
        else:
            nofiles.append(i)

    L.listerrors.append('\n\n')
    for i in nofiles:
        L.listerrors.append(i)

    print "limpieza Finalizada"

    

    L.MakeLog()

    return

############################Recolector de basura##############################
# realiza todas las funciones de limpieza
class GarbageCollector(object):
    """Realiza las funciones de limpieza en base a un diccionario que indica 
       los elementos a vaciar, eliminar, mover, o renombrar"""
    def __init__(self, tasklist):
        super(GarbageCollector, self).__init__()
        # resive una lista con diccionarios que posteriormente desempaquetara
        self.tasklist = tasklist
        # archivos que no existen
        self.inexist = [] 
        # archivos elimindados
        self.deletefiles = []


        for i in tasklist:
            self.RouteTask(i)

        for i in self.inexist:
            L.add(i)

    def RouteTask(self,task):
        # estas son las tareas que es  capaz de routear
        # delete : eliminar un archivo
        # move : mover un archivo
        # error : imprimir en el log los errores empaquetados

        # estos son los parametros que comprueba
        # name : nombre del archivo principal
        # deletecandidate : nombre del archivo a borrar path absoluto
        # movecandidate : nombre del archivo a mover path absoluto
        # dirmovecandidate : nombre del directorio al que se movera el archivo 
        # error : lista de errores que se deben de imprimir
        
        if task.has_key('tasks'):

            if 'delete' in task['tasks']:

                self.deleteTask(task['deletecandidate'])

            if 'move' in task['tasks']:

                self.moveTask(task['movecandidate'],task['dirmovecandidate'])

    def deleteTask(self,path):
        if os.path.exists(path):
            self.deletefiles.append(os.path.basename(path))
            os.remove(path)
        else:
            self.inexist.append(path)

    def moveTask(self,origin,dest):
        if os.path.exists(origin):

            shutil.move(origin,dest)
        else:
            self.inexist.append(dest)

    def errorTask(self,error):

        L.add(error)
        L.space()

    def InfoLog(self):
        if len(self.deletefiles) > 0:
            L.add(False,'los siguientes archivos han sido elimindados\n')
            L.add(True,self.deletefiles)

        L.MakeLog()
############################Funciones de limpieza############################
def Selectfile(path,dirpath):

    filenameother = os.path.basename(path)

    R = re.compile('_low')

    for i in os.listdir(dirpath):
        name = R.sub('',os.path.splitext(i)[0])



        if name == os.path.splitext(filenameother)[0]:
            # revisa dos posibilidades en caso de no coincidir ninguna no hace 
            # nada
            if i.count('_low'):
                deletecandidate = os.path.join(dirpath,i)
                movecandidate = path
                dirmovecandidate = dirpath

            elif os.path.getsize(os.path.join(dirpath,i)) >= os.path.getsize(path):
                deletecandidate = os.path.join(dirpath,i)
                movecandidate = path
                dirmovecandidate = dirpath
            else:
                error = i
                deletecandidate = movecandidate = dirmovecandidate =''

            error = '' if (deletecandidate != '') else error

            if error != '':
                print "se encontro un error en ",filenameother
                print "\t\t",error

            # estructura sobre la que se informan los seguimientos
            # agregar la structura a una lista para posteriormente registrarla
            # en el Log

            bitacora = {
            'name' : filenameother,
            'deletecandidate' : deletecandidate,
            'movecandidate' : movecandidate,
            'dirmovecandidate' : dirmovecandidate,
            'error' :  error,
            'tasks' : ('delete','move','error')
            }

            seglist.append(bitacora)



    # pasar a funciones de limpieza



##########################funciones de filtraje############################

def getPrimaryPattern(name):
    # obtener cuanto vale cada letra dentro del patron
    # extraer caracteres no alfabeticos
    # extraer la extencion del archivo

    R = re.compile('[^a-z ]',re.IGNORECASE)

    name = name.replace(os.path.splitext(name)[1],'')
    name = name.replace('-',' ')
    name = name.replace('~',' ')

    name = R.sub('',name)

    res = name.split(' ')

    return res


def getProbability(pathsplit):

    # recibe una lista con la cadena divida

    for i in pathsplit:
        if len(i) == 0:

            index = pathsplit.index(i)

            pathsplit.pop(index)

    # Obtiene el porcentaje de valor para la frase
    # ademas de obtener el minimo de palabras suficientes para validar(50%)
    # obtiene la cadena minima
    tam = len(pathsplit)
    porc = 100/tam
    minimo = 50 / porc
    minimo += 1
    minpath = " ".join(pathsplit[:minimo])

    return minpath

def getAllFiles(path):
    # precarga todas las direcciones a evaluar

    index = {}
    for i in os.listdir(path):
        filename = " ".join(getPrimaryPattern(i))

        index[filename] = (getProbability(i),i)

    return index
##########################terminan funciones de filtraje######################

# TODO : implentar funcion para guardar y restaurar datos en xml

def Convert(path):

    os.chdir(path)
    
    lista = glob.glob('*.3gp') + glob.glob('*.mp4')

    if not os.path.exists(SALIDA):
        os.mkdir(SALIDA)

    if not os.path.exists(LISTOS):
        os.mkdir(LISTOS)

    for i in lista:

        if os.path.getsize(i) >= 1000:

            remplaza = [' ','(',')','&','\'','`']
            remplazo = ['\\ ','\\(','\\)','\\&','\\\'','\\`']
            other_i = i

            for x in xrange(0,5):
                other_i = other_i.replace(remplaza[x],remplazo[x])

            out = os.path.splitext(other_i)[0] + '.mp3'
            orden = 'ffmpeg -i %s -vn -ar 44100 -ac 2 -ab 256k -f mp3 '%other_i
            orden = orden + out

            # TODO: Crear multiproceso en esta tarea
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

            output = i + '\n' + orden + '\n' + other_i + '\n' + out + '\n' 

            L.add(output)
            L.add('################################################'+'\n')


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




