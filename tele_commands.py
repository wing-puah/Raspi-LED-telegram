#! /usr/bin/python3.5
import time
import LED_vars

Led_1 = LED_vars.Led_1
Led_2 = LED_vars.Led_2
Led_3 = LED_vars.Led_3

def greet(user):
    return("Howdy %s!" % user)

def on(el):
    LED_vars.setup_LED(el)
    LED_vars.on_LED(el)

def green():
    on(LED_vars.lights['green'])
    return 'Green light is on'

def blue():
    on(LED_vars.lights['blue'])
    return 'Blue light is on'

def red():
    on(LED_vars.lights['red'])
    return 'Red light is on'

def off():
	LED_vars.off_LED()
	return 'Lights are off'

def fizzbuzz():
    LED_vars.setup_LED(Led_1, Led_2, Led_3)
    Count = 0

    while Count < 25:
        Count = Count + 1
        if Count % 3 == 0 and Count % 5 == 0:
            LED_vars.blink(Led_1, time_delay=0.05)
            LED_vars.blink(Led_2, time_delay=0.05)
            LED_vars.blink(Led_3, time_delay=0.05)
        if Count % 3 == 0:
            LED_vars.blink(Led_1, time_delay=0.4)
        elif Count % 5 == 0:
            LED_vars.blink(Led_2, time_delay=0.6)
        else:
            LED_vars.blink(Led_3)

    return 'That was the Fizzbuzz test. Counting up to %s' % Count

def all():
    LED_vars.setup_LED(Led_1, Led_2, Led_3)
    LED_vars.on_LED(Led_1)
    LED_vars.on_LED(Led_2)
    LED_vars.on_LED(Led_3)
    return 'Lighting up all the lights!'

def exit():
    LED_vars.off_LED()
    return 'Okie, bye bye!'
