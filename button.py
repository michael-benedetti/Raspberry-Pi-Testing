import RPi.GPIO as GPIO
import time, traceback
print('Running button program')
GPIO.setmode(GPIO.BOARD)

b = 11
l = 13

GPIO.setup(b, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(l, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
p = GPIO.PWM(15, 50)
GPIO.output(l, 0)
GPIO.output(15, 1)
def buttonHandler(c):
    if GPIO.input(c):
        GPIO.output(l, 0)
    else:
        GPIO.output(l, 1)

def mainloop():
    while True:
        f = 1
        x = 10
        p.stop()
        GPIO.output(l, 0)
        while not GPIO.input(11):
            GPIO.output(l, 1)
            p.start(100)
            p.ChangeDutyCycle(90)
            p.ChangeFrequency(f)
            f += x
            if f > 15590:
                x = -10
            if f < 10:
                x = 10
            time.sleep(0.001)
try:
    buttonHandler(11)
    mainloop()
except KeyboardInterrupt:
    GPIO.cleanup()
    print('Keyboard Interrupt')
except:
    GPIO.cleanup()
    tb = traceback.print_exc()
    print(tb)
