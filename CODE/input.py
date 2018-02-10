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
driver1 = DriverSerial(num = 650, type = LEDTYPE.WS2811, deviceID = 1)
driver2 = DriverSerial(num = 600, type = LEDTYPE.WS2811, deviceID = 2)
led = LEDMatrix([driver1, driver2], width=50, height=25, coordMap = None, rotation=MatrixRotation.ROTATE_180, masterBrightness=100, pixelSize=(1,1))

chunk = 4096

s = pyaudio.PyAudio()

sound = s.open(format = pyaudio.paInt16, channels = 2, rate = 44100, input = True, frames_per_buffer = chunk)

data = sound.read(chunk)
while True:
    data = sound.read(chunk)
    data = unpack("%dh"%(len(data)/2),data)
    data = np.array(data,dtype='h')
    data = abs(np.fft.rfft(data))
    data = np.floor(data/600000)
    y = 12
    for z in range(0,50):
        t=data[y]
        if t>12:
            led.fillRect(z,0,1,int(t),color=(255,0,0))
        elif t>9:
            led.fillRect(z,0,1,int(t),color=(255,255,0))
        elif t>6:
            led.fillRect(z,0,1,int(t),color=(0,255,0))
        else:
            led.fillRect(z,0,1,int(t),color=(0,0,255))
        
        y = y + 1

    led.update()
    led.all_off()

sound.stop_stream()

sound.close()
s.terminate()
