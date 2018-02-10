import pyaudio

a = pyaudio.PyAudio()
info = a.get_host_api_info_by_index(0)
devices = info.get('deviceCount')
device = a.get_device_info_by_host_api_device_index(0, 2)

print info
print "\n"
print devices
print "\n"
print device
