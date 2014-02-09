#!/usr/bin/env python2.7

import os
import glob
import shutil
from PIL import Image

def Manipulate(img):

    im = Image.open(img)

    ult = im.resize((500,500))

    os.mkdir('modified/'+img)

    if os.path.exists('modified/'+img+'/'+'cover.jpg'):
        print "el archivo %s ya existe" %img
        ult.save('modified/'+img+'/'+'cover(1).jpg')
    else:
        ult.save('modified/'+img+'/'+'cover.jpg')

def main():

    os.chdir('/home/lokiteitor/Imagenes')

    if not  os.path.exists('cover/modified'):

        os.makedirs('cover/modified')

    if not os.path.exists('cover/original'):
        os.makedirs('cover/original')

    os.chdir('/home/lokiteitor/Imagenes/cover')

    candidate = glob.glob('*.jpg') + glob.glob('*.jpeg')

    for i in candidate:
        Manipulate(i)
        if os.path.exists('original/'+i):
            print "el archivo ya existe"
        else:
            shutil.move(i,'original/')


if __name__ == '__main__':
    main()