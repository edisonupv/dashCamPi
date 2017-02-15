# dashCamPi
dashCamPi is a project that allows to record video from 2 cameras while is storing the data coming from a GPS. This project is built with:
   - Raspberry Pi 3: Include a 2A power supply, microSD card of 16 GB, Raspbian Jessie 8.0 and Linux 4.4.38-v7+. 
   - USB webcam: Logitech c920.
   - Raspberry Pi Camera Module 1.3.
   - GPS-USB: Glonass U-blox7.

The Dash Cam Project produces three types of file:
   - A file .avi for the front camera.
   - A file .h264 for the rear camera.
   - A file .txt for the data logger of the GPS.

Each video is five minutes long and the data logger stores the route of the car for those five minutes. The name of the file is a string formed by the date and time when the files was created, e.g. we have these files: 
   - 13022017_1130FC.avi
   - 13022017_1130RC.h264
   - 13022017_1230DL.txt

Those files were created at 11:30 in 13 February 2017 therefore they have information from 11:30:00 until 11:34:59. Moreover each six hours those files are uploaded to Dropbox, so we can download it to any device with internet.

**BEFORE YOU START**

This project will need some folders. In the terminal run the following commands:

```
$ mkdir /home/pi/dashCam
$ mkdir /home/pi/dashCam/daschCamData
$ mkdir /home/pi/dashCam/daschCamFiles
```

Use crontab to run the scripts every 5 minutes. In the crontab add these lines: 

```
*/5 * * * * sh /home/pi/dashCam/dashCamFiles/dashCamFC.sh 
*/5 * * * * python /home/pi/dashCam/dashCamFiles/dashCamRC.py 
*/5 * * * * python /home/pi/dashCam/dashCamFiles/gpsDataLogger.py
```

Make sure the script are in the path /home/pi/dashCam/ dashCamFiles/


You can see my results in this [link](https://www.dropbox.com/sh/i0p91yv03mfpqq0/AAAnWxKzw22XX4Q1bG7G7yfva?dl=0).

Be free to make any change in the code and help me to built a better project!

PS: I apologize if you can't understand my english grammar. My English lessons are continuing! 

**Este texto estará en negritas**
