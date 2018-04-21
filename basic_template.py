#! /usr/bin/python3.5

import time
import RPi.GPIO as GPIO

Led_1 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(Led_1, GPIO.OUT)


def blink(el, time_delay=0.1):
	GPIO.output(el, True)
	time.sleep(time_delay)
	GPIO.output(el, False)
	time.sleep(time_delay)

Count = 0
try:
	while Count < 25:
		Count = Count + 1
		blink(Led_1)
		print(Count)

except KeyboardInterrupt:
	print("\n %s" % Count)

except:
	print('Other error or exception occured!') 

finally:
	GPIO.cleanup()
