#!/usr/bin/env python2.7
import sys
import os
import shutil

def main(path):

    error = []

    lista = os.listdir(path)

    for i in lista:

        if os.path.splitext(i)[1] != '.mp3':
            lista.remove(i)
            error.append(i)

    for i in lista:
        print i

    print error


if __name__ == '__main__':
    main(sys.argv[1])


