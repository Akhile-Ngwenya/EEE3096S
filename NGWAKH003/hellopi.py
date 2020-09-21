
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)



GPIO.setup(12, GPIO.OUT)
i = 1000000

while (i>0):
	GPIO.output(12, GPIO.HIGH)
	i=i-1

GPIO.cleanup()

