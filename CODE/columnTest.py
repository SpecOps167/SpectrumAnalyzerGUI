import time
import random
import bibliopixel
from bibliopixel.drivers.serial_driver import *
from bibliopixel.led import *

class pixel(object):
   
    def __init__(self):
        self.col  = 50
        self.row = 3
        self.size = self.row*self.col
        bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)
        self.driver = DriverSerial(num = self.size, type = LEDTYPE.WS2811)
        self.led = LEDStrip(self.driver, False, 255, 1)
        self.led.all_off()
        self.led.update()
    def column(self,col, hieght):
        try:
            for i in xrange(hieght):
                if i%2 == 0:
                    num = col + i*self.col
                else:
                    print "hello"
                    num = col + i*self.col  +(self.col - col) -col-1
                self.led.set(num, (255,255,255))
            self.led.update()
        except KeyboardInterrupt:
            print "\ninterrupted"
            self.led.all_off()
            self.led.update()

            
    
            

p = pixel()
p.column(3,12)

