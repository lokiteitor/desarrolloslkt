#!/usr/bin/env python2.7

import os

import music_conv


def contar():
    fuente = []
    for root, dirs, files in os.walk(music_conv.DISP, topdown=False):
        for name in files:

            fuente.append(name)
    return fuente


def imprimir(original,fuente):
    print "el contenido reciente es:\n"

    for i in original:
        print "\t", i 

    print "el contenido en la fuente es:\n"

    for i in fuente:
            print "\t",i



# contar los archivos en ambos directorios

original = os.listdir(music_conv.SALIDA)
fuente = contar()

imprimir(original,fuente)


# ejecutar las tareas

music_conv.CleanRepeat()

# comparar anter y despues

newfuente = contar()

neworiginal = os.listdir(music_conv.SALIDA)


print "los cambios siguientes \n\n"
cont = 0
for i in fuente:

    if not newfuente.count(i):
        print i

        cont += 1

print i

print len(original)

print (len(original) - len(neworiginal))

