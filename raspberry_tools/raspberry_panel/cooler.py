#!/usr/bin/env python2.7
import time
from subprocess import Popen,PIPE

import RPi.GPIO as GPIO

COOLER = 17
# Al utiliza la numeracion broadcom
# como referencia el pin fisico 11 es el 17 BCM

GPIO.setmode(GPIO.BCM)
GPIO.setup(COOLER,GPIO.OUT)


def readTemp():
    
    Prcss = Popen(["vcgencmd","measure_temp"],stdout=PIPE)
    rest = Prcss.stdout.read()
    
    temp = rest.split("=")[1].split("'")[0]

    return float(temp)

def setCooler(estate=False):
    
    if estate==True:
        GPIO.output(COOLER,True)
    else:
        GPIO.output(COOLER,False)
    return 


def main():
    # guardar el estado hasta que se alcanze una temperatura
    # por debajo de 35 C
    blk = False
    # Esperamos 3 segundos
    while True:
        if readTemp() >= 40.0 and blk==False:
            setCooler(True)
            blk = True
        
        elif readTemp() >= 35.0 and blk == True:
            setCooler(True)
        elif readTemp() < 35.0 and blk == True:
            setCooler(False)
            blk = False
        else:
            setCooler(False)
            blk = False

        print "Temp=" + str(readTemp())
        time.sleep(3)

main()
GPIO.cleanup()

