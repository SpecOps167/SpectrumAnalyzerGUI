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
driver = DriverSerial(num = 650, type = LEDTYPE.WS2811)
led = LEDMatrix(driver, width=50, height=13, rotation=MatrixRotation.ROTATE_180, masterBrightness=100, pixelSize=(1,1))
wr = wave.open(r"C:\Users\ztech\documents\code\other.wav","rb")

s = pyaudio.PyAudio()

sound = s.open(format = s.get_format_from_width(wr.getsampwidth()),channels = wr.getnchannels(), rate = wr.getframerate(), output = True)

chunk=1024
data = wr.readframes(chunk)
while True:
    data = wr.readframes(chunk)
    sound.write(data)
    data = unpack("%dh"%(len(data)/2),data)
    data = np.array(data,dtype='h')
    data = abs(np.fft.rfft(data))
    data = np.floor(data/800000)
    y = 0
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
