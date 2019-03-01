import RPi.GPIO as GPIO
import time

channel=32

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def fire(p):
	print("fire is occur",p)


GPIO.add_event_detect(channel,GPIO.FALLING,callback=fire)

while True:
	print("no fire")
	time.sleep(0.5)


