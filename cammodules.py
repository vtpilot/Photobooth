#!/usr/bin/python
import time
import subprocess
import datetime

def ConfigureCamera(option):
	print "Configurion option " + option
	try:
		subprocess.call("gphoto2 --set-config " + option, shell=True)
	except Exception as e: 
		print(e)	

def TakePicture(OutputDir):
	print "Taking picture!"
	try:
		subprocess.call("gphoto2 --capture-image-and-download --keep --filename " + OutputDir + "%f.%C", shell=True)
	except Exception as e: 
		print(e)


def  TakeHDRPicture(HDR):
	now = datetime.datetime.now()
	print now

	print "gphoto - configure camera for underexposed picture"
	print "gphoto - take underexposed picture"
	#output = subprocess.call("gphoto2 --capture-image-and-download --keep --filename  " + OutputDir + now.strftime("%H_%M_%S") + ".%C", shell=True)
	#print(output)
	
	print "gphoto - configure camera for normal exposure"
	print "gphoto - take normal picture"
	#output = subprocess.call("gphoto2 --capture-image-and-download --keep --filename  " + OutputDir + now.strftime("%H_%M_%S") + ".%C", shell=True)
	#print(output)
	
	print "gphoto - configure camera for overexposed picture"
	print "gphoto - take overexposed picture"
	#output = subprocess.call("gphoto2 --capture-image-and-download --keep --filename  " + OutputDir + now.strftime("%H_%M_%S") + ".%C", shell=True)
	#print(output)

#def ActuateMotor():
#	print "Moving carrier"
		

