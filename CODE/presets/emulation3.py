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
driver = DriverVisualizer(width=50, height=25, pixelSize=10)
led = LEDMatrix(driver, vert_flip=True)
chunk = 1024

s = pyaudio.PyAudio()

sound = s.open(format = pyaudio.paInt16, channels = 2, rate = 44100, input = True, frames_per_buffer = chunk, input_device_index=2)

data = sound.read(chunk)
while True:
    data = sound.read(chunk)
    data = unpack("%dh"%(len(data)/2),data)
    data = np.array(data,dtype='h')
    data = abs(np.fft.rfft(data))
    data = data/20000
    y = 1
    for z in range(0,50):
        try:
            t = int(log(data[y], 1.35)+(math.pow(y+200,2)/35000))
        except ValueError:
            t = 1

        led.fillRect(z,0,1,t,color=(255,255,255))
        y=y+9

    led.update()
    led.all_off()

sound.stop_stream()

sound.close()
s.terminate()
