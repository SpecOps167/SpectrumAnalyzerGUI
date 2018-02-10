import time
import random
import bibliopixel
from bibliopixel.drivers.serial_driver import *
from bibliopixel.led import *

class pixel(object):
    def change(self, f):
        bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)
        self.driver = DriverSerial(num = f, type = LEDTYPE.WS2811)
        self.led = LEDStrip(self.driver, False, 255, 1)
        while True:
            for x in range(0, f):
                self.led.set(x, (255, 255, 255))
                print x
                self.led.update()
                time.sleep(0.1)
                self.led.all_off()
        print('done')

p = pixel()
p.change(50)
