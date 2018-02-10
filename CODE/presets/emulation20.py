import time
import random
import bibliopixel
from bibliopixel.drivers.visualizer import *
from bibliopixel.drivers.serial_driver import *
from bibliopixel.led import *
import pyaudio
import wave
import numpy as np
from struct import unpack
from math import *
import bibliopixel.image as image
import sys
from decimal import *

class main(object):
    visw = 40
    vish = 20
    idevice = 2
    chunk = 4096
    yshift = 700
    bandc = 1.00185
    logc = 1.35
    powshift = 100
    wscale = 900000
    freqrange = 83

    def initialize(self):
        self.visw = int(sys.argv[2])
        self.vish = int(sys.argv[3])
        self.idevice = int(sys.argv[4])
        self.chunk = int(sys.argv[5])
        self.yshift = int(sys.argv[6])
        self.bandc = Decimal(sys.argv[7])
        self.logc = Decimal(sys.argv[8])
        self.powshift = int(sys.argv[9])
        self.wscale = int(sys.argv[10])
        self.freqrange = int(sys.argv[11])
        
        self.startemu(sys.argv[1])

    def startemu(self, option):
        i = initled()
        o = output()

        if option == "emulated":
            i.ledemu(self.visw, self.vish)
        elif option == "double":
            i.leddouble(self.visw, self.vish)

        o.mainloop(self.idevice, self.yshift, self.visw, self.bandc, self.logc, self.powshift, self.wscale, self.freqrange, self.chunk, i.led)

class initled(object):
    def ledemu(self, visw, vish):
        bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)
        driver = DriverVisualizer(width=visw, height=vish, pixelSize=10)
        self.led = LEDMatrix(driver, vert_flip=True)
        texture1 = image.loadImage(self.led, "c:\\users\\ztech\\pictures\\texture2.jpg")
        self.led.setTexture(tex=texture1)

    def ledsingle(self, visw, vish):
        coords1 = mapGen(10,5)
        bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)
        driver1 = DriverSerial(num = 50, type = LEDTYPE.WS2811, deviceID = 1)
        self.led = LEDMatrix(driver1, width=10, height=5, coordMap = coords1, rotation=MatrixRotation.ROTATE_180, masterBrightness=250, pixelSize=(1,1))

    def leddouble(self, visw, vish):
        m = MultiMapBuilder()
        m.addRow(mapGen(20,20,rotation=MatrixRotation.ROTATE_270),mapGen(20,20,rotation=MatrixRotation.ROTATE_270,vert_flip=True))
        bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)
        driver1 = DriverSerial(num = 400, type = LEDTYPE.WS2811, deviceID = 1)
        driver2 = DriverSerial(num = 400, type = LEDTYPE.WS2811, deviceID = 2)
        self.led = LEDMatrix([driver2,driver1], width=visw, height=vish, coordMap = m.map, rotation=MatrixRotation.ROTATE_0, masterBrightness=100, pixelSize=(1,1))
        texture1 = image.loadImage(self.led, "c:\\users\\ztech\\pictures\\texture2.jpg")
        self.led.setTexture(tex=texture1)

class output(object):
    def mainloop(self, idevice, yshift, visw, bandc, logc, powshift, wscale, freqrange, chunk, led):
        s = pyaudio.PyAudio()
        sound = s.open(format = pyaudio.paInt16, channels = 2, rate = 44100, input = True, frames_per_buffer = chunk, input_device_index=idevice)
        data = sound.read(chunk)
        while True:
            f = open("C:\\Users\\ZTech\\Documents\\CODE\\presets\\volume.txt", "r")
            vol = int(f.readline())
            f.close()
            data = sound.read(chunk)
            data = unpack("%dh"%(len(data)/2),data)
            data = np.array(data,dtype='h')
            data = abs(np.fft.rfft(data))
            data = data/vol
            y = yshift
            for z in range(0,visw):
                try:
                    t = int(log(data[int(pow(bandc,y))], logc)+(math.pow(y+powshift,2)/wscale))
                except ValueError:
                    t = 1

                led.fillRect(z,0,1,t)
                y=y+freqrange

            led.update()
            led.all_off()

m = main()
m.initialize()
