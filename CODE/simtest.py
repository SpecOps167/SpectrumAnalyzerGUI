import matplotlib.pyplot as plt
import pyaudio
import wave
import numpy as np
from struct import unpack
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import *

fig = plt.figure()
ax1 = fig.add_subplot(111)

chunk = 4096

s = pyaudio.PyAudio()

sound = s.open(format = pyaudio.paInt16, channels = 2, rate = 44100, input = True, frames_per_buffer = chunk, input_device_index=2)

data = sound.read(chunk)

def animate(i):
    data = sound.read(chunk)
    data = unpack("%dh"%(len(data)/2),data)
    data = np.array(data,dtype='h')
    data = abs(np.fft.rfft(data))

    ax1.clear()
    ax1.plot(data)

ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()

sound.stop_stream()
sound.close()

a.terminate()
