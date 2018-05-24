import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BOARD)

b = 11
g = 13
r = 15

GPIO.setup(r, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)

def white():
    GPIO.output(r, 0)
    GPIO.output(g, 0)
    GPIO.output(b, 0)

def red():
    GPIO.output(r, 0)
    GPIO.output(g, 1)
    GPIO.output(b, 1)

def green():
    GPIO.output(r, 1)
    GPIO.output(g, 0)
    GPIO.output(b, 1)

def blue():
    GPIO.output(r, 1)
    GPIO.output(g, 1)
    GPIO.output(b, 0)

def off():
    GPIO.output(r, 1)
    GPIO.output(g, 1)
    GPIO.output(b, 1)

option = sys.argv[1]

if option == "off": off()
elif option == "white": white()
elif option == "red": red()
elif option == "green": green()
elif option == "blue": blue()
else: print option

