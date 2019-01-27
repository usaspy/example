import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.IN)

while True:
	if GPIO.input(29) == GPIO.HIGH:
		print("someone is come in!!!")
	time.sleep(6)
	print("monitoring...")
GPIO.cleanup()
