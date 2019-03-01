import RPi.GPIO as GPIO
import atexit
import time

atexit.register(GPIO.cleanup)

GPIO.setmode(GPIO.BOARD)
used_pin1=40
used_pin2=38

GPIO.setup(used_pin1,GPIO.OUT,initial=False)
p = GPIO.PWM(used_pin1,50)
p.start(12.5)

GPIO.setup(used_pin2,GPIO.OUT,initial=False)
p2 = GPIO.PWM(used_pin2,50)
p2.start(12.5)

time.sleep(2)

for i in range(0,360,20):     
     p.ChangeDutyCycle(12.5-10*i/360)
     p2.ChangeDutyCycle(12.5-10*i/360) 
     time.sleep(0.02)


