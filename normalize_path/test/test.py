#!/usr/bin/env python2.7

import os
import sys
import unittest

import normapath



# modificamos el path para poder acceder mejor a los modulos
this_dir = os.path.dirname(os.path.abspath(__file__))
trunk_dir = os.path.split(this_dir)[0]

# /home/lokiteitor/git/swiss-manager
sys.path.insert(0,trunk_dir)


class Context(unittest.TestCase):
    """crear el contexto necesario"""
    def __init__(self, arg):
        super(Context, self).__init__()



class BraseroTestClass(unittest.TestCase):
    """pruebas definidas para el frontend de brasero"""
    def __init__(self, braserofile):
        super(BraseroTestClass, self).__init__()
        self.braserofile = braserofile
        
        



if __name__ == '__main__':
            main(sys.argv[1:])