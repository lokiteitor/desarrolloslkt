#!/usr/bin/env python2.7

import os
import sys
import pdb


# modificamos el path para poder acceder mejor a los modulos
this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]

# /home/lokiteitor/git/swiss-manager
sys.path.insert(0,trunk_dir)
# print sys.path
# print this_dir
from LktUtility import Log



L = Log.Log('logtest.log',this_dir)

lista = ['elemento1','elemento2','elemento3','elemento4']

tupla = ('elemento1','elemento2','elemento3','elemento4')

diccionario = {'1':'2',2:'hola',True:False}


L.add(True,lista)

L.add(False,lista)
L.space(2)
L.division(1)

L.add(True,tupla)
L.add(False,tupla)
L.space(2)
L.division(1)

L.add(True,diccionario)
L.add(False,diccionario)
L.space(2)
L.division(1)


# TODO : Error al intentar recorrer booleano
L.add('elemento1',lista,False,3,tupla,diccionario)

L.space(4)
L.division(1)

L.add(L.listerrors)

# print L.listerrors
# print L.LOG
L.MakeLog()


