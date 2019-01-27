#-*- coding: UTF-8 -*-
#超声波测距

import RPi.GPIO as GPIO
import time

echo=33
trig=37

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(trig,GPIO.OUT,initial=GPIO.LOW)
	GPIO.setup(echo,GPIO.IN)

def distance():
	print("starting...")	
	GPIO.output(trig,GPIO.HIGH)
	time.sleep(0.0001)
	
	GPIO.output(trig,GPIO.LOW)

	while GPIO.input(echo) == GPIO.LOW:
		pass
	starttime = time.time()
	while GPIO.input(echo)==GPIO.HIGH:
		pass
	endtime = time.time()
	print("time:",endtime-starttime)
	print("distance:",340*(endtime-starttime)/2)

if __name__ == "__main__":
	try:
		init()
		while True:
			distance()
			time.sleep(2)
	except KeyboardInterrupt as e:
		pass
	finally:
		GPIO.cleanup()
