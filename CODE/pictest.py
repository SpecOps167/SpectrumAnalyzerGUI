import bibliopixel
from bibliopixel.drivers.serial_driver import *
from bibliopixel.led import *
import bibliopixel.image as image

coords1 = mapGen(50,13)
coords2 = mapGen(50,12)
bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)
driver1 = DriverSerial(num = 650, type = LEDTYPE.WS2811, deviceID = 1)
driver2 = DriverSerial(num = 600, type = LEDTYPE.WS2811, deviceID = 2)
led1 = LEDMatrix(driver1, width=50, height=13, coordMap = coords1, rotation=MatrixRotation.ROTATE_0, masterBrightness=100, pixelSize=(1,1))
led2 = LEDMatrix(driver2, width=50, height=12, coordMap = coords2, rotation=MatrixRotation.ROTATE_0, masterBrightness=100, pixelSize=(1,1))

image.showImage(led1, "c:\\users\\ztech\\pictures\\bill2.jpg", offset=(12,0))
image.showImage(led2, "c:\\users\\ztech\\pictures\\bill2.jpg", offset=(12,-12))
led1.update()
led2.update()
