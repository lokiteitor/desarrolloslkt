#!/usr/bin/env python2.7


# el objetivo es permitir conocer de una lista de paquetes 
# cual es el que tiene la version mas actual basandonos en el nombre
# o cadena de versionado

import os , re

DIR = '/run/media/lokiteitor/lkt/pkg/'

lista = os.listdir(DIR)

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

    for x in lista:

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



for x in matchlist.keys():

    cont = 0

    pat = re.compile('\d')

    sub1 = pat.sub('',i)

    for y in matchlist.keys():

        sub2 = pat.sub('',y)

        if sub2 == sub1:

            cont += 1

    if cont > 1 and cont != 3:
        print cont


print matchlist
