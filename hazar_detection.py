
import smbus
import time
import smtplib
import RPi.GPIO  as GPIO
from Adafruit_IO import Client, Feed
ADAFRUIT_IO_KEY = 'f1cdd7ccdf66413e8c65fe02e4770bcc'
ADAFRUIT_IO_USERNAME = 'HAZAR_DETECT'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
LPG_OUTPUT = aio.feeds('lpg')#adafruit


bus = smbus.SMBus(1)
#check your PCF8591 address by type in 'sudo i2cdetect -y -1' in terminal.
def setup(Addr):
    global address
    address = Addr

def read(chn):
    try:
        if chn == 3:
            bus.write_byte(address,0x43)
        bus.read_byte(address)
    except Exception as e:
        print ("Address: %s" % address)
        print (e)
    return bus.read_byte(address)

def write(val):
    try:
        temp = val # move string value to temp
        temp = int(temp) # change string to integer
        # print temp to see on terminal else comment out
        bus.write_byte_data(address, 0x40, temp)
    except Exception as e:
        print ("Error: Device address: 0x%2X" % address)
        print (e)

if __name__ == "__main__":
    setup(0x48)
    while True:
        print ("LPG_GAS=",read(3))
        time.sleep(2)
        aio.send(LPG_OUTPUT.key, str(read(3)))
       