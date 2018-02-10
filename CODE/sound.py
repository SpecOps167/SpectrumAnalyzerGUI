import pyaudio
import wave
import numpy
from struct import unpack

chunk = 1024

f = wave.open(r"C:\Users\LiamJ\Desktop\cb3k.wav","rb")

a = pyaudio.PyAudio()

sound = a.open(format = a.get_format_from_width(f.getsampwidth()),channels = f.getnchannels(), rate = f.getframerate(), output = True)

data = f.readframes(chunk)

while data:
    sound.write(data)
    data = unpack("%dh"%(len(data)/2),data)
    data = numpy.array(data,dtype='h')
    calc = numpy.fft.rfft(data)
    calc = numpy.delete(calc,len(calc)-1)
    data = f.readframes(chunk)
    print(calc)

sound.stop_stream()
sound.close()

a.terminate()

