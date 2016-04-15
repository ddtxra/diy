import RPi.GPIO as GPIO
import time

sensor = 4

current_milli_time = lambda: int(round(time.time() * 1000))

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "1" if current_state else "0"
        print("%d,%s" % (current_milli_time(), new_state))
