import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)
i = 0

while i == 0:
    GPIO.output(8, GPIO.HIGH)
