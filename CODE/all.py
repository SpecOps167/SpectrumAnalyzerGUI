import time
import random
import bibliopixel
from bibliopixel.drivers.serial_driver import *
from bibliopixel.led import *
import pyaudio
import wave
import numpy as np
from struct import unpack
import math

bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)
driver1 = DriverSerial(num = 600, type = LEDTYPE.WS2811, deviceID = 1)
driver2 = DriverSerial(num = 650, type = LEDTYPE.WS2811, deviceID = 2)
led1 = LEDMatrix(driver1, width=50, height=12, coordMap = None, rotation=MatrixRotation.ROTATE_180, masterBrightness=100, pixelSize=(1,1))
led2 = LEDMatrix(driver2, width=50, height=13, coordMap = None, rotation=MatrixRotation.ROTATE_180, masterBrightness=100, pixelSize=(1,1))

led1.fillRect(0,0,50,12,color=(0,0,255))
led2.fillRect(0,0,50,13,color=(0,0,255))


led1.update()
led2.update()
raw_input("sdof")
led1.all_off()
led2.all_off()
led1.update()
led2.update()

