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
import socket

class audio(object):
    def audioinfo(self, sound, chunk):
        data = sound.read(chunk)
        data = unpack("%dh"%(len(data)/2),data)
        data = np.array(data,dtype='h')
        data = abs(np.fft.rfft(data))
        data = data/100000
        return data

    def a(self):
        ch = 4096
        s = pyaudio.PyAudio()
        snd = s.open(format = pyaudio.paInt16, channels = 2, rate = 44100, input = True, frames_per_buffer = ch, input_device_index=2)
        return self.audioinfo(snd, ch)

class output(object):
    def calculations(self, data):
        try:
            t = int(math.log(data, 1.4))
            return t
        except ValueError:
            t = 0
            return t

    def lights(self, data):
        y = 0
        for z in range(0,50):

            gSum=0
            for y in range(y,y+4):
                gSum+=data[y]
            dData=gSum/4

            try:
                t = dData * (math.log(z, 1.04)/60)
            except ValueError:
                t = 0

            print z, " ", t
            
            msg = str(z) + " " + str(t) + "\n"

class main(object):
    def startlights(self):
        audiooutput = audio()
        printoutput = output()
        while True:
            printoutput.lights(audiooutput.a())

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
