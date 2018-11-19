from picamera import PiCamera
from time import sleep, gmtime, strftime

camera = PiCamera()

camera.resolution = (800, 480)
camera.hflip = True
camera.start_preview(alpha=128)

output = strftime("/home/pi/ts-images/image-%d-%m %H:%M.jpg", gmtime())

def take_picture():
    camera.capture(output)
    camera.stop_preview()
