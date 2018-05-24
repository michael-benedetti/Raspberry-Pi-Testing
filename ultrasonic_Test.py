import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 7
ECHO = 12
LED = 10

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

time.sleep(0.1)

try:
    print("starting measurement")
    while True:
        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG, 0)

        while GPIO.input(ECHO) == 0:
            pass
        start = time.time()

        while GPIO.input(ECHO) == 1:
            pass
        stop = time.time()

        print((stop - start) * 170)

        if ((stop - start) * 170) < 1:
            GPIO.output(LED, 1)
        else:
            GPIO.output(LED, 0)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Done")
