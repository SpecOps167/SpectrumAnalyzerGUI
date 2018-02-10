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
import bibliopixel.image as image

coords1 = mapGen(10,5)
bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)
driver1 = DriverSerial(num = 50, type = LEDTYPE.WS2811, deviceID = 1)
led1 = LEDMatrix(driver1, width=10, height=5, coordMap = coords1, rotation=MatrixRotation.ROTATE_180, masterBrightness=250, pixelSize=(1,1))
chunk = 1024

s = pyaudio.PyAudio()

sound = s.open(format = pyaudio.paInt16, channels = 2, rate = 44100, input = True, frames_per_buffer = chunk, input_device_index=1)

data = sound.read(chunk)
while True:
    f = open("volume.txt", "r")
    vol = int(f.readline())
    f.close()
    data = sound.read(chunk)
    data = unpack("%dh"%(len(data)/2),data)
    data = np.array(data,dtype='h')
    data = abs(np.fft.rfft(data))
    data = data/vol
    y = 1
    for z in range(0,10):
        try:
            t = int(log(data[int(pow(1.006,y))], 1.35)+(math.pow(y+100,2)/90000))
        except ValueError:
            t = 1

        led1.fillRect(z,0,1,t,color=(255,255,255))
        y=y+102

    led1.update()
    led1.all_off()

sound.stop_stream()

sound.close()
s.terminate()
