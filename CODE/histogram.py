import pyaudio
import wave
import numpy as np
from struct import unpack
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

chunk = 4096

f = wave.open(r"C:\Users\LiamJ\Desktop\other.wav","rb")

a = pyaudio.PyAudio()

sound = a.open(format = a.get_format_from_width(f.getsampwidth()),channels = f.getnchannels(), rate = f.getframerate(), output = True)

data = f.readframes(chunk)

def animate(i):
    data = f.readframes(chunk)
    sound.write(data)
    data = unpack("%dh"%(len(data)/2),data)
    data = np.array(data,dtype='h')
    freq = np.fft.fftshift(np.fft.rfft(data,chunk,norm="ortho").real).real
    norm = remap(freq)
    hist,_ = np.histogram(norm,bins=25, density=True)
    
    ax1.clear()
    ax1.hist(norm,bins=25,normed=True)


def remap(x):
    oldMin = x.min()
    oldMax = x.max()
    low = -25
    high = 25
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

    
ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()
sound.stop_stream()
sound.close()

a.terminate()
