from time import sleep
import RPi.GPIO as GPIO
from super_mario import notes, melody, tempo

buzzTime = 0.5
buzzDelay = 2
buzzerPin = 4

def setup_buzz():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzerPin, GPIO.IN)
    GPIO.setup(buzzerPin, GPIO.OUT)

def buzz(frequency, length):
	if(frequency==0):
		sleep(length)
		return
	period = 1.0 / frequency
	delayValue = period / 2
	numCycles = int(length * frequency)

	for i in range(numCycles):
		GPIO.output(buzzerPin, True)
		sleep(delayValue)
		GPIO.output(buzzerPin, False)
		sleep(delayValue)

def play(melody,tempo,pause,pace=0.800):
	for i in range(0, len(melody)):
		noteDuration = pace/tempo[i]
		buzz(melody[i],noteDuration)

		pauseBetweenNotes = noteDuration * pause
		sleep(pauseBetweenNotes)


def beep():
    setup_buzz()
    GPIO.output(buzzerPin, True)
    sleep(buzzTime)
    GPIO.output(buzzerPin, False)
    sleep(buzzDelay)
    GPIO.cleanup()
    return 'Beep Bop Beep Beep'

def mariosong():
    setup_buzz()
    play(melody, tempo, 1.3, 0.800)
    sleep(2)
    return 'Mamma mia!'
