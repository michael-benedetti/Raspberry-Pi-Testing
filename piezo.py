import RPi.GPIO as GPIO 
import time, random



class buzzer():
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(19, GPIO.OUT)
        
    def play(self, numTimes, speed):
        for i in range(0,numTimes):
            p = GPIO.PWM(19, 50)
            c = 261
            d = 294
            e = 329
            f = 349
            g = 392
            a = 440
            b = 493
            C = 523
            r = 1
            GPIO.output(19, True)
            time.sleep(speed) ## Wait
            p.start(100)             # start the PWM on 100  percent duty cycle  
            p.ChangeDutyCycle(90)   # change the duty cycle to 90%
            x = [x for x in range(1000, 25000, 1000)]
            z=[]
            m=0
            for i in x:
                z.append(i + m)
                if m == 0:
                    m = 1500
                elif m == 1500:
                    m = 0.1
                elif m == 0.1:
                    m = -1500
                elif m == -1500:
                    m = 0
            for f in z:
                try:
                    p.ChangeFrequency(f)
                    time.sleep(0.1)
                except:
                    pass
##            for f in range(1, 4600, 10):
##                p.ChangeFrequency(f)
##                time.sleep(0.001)
##            for f in reversed(range(1,4600, 10)):
##                p.ChangeFrequency(f)
##                time.sleep(0.001)
##            p.ChangeFrequency(c)  # change the frequency to 261 Hz (floats also work)  
##            time.sleep(speed) ## Wait
##            p.ChangeFrequency(d)  # change the frequency to 294 Hz (floats also work)  
##            time.sleep(speed) ## Wait
##            p.ChangeFrequency(e)   
##            time.sleep(speed) ## Wait
##            p.ChangeFrequency(f)  
##            time.sleep(speed) ## Wait
##            p.ChangeFrequency(g)    
##            time.sleep(speed) ## Wait
##            p.ChangeFrequency(a)    
##            time.sleep(speed) ## Wait
##            p.ChangeFrequency(b)    
##            time.sleep(speed) ## Wait
##            p.ChangeFrequency(C)    
##            time.sleep(speed) ## Wait
##            p.ChangeFrequency(r)  
##            time.sleep(speed) ## Wait
            p.stop()                # stop the PWM output  
                
if __name__ == "__main__":
    iterations = 2
    speed = 0.5
    test = buzzer()
    test.play(int(iterations),float(speed))
    GPIO.cleanup()

