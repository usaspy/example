import RPi.GPIO as GPIO
import time

while True:
	channel = 29
	data = []
	j = 0
 	
	GPIO.setmode(GPIO.BOARD)	
	time.sleep(1)
	
	GPIO.setup(channel,GPIO.OUT,initial=GPIO.LOW)
	time.sleep(0.02)
	GPIO.setup(channel,GPIO.IN,pull_up_down=GPIO.PUD_UP)

	while GPIO.input(channel) == GPIO.LOW:
		continue
	while GPIO.input(channel) == GPIO.HIGH:
		continue
	
	while j < 40:
		k = 0
		while GPIO.input(channel) == GPIO.LOW:
			continue
		while GPIO.input(channel) == GPIO.HIGH:
			k += 1
			if k > 100:
				break
			if k < 8:
				data.append(0)
			else:
				data.append(1)
			j+=1
	h_1=data[0:8]
	h_2=data[8:16]
	t_1=data[16:24]
	t_2=data[24:32]
	checksum=data[32:40]

	
	print(h_1)
	print(h_2)
	print(t_1)
	print(t_2)	
	print(checksum)

	h1=0
	h2=0
	t1=0
	t2=0
	for i in range(8):
		h1 +=h_1[i]*2**(7-i)
		h2 +=h_2[i]*2**(7-i)
	        t1 +=t_1[i]*2**(7-i)
		t2 +=t_2[i]*2**(7-i)	
	print("temperature:",t1,"humidity:",h1)
	GPIO.cleanup()
