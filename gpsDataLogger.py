import gps
import time

print(time.strftime("%I:%M:%S"))
i = 0
#Get date and time
date = time.strftime("%d%m%Y_%H%M")

#Directory where the data logger will be stored
directory = "/home/pi/dashCam/dashCamData/"

#Name of the file which stores the data of GPS
filename = directory + date + 'DL' + '.txt'

#where 'a' is for add text the file
dataFile = open(filename, "a")
 
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

#Main Bucle
while i < 240:
    try:
    	report = session.next()
        if report['class'] == 'TPV':
	    if hasattr(report, 'lat') and hasattr (report, 'lon'):
	    	dataFile = open(filename, "a")
                #Add longitud and latitude to the file
            	dataFile.write("%s,%s\n" % (report.lat, report.lon))
            	dataFile.close()
        #Delay 1s
        time.sleep(1)
	i +=1
    except KeyError:
		pass
    except KeyboardInterrupt:
		quit()
    except StopIteration:
		session = None
		print "GPSD has terminated"
print(time.strftime("%I:%M:%S"))
