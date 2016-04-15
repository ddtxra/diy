import RPi.GPIO as GPIO
import time

sensor = 4

current_milli_time = lambda: int(round(time.time() * 1000))

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)


time.sleep(0.1)
state = GPIO.input(sensor)
print("%d,%s" % (current_milli_time(), state))
