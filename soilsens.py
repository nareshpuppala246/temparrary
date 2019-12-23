import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup(2,gp.IN)
gp.setup(3,gp.OUT)

while True:
    x=gp.input(2)
    print(x)
    if(x==True):
        gp.output(3,True)
    if(x==False):
        gp.output(3,False)

    
    