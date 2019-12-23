import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
trig = 2
echo = 3
buz = 17
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(buz, GPIO.OUT)
while True:
    GPIO.output(trig,True)
    time.sleep(0.00001)     #Generatio of a pulse
    GPIO.output(trig,False)

    while GPIO.input(echo) == 0:
        start = time.time()      
    while GPIO.input(echo) == 1:
        stop = time.time() 
    duration = stop - start
    distance = (duration/2) * 34000
    distance=round(distance,2)
    print('Distance = :',distance,' cm.')
    if(distance>10):
        GPIO.output(buz, False)
    else:
        GPIO.output(buz, True)


