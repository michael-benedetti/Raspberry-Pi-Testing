#!/usr/bin/python
import time, Lcd, datetime, statistics
import Lcd as lcd
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
lcd.lcd_init()

TRIG = 4
ECHO = 18
LED = 15

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

time.sleep(0.1)

try:
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
        dist = (stop - start) * 170
        
        lcd.lcd_string(str("%.2f" % round(dist,2)) + "m", lcd.LCD_LINE_1, 2)
        
        if dist < 1:
            GPIO.output(LED, 1)
            lcd.lcd_string("Obj w/in 1m", lcd.LCD_LINE_2,2)
        else:
            GPIO.output(LED, 0)
            lcd.lcd_string("", lcd.LCD_LINE_2,2)
        time.sleep(0.25)
except KeyboardInterrupt:
    GPIO.cleanup()

##i = 0
##while True:
##    if i == 0:
##    	try:
##       	    owm = pyowm.OWM('26f7a38fb8a7a213f614fcc2102fab23')
##       	    observ = owm.weather_at_id(7259396)
##       	    w = observ.get_weather()
##    	except:
##	    lcd.lcd_string('Error Loading',lcd.LCD_LINE_1,2)
##            lcd.lcd_string('Weather',lcd.LCD_LINE_2,2)
##	    time.sleep(3)
##	    pass
##    # Send some centred text
##    lcd.lcd_string(datetime.datetime.strftime(datetime.datetime.now(),'%m/%d/%Y'),lcd.LCD_LINE_1,2)
##    lcd.lcd_string(datetime.datetime.strftime(datetime.datetime.now(),'%H:%M'),lcd.LCD_LINE_2,2)
## 
##    time.sleep(3) # 3 second delay
## 
##    # Send some left justified text
##    lcd.lcd_string("Current Temp",lcd.LCD_LINE_1,2)
##    lcd.lcd_string(str(w.get_temperature('fahrenheit')['temp']) + " F",lcd.LCD_LINE_2,2)
## 
##    time.sleep(3) # 3 second delay
##    i +=1
##    if i >= 150:
##        i = 0
