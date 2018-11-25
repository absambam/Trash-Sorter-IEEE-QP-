from picamera import PiCamera
from time import sleep, gmtime, strftime

camera = PiCamera()

def take_picture():
    output = strftime("/home/pi/ts36/images/image-%d-%m_%H:%M.jpg", gmtime())
    
    camera.start_preview()
    sleep(3)
    camera.capture(output)
    camera.stop_preview()

take_picture()
