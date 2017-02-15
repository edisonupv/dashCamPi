#!/bin/bash

#Get time and data
date=$(date +"%d%m%Y_%H%M")

#Video output .avi and FC for Front Camera
filenameFC='FC.avi'

#Here we use avconv to record teh video
#-t means five minutes long of video
#-r is framerate
#-s is the resolution
#-i is the input ==> USB CAMERA
#-f is the Codec
#-y is the directory and name of the file
avconv -t 290 -f video4linux2 -s 640x480 -i /dev/video0 -y /home/pi/dashCam/dashCamData/$date$filenameFC
