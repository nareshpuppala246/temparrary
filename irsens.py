import RPi.GPIO as g
import time
g.setmode(g.BCM)
g.setwarnings(False)
blue = 2
red = 3
green = 17
irb = 21
irg = 16
irr = 20
g.setup(blue , g.OUT)
g.setup(green , g.OUT)
g.setup(red , g.OUT)
g.setup(irb , g.IN)
g.setup(irg , g.IN)
g.setup(irr , g.IN)
while True:
    x = g.input(irb)
    y = g.input(irg)
    z = g.input(irr)
    print(x)
    print(y)
    print(z)
    if(x==True):
        g.output(blue, True)
        g.output(red,False)
        g.output(green,False)
    elif(y==True):
        g.output(green, True)
        g.output(blue,False)
        g.output(red,False)
    elif(z==True):
        g.output(red, True)
        g.output(blue,False)
        g.output(green,False)
    elif(x==True and y==True and z==True):
        g.output(red,True)
        g.output(blue,True)
        g.output(green,True)
    else:
        g.output(blue, False)
        g.output(red, False)
        g.output(green, False)
    

    
