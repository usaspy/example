import RPi.GPIO as GPIO
import time

channel = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def active(p):
    print("alert! alert!",p)

GPIO.add_event_detect(channel,GPIO.RISING,callback=active)

try:
        while True:
            print("alive")
            time.sleep(0.5)
except KeyboardInterrupt as e:
    pass
finally:
    GPIO.cleanup()
