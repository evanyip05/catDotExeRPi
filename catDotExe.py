import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
i = 0

while i == 0:
    GPIO.output(8, 1)
    sleep(1)
    GPIO.output(8, 0)
    sleep(1)
    i += 1

GPIO.cleanup()
