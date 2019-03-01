try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("gpio error")
import time

print("ok",GPIO.VERSION)

GPIO.setmode(GPIO.BOARD)
sensor = 18 
sg90 = 40 
led=12
GPIO.setup(sensor,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led,GPIO.OUT,initial=False)
GPIO.setup(sg90,GPIO.OUT,initial=False)
p = GPIO.PWM(sg90,50)

p.start(12.5)

flg = 0
while True:
	if GPIO.input(sensor)==GPIO.LOW:
		print('-----------')
	        flg = not flg

		if flg:		
			p.ChangeDutyCycle(4.5)
		else:
			p.ChangeDutyCycle(12.5)
		GPIO.output(led,flg)
		time.sleep(0.7)


GPIO.cleanup()
