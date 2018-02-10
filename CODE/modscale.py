import time
import random
import bibliopixel
from bibliopixel.drivers.serial_driver import *
from bibliopixel.led import *
import pyaudio
import wave
import numpy as np
from struct import unpack
from math import *

bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)
driver1 = DriverSerial(num = 600, type = LEDTYPE.WS2811, deviceID = 2)
driver2 = DriverSerial(num = 650, type = LEDTYPE.WS2811, deviceID = 1)
led1 = LEDMatrix(driver1, width=50, height=12, coordMap = None, rotation=MatrixRotation.ROTATE_180, masterBrightness=100, pixelSize=(1,1))
led2 = LEDMatrix(driver2, width=50, height=13, coordMap = None, rotation=MatrixRotation.ROTATE_180, masterBrightness=100, pixelSize=(1,1))

class audio(object):
    chunk = 4096
    s = pyaudio.PyAudio()
    sound = s.open(format = pyaudio.paInt16, channels = 2, rate = 44100, input = True, frames_per_buffer = chunk, input_device_index=2)
    
    def audioinfo(self):
        data = self.sound.read(self.chunk)
        data = unpack("%dh"%(len(data)/2),data)
        data = np.array(data,dtype='h')
        data = abs(np.fft.rfft(data))
        data = data/100000
        return data

class output(object):
    def calculations(self, data, xax):
        try:
            t = int(log(data, 1.35) * log10(xax+10))
            return t
        except ValueError:
            t = 0
            return t

    def average(self, yax, dat):
        avg = 0
        for yax in range(yax, yax+4):
            avg = avg + dat[yax]
        return avg/4

    def lights(self, data):
        y = 0
        for z in range(0,50):

            t = self.calculations(self.average(y, data), z)
            
            if t>23:
                led1.fillRect(z,0,1,t,color=(255,0,0))
                led2.fillRect(z,0,1,t-11,color=(255,0,0))
            elif t>21:
                led1.fillRect(z,0,1,t,color=(255,255,0))
                led2.fillRect(z,0,1,t-11,color=(255,255,0))
            elif t>15:
                led1.fillRect(z,0,1,t,color=(0,255,0))
                led2.fillRect(z,0,1,t-11,color=(0,255,0))
            elif t>12:
                led1.fillRect(z,0,1,t,color=(0,0,255))
                led2.fillRect(z,0,1,t-11,color=(0,0,255))
            else:
                led1.fillRect(z,0,1,t,color=(0,0,255))
                led2.fillRect(z,0,1,t-11,color=(0,0,0))

            y = y + 4

        led1.update()
        led2.update()
        led1.all_off()
        led2.all_off()

class main(object):
    def startlights(self):
        audiooutput = audio()
        printoutput = output()
        while True:
            printoutput.lights(audiooutput.audioinfo())

    def config(self):
        raw_input("""
 _____   _____   __   __   __   _____
|  _  | |  ___| |   \|  | |  | |  ___|
| |_| | | |___  |  |    | |  | | |___
|  ___| |  ___| |  |\   | |  | |___  |
| |     | |___  |  | |  | |  |  ___| |
|_|     |_____| |__| |__| |__| |_____|
""")
        print("starting server")
        self.startlights()

run = main()
run.config()
