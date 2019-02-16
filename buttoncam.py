from time import gmtime, strftime
from gpiozero import Button
from signal import pause
from picamera import PiCamera
import upload

def take_picture():
    out = strftime("img-%d-%m-%H:%M:%S.jpg", gmtime())
    camera.capture("./imgs/"+out)
    upload.upload_blob(out)
    

camera = PiCamera()
take_pic = Button(2)

take_pic.when_pressed = take_picture

pause()
