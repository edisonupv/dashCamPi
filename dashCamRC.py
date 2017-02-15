import os
import sys
import threading
import time
from time import sleep
from picamera import PiCamera

#Directory where video will be storaged
directory = "/home/pi/dashCam/dashCamData/"

#Date and time
date = time.strftime("%d%m%Y_%H%M")

#Name video of Rear camera
filenameRC = directory + date + "RC" + ".h264"

#Initialization Pi camera
camera = PiCamera()

camera.resolution = (640, 480)        #Resolution
camera.framerate = 30                 #Framerate
camera.start_recording(filenameRC)    #Start record video
camera.wait_recording(290)            #280 seconds 
camera.stop_recording()               #After that stop the video
