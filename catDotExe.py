import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)


def setOut(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    
def setIn(pin)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN)

def pinEnable(pin):
    GPIO.output(pin, 1);

def pinDisable(pin):
    GPIO.output(pin, 0)
    
def pinTempEnable(pin, time):
    pinEnable(pin)
    sleep(time)
    pinDisable(pin)
    
def isEnabled(pin):
    return GPIO.input(pin) > 0
    
def pinTempDisable(pin, time):
    if (isEnabled(pin)):
        pinDisable(pin)
        sleep(time)
        pinEnable()
    else:
        sleep(time)
        
def setAllPinsOut():
    for i in range(40):
        try:
            setOut(i)
        except:
            print(i)
            
setAllPinsOut()
    
i = 0

while i == 0:
    GPIO.output(8, 1)
    sleep(1)
    GPIO.output(8, 0)
    sleep(1)
    i += 1

GPIO.cleanup()
