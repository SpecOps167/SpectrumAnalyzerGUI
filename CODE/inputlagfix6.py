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

coords2 = mapGen(50,13)
coords1 = mapGen(50,12)
bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)
driver1 = DriverSerial(num = 600, type = LEDTYPE.WS2811, deviceID = 1)
driver2 = DriverSerial(num = 650, type = LEDTYPE.WS2811, deviceID = 2)
led1 = LEDMatrix(driver1, width=50, height=12, coordMap = coords1, rotation=MatrixRotation.ROTATE_180, masterBrightness=250, pixelSize=(1,1))
led2 = LEDMatrix(driver2, width=50, height=13, coordMap = coords2, rotation=MatrixRotation.ROTATE_180, masterBrightness=250, pixelSize=(1,1))
texture1 = image.loadImage(led1, "c:\\users\\ztech\\pictures\\texture1.jpg", offset=(0,0))
texture2 = image.loadImage(led2, "c:\\users\\ztech\\pictures\\texture1.jpg", offset=(0,-12))
led1.setTexture(tex=texture1)
led2.setTexture(tex=texture2)

chunk = 2048

s = pyaudio.PyAudio()

sound = s.open(format = pyaudio.paInt16, channels = 2, rate = 44100, input = True, frames_per_buffer = chunk, input_device_index=2)

data = sound.read(chunk)
while True:
    data = sound.read(chunk)
    data = unpack("%dh"%(len(data)/2),data)
    data = np.array(data,dtype='h')
    data = abs(np.fft.rfft(data))
    data = data/100000
    y = 1
    for z in range(0,50):
        gSum=0
        for y in range(y,y+6):
            gSum+=data[y]
        dData=gSum/4
        try:
            t = int(log(dData, 1.25) * log(z+3, 9))
        except ValueError:
            t = 0

        if t>12:
            led1.fillRect(z,0,1,t,color=None)
            led2.fillRect(z,0,1,t-12,color=None)
        else:
            led1.fillRect(z,0,1,t,color=None)
            led2.fillRect(z,0,1,t-12,color=(0,0,0))

    led2.update()
    led2.all_off()
    led1.update()
    led1.all_off()

sound.stop_stream()

sound.close()
s.terminate()
