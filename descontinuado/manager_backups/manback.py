#!/usr/bin/env python2.7

# #Copyright (C) 2014  David Delgado Hernandez 
# # This program is free software: you can redistribute it and/or modify
# # it under the terms of the GNU General Public License as published by
# # the Free Software Foundation, either version 2 of the License, or
# # (at your option) any later version.

# # This program is distributed in the hope that it will be useful,
# # but WITHOUT ANY WARRANTY; without even the implied warranty of
# # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# # GNU General Public License for more details.

# # You should have received a copy of the GNU General Public License
# # along with this program. If not, see <http://www.gnu.org/licenses/>.


# este script permite abstraer de la configuracion de rsync(por defecto)
# automatizando el reconocimiento de archivos a directorios y determinando de 
# forma inteligente el destino del backup

# el script fue hecho de origen para uso personal por lo que puede ser modificado
# sin riesgo en los lugares en que se especefiquen

# # para que este script pueda funcionar de forma apropiada es necesita tener
# # instalado rsync

# # el programa toma su configuracion inicial desde el archivo ubicado env
# # /home/user/.config/manager_backup/config
# # desde el cual toma sus valores para listar los directorios objetivo del
# # backup.
# # el archivo de log se encuetra ubicado en /home/user/.config/manager_backup/log

# este programa permite hacer un backup de forma automatica a los archivos que
# se encuentren en el listado de objetivos o de forma especifica a los archivos 
# proporcionados. Diferenciando los archivos de los directorios para poder abstraer
# la configuracion de rsync

import sys
import getopt


# entidad de entrada de datos a traves de linea de comandos

class Gui():
    """proporciona una seleccion de las opciones. es el punto de entrada del
       sistema pero no es la logica del mismo conforma la lista de tareas que
       entragara a la entidad ruteadora"""
    def __init__(self, args):
        # costruye el menu toma las respuestas y devuelve true si hay opciones
        # disponibles
        self.args = args
        self.task = {}
        self.optionSingle = "alhs:A:r:B:C:R:"
        self.listOptions = ["all","list","help","select=","add=","remove=","autobackup=",
                            "config=","restore="]
        try:
            options , arg = getopt.getopt(self.args, self.optionSingle,self.listOptions)
        except getopt.GetoptError:
            print "el argumento no es valido"        

        for opt , arg in options:

            self.task['all'] = [True,[]] if (opt in ("-a","--all")) else [False]

            self.task['list'] = [True,[]] if (opt in ("-l","--list")) else [False]


            if opt in ("-h","--help"):
                # ir a help
                pass

            self.task['select'] = [True,[arg]] if (opt in ("-s","--select")) else [False]

            self.task['add'] = [True,[arg]] if (opt in ("-A","--add")) else [False]

            self.task['remove'] = [True,[arg]] if (opt in ("-r","--remove")) else [False]

            self.task['autobackup'] = [True,[arg]]  if (opt in ("-B","--backup")) else [False]

            self.task['config'] = [True,[arg]] if (opt in ("-C","--config")) else [False]

            self.task['restore'] = [True,[arg]] if (opt in ("-R","--restore")) else [False]


        def __help(self):
            # hacer ayuda
            pass
        
        def geTask(self):
            
            if not options:
                self.request = False
                return False

            self.request = True

            return self.task

class Router():
    """se encarga de gestionar los argumentos ejecutando las tareas asignadas 
       enruta la informacion apropiada (y desempaqueta si es necesario) hacia 
       las funciones encargadas. es el nucleo del sistema pero no es quien 
       ejecuta las tareas diversas tan solo gestiona"""
    def __init__(self, task):

        # obtenemos el paquete de lista de tareas si esta vacio activamos la
        # bandera de accion por defecto
        
        self.task = task
        self.flagDefault = False
        self.listTask = []
        
        if task == False:

            self.flagDefault = True

    def ExecTask(self):

        # ejecuta las tareas predefinidas si no ejecuta la accion por defecto

        if self.flagDefault:

            # saltar directo a la opcion por defecto
            pass

        self.__checkTask()

        self.__iterationTask()

    def __checkTask(self):
        # revisa cuales tareas fueron activadas y las pasa a una lista
        # para revisar unicamente estas
        
        for i in self.task:

            if self.task[i][0]:

                self.listTask.append(i)

    def __unpack(self,index):
        # desempaqueta los argumentos de las opciones 
        # en caso de existir mas de una los separa
        # cada proceso es responsable de manejar el paquete por su cuenta

            if len(self.task[index][1][0]) > 0:

                extract = self.task[index][0][1]

                if extract.count(','):

                    pack = extract.split(',')
                else:
                    pack = [extract]

                return pack
            else:

                return False

    def __iterationTask(self):
        # obtiene el paquete de argumentos para cada opcion
        # de no encontrarse establece swt a false para informar que no tiene 
        # argumentos esa tarea
        
        for i in self.listTask:

            pack = self.__unpack(i)

            swt = True if (pack) else False

            self.__doTask(pack,swt)

    
    def __doTask(self,pack,switch):
        pass
                

if __name__ == '__main__':


    menu = Gui(sys.argv[1:])




    print menu.task


        