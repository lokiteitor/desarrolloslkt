#!/usr/bin/env python2.7

import os 
import sys
import shutil

def verify(path):
    for root, dirs, files in os.walk(path, topdown=False):

        if not os.path.exists('convertidos/'):
            os.mkdir('convertidos')

        for f in files:
            if os.path.splitext(f)[1] == '.html':
                convert = os.path.join(root,f)
                order = 'unoconv -vv -f txt ' + convert
                os.system(order)

                result = os.path.splitext(convert)[0]+'.txt'

                finaldir = 'convertidos/'+os.path.basename(os.path.dirname(result))


                if not os.path.exists(finaldir) and not os.path.isdir(finaldir):
                    os.mkdir(finaldir)

                shutil.move(result,finaldir)



def main(path):
    print path[0]
    if os.path.isdir(path[0]):
        verify(path[0])

if __name__ == '__main__':
    main(sys.argv[1:])