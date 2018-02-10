import pyaudio
import wave
import numpy as np
import math
from struct import unpack
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random
import bibliopixel
from bibliopixel.drivers.serial_driver import *
from bibliopixel.led import *



fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

chunk = 4096

f = wave.open(r"C:\Users\LiamJ\Desktop\other.wav","rb")

a = pyaudio.PyAudio()

sound = a.open(format = a.get_format_from_width(f.getsampwidth()),channels = f.getnchannels(), rate = f.getframerate(), output = True)

data = f.readframes(chunk)
class pixel(object):
   
    def __init__(self):
        self.col  = 50
        self.row = 3
        self.size = self.row*self.col
        bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)
        self.driver = DriverSerial(num = self.size, type = LEDTYPE.WS2811)
        self.led = LEDStrip(self.driver, False, 255, 1)
        self.led.all_off()
        self.led.update()
    def column(self,col, hieght):
        for i in xrange(hieght):
                if i%2 == 0:
                    num = col + i*self.col
                else:
                    num = col + i*self.col  +(self.col - col) -col-1
                self.led.set(num, (255,255,255))
    def lightup(self, data):
        count = 0
        for i in data:
            self.column(count,i)
            count = count+1
        self.led.update()
        
      

def animate(i):
    data = f.readframes(chunk)
    sound.write(data)
    data = unpack("%dh"%(len(data)/2),data)
    data = np.array(data,dtype='h')
    freq = np.fft.fftshift(np.fft.rfft(data,chunk,norm="ortho").real).real
    norm = remap(freq,-25,25)
    hist,_ = np.histogram(norm,bins=25, density=True)
    light = [int(round(i)) for i in remap(hist,0,12)]
    p.lightup(light)
    ax1.clear()
    ax1.hist(norm,bins=25,normed=True)



def remap(x,minVal,maxVal):
    oldMin = x.min()
    oldMax = x.max()
    low = minVal
    high = maxVal
    newRange = high-low
    oldRange = oldMax -oldMin
    norm = []
    for i in x:
        if oldRange == 0:
            newVal = 0
        else:
            newVal =(((i - oldMin) * newRange) / oldRange) + low
        norm.append(newVal)
    return norm

p = pixel()    
ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()

sound.stop_stream()
sound.close()

a.terminate()
