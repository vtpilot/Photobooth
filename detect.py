import subprocess
import time

device = False

while True:
	gpout = subprocess.check_output("gphoto2 --auto-detect", shell=True)
	
	if "usb" in gpout:
		#logging.error(gpout)
		print "Camera found"#raise IOError("Not able to take photo as the command failed for photo ")	
		break
	else:
		print "Waiting for camera"
	time.sleep(1)
