import time
import random
import bibliopixel
from bibliopixel.drivers.visualizer import *
from bibliopixel.led import *
import pyaudio
import wave
import numpy as np
from struct import unpack
from math import *

bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)
driver = DriverVisualizer(width=40, height=20, pixelSize=10)
led = LEDMatrix(driver, vert_flip=True)
chunk = 1024

s = pyaudio.PyAudio()
sound = s.open(format = pyaudio.paInt16, channels = 2, rate = 44100, input = True, frames_per_buffer = chunk, input_device_index=2)
data = sound.read(chunk)

temp = [40]
for x in range(0,40):
    temp.append(0)

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
    for z in range(0,40):
        try:
            t = int(log(data[int(pow(1.006,y))], 1.35)+(math.pow(y+100,2)/90000))
        except ValueError:
            t = 1

        if t > temp[z]:
            temp[z] = t

        led.fillRect(z,0,1,int(temp[z]),color=(255,255,255))
        y=y+25

        if temp[z] >= 1:
            factor = 1.5
            temp[z] = temp[z] - factor

    led.update()
    led.all_off()

sound.stop_stream()

sound.close()
s.terminate()
