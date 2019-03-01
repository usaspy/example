import RPi.GPIO as GPIO
import time

channel=40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel,GPIO.OUT)
GPIO.output(channel,False)
time.sleep(5)
print(GPIO.input(channel))
GPIO.cleanup()
