import time
import random
import bibliopixel
from bibliopixel.drivers.serial_driver import *
from bibliopixel.led import *

class pixel(object):
    def change(self, f):
        bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)
        self.driver = DriverSerial(num = 50, type = LEDTYPE.WS2811)
        self.led = LEDStrip(self.driver, False, 255, 1)
        self.led.set(32, (255, 255, 255))
        self.led.update()
        time.sleep(f)
        self.led.all_off()
        raw_input("sdaf")
        self.led.all_off()
        self.led.update()

p = pixel()
p.change(0.05)
