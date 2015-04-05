#!/usr/bin/env python2.7

import xml.etree.ElementTree as ET

class Population(object):
    """docstring for population"""
    def __init__(self):
        super(Population, self).__init__()

        self.badfiles = []

        self.Animal = []
        self.Ship = []
        self.Build = []


    def setPath(self,path):
        print path

        self.path = path
        self.xml = ET.parse(path)

        self.root = self.xml.getroot()

    def getGraft(self):
        
        self.popu = self.root.findall('Unit')

    def iterPopu(self):

        for i in self.popu:
            try:
                child = i.find('PopulationCount')
                # revisar el buildlimit y los animales

                if child is not None:
                    child.text = str(1)

                Limit = i.find('BuildLimit')

                if Limit is not None:
                    Type = i.findall('UnitType')

                    for x in Type:

                        if x.text == 'AnimalPrey':
                            self.Animal.append(i);
                            Limit.text = str(1000)

                        elif x.text == 'Ship':
                            self.Ship.append(i)
                            Limit.text = str(int(Limit.text) * 2)

                        elif x.text == 'Building':
                            self.Build.append(i)

                            Limit.text = str(int(Limit.text) * 3)

            except AttributeError:
                self.badfiles.append(i.attrib['name'])

                child = None

            child = None

        self.xml.write(self.path)

    def clear(self):
        self.Animal = []
        self.Ship = []
        self.Build = []
        self.badfiles = []
        self.root = None
        self.xml = None
        self.path = None

def imprimirObjetivos():
    pass
    print 'los animales son:'
    for i in P.Animal:
        print '\t',i.attrib['name']

    print 'los barcos son:' 
    for i in P.Ship:
        print '\t',i.attrib['name']

    print 'los edificios son:'
    for i in P.Build:
        print '\t',i.attrib['name']

def main():
    pathy = '/home/lokiteitor/git/lab/protoy.xml'


    pathx = '/home/lokiteitor/git/lab/protox.xml'

    path = '/home/lokiteitor/git/lab/proto.xml'

    paths = [pathy,path,pathx]


    for i in paths:

        P.setPath(i)
        P.getGraft()
        P.iterPopu()

        imprimirObjetivos()

        P.clear()


P = Population()



if __name__ == '__main__':
    main()