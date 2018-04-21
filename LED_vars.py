#! /usr/bin/python3.5
import RPi.GPIO as GPIO
import time

Led_1 = 18
Led_2 = 24
Led_3 = 21

lights = {
    'blue': Led_1,
    'green': Led_2,
    'red': Led_3
}

def setup_LED(*args):
    GPIO.setmode(GPIO.BCM)
    for arg in args:
        GPIO.setup(arg, GPIO.OUT)
        GPIO.output(arg, False)

def on_LED(el):
    GPIO.output(el, True)

def off_LED():
    GPIO.cleanup()

def blink(el, time_delay=0.2):
    GPIO.output(el, True)
    time.sleep(time_delay)
    GPIO.output(el, False)
    time.sleep(time_delay)
