import RPi.GPIO as GPIO
from datetime import datetime
import time, traceback, threading
import Lcd as lcd
print('Running button program')
GPIO.setmode(GPIO.BCM)

b = 26

GPIO.setup(b, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
lcd.lcd_init()

class buzzer():
    def __init__(self, pin, freq):
        GPIO.setup(22, GPIO.OUT)
        GPIO.output(22, 1)
        self.p = GPIO.PWM(pin, freq) #15, 50
        self.p.start(100)
        
    def encode(self):
        self.p.ChangeDutyCycle(90)
        self.p.ChangeFrequency(7000)

    def accept(self):
        self.p.ChangeDutyCycle(90)
        self.p.ChangeFrequency(2000)

    def deny(self):
        self.p.ChangeDutyCycle(90)
        self.p.ChangeFrequency(300)
        
    def stop(self):
        self.p.ChangeDutyCycle(100)

    def kill(self):
        self.p.stop()

class charPart():
    def __init__(self):
        self.timeStarted = datetime.now()

class morseChar():
    def __init__(self):
        self.parts = []
        self.timeCreated = datetime.now()
        
    def addPart(self, part):
        if len(self.parts) < 5:
            self.parts.append(part)
        else:
            print('Too many parts')

class morseString():
    def __init__(self):
        self.chars = []
        self.mDict = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.',
                      'f':'.-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---',
                      'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---',
                      'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                      'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--',
                      'z':'--.'}

    def addChar(self, char):
        self.chars.append(char)
        
    def validateString(self, char):
        ret = False
        for c in self.mDict:
            if self.mDict[c] == char:
                ret = c
        return ret


buz = buzzer(22, 50)

def threadTimer():
    global stopChar
    stopChar = True
def mainloop():
    global stopChar
    while True:
        try:
            mChar
        except NameError:
            mChar = None
            threadStart = None
            stopChar = False
        if mChar:
            if threadStart:
                threading.Timer(2.2, threadTimer).start()
                threadStart = False
            if stopChar:
                try:
                    mString
                except NameError:
                    mString = morseString()
                morseLetter = ''.join(mChar.parts)
                plainLetter = mString.validateString(morseLetter)
                if plainLetter:
                    mString.addChar(plainLetter)
                    buz.accept()
                    time.sleep(0.2)
                    buz.stop()
                    lcd.lcd_string(''.join(mString.chars),lcd.LCD_LINE_1,2)
                else:
                    buz.deny()
                    time.sleep(0.2)
                    buz.stop()
                print(mString.chars)
                mChar = None
                stopChar = False
        mCharPart = None
        while GPIO.input(b):
            if not mChar:
                mChar = morseChar()
                threadStart = True
            if not mCharPart:
                mCharPart = charPart()
            buz.encode()
        if mCharPart:
            start = mCharPart.timeStarted
            stop = datetime.now()
            buz.stop()
            dur = stop-start
            print(dur.total_seconds())
            if .01 < dur.total_seconds() < .22:
                mChar.addPart('.')
            elif .22 <=dur.total_seconds() < 2:
                mChar.addPart('-')
            elif dur.total_seconds() >= 2:
                try:
                    del mString
                    time.sleep(0.5)
                    for i in range(3):
                        buz.deny()
                        time.sleep(0.1)
                        buz.stop()
                        time.sleep(0.1)
                    lcd.lcd_string('',lcd.LCD_LINE_1,2)
                    time.sleep(1)
                except:
                    pass
            del mCharPart

try:
    mainloop()
except KeyboardInterrupt:
    GPIO.cleanup()
except:
    GPIO.cleanup()
    tb = traceback.print_exc()
    print(tb)
