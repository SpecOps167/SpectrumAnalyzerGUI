from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
import pyaudio
import wave
import numpy as np
from struct import unpack
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

chunk = 4096

f = wave.open(r"C:\Users\LiamJ\Desktop\cb3k.wav","rb")

a = pyaudio.PyAudio()

sound = a.open(format = a.get_format_from_width(f.getsampwidth()),channels = f.getnchannels(), rate = f.getframerate(), output = True)

data = f.readframes(chunk)

def animate(i):
    data = f.readframes(chunk)
    sound.write(data)
    data = unpack("%dh"%(len(data)/2),data)
    data = np.array(data,dtype='h')
    A = fft(data, 2048) / (len(data)/2.0)
    freq = np.linspace(-0.5, 0.5, len(A))
    response = 20 * np.log10(np.abs(fftshift(A / abs(A).max())))
    ax1.clear()
    ax1.plot(freq,responce)

ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()

sound.stop_stream()
sound.close()

a.terminate()
