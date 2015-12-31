#!/usr/bin/python

import time
import subprocess
import datetime
import os.path
import shutil

def CheckFolder(directory):
	if not os.path.exists(directory):
		print "Creating directory " + directory
		os.makedirs(directory)

def CheckFile(file, srcfile):
	if not os.path.exists(file):
		print file + " does not exist"
		if os.path.exists(srcfile):
			print "Copying " + srcfile
		shutil.copy(srcfile, file)
		
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

def TakeMontage(OutputDir, shots, delay):
	print "Taking montage"
	now = datetime.datetime.now().strftime('%H_%M_%S')
	i=1
	while i<=shots:
		print "Taking shot " + str(i) + " of " + str(shots)
		try:
			subprocess.call("gphoto2 --capture-image-and-download --keep --filename " + OutputDir + now + "_" + str(i) + ".%C", shell=True)
		except Exception as e: 
			print(e)		
		time.sleep(delay)
		i = i + 1
		
	subprocess.call("montage " + OutputDir + now + "_*.jpg -tile 2x2 -geometry 1920x1280+10+10 " + OutputDir + "Montages/" + now + "_montage.jpg", shell=True)
	
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

def ActuateMotor():
	print "Moving carrier"
		

