#!/usr/bin/python

import RPi.GPIO as GPIO
import time
#import subprocess
import datetime
from cammodules import TakePicture
from cammodules import ConfigureCamera

SWITCH = 21
RED_LED = 19
GREEN_LED = 13
BLUE_LED = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)

now = datetime.datetime.now().strftime('%Y-%m-%d')
OutputDir = "/home/pi/Pictures/" + now + "/"

### Configure Camera
options=[ \
	"autopoweroff=0", \
	"capturetarget=1", \
	"focusmode=0", \
	"imageformat=6" \
	]

for option in options:
	ConfigureCamera(option) 

try:
	print("Starting Photobooth")
	
	while True:
		GPIO.output(GREEN_LED, True)
		GPIO.output(RED_LED, False)
		GPIO.output(BLUE_LED, False)
	
		switch_value = GPIO.input(SWITCH)
	
		if (switch_value == False):
			now = datetime.datetime.now()
		
			print("Button pushed at " + now.strftime("%H:%M:%S"))
			
			GPIO.output(GREEN_LED, False)
	
			print("POSE!")
			
			for i in range(3):
				GPIO.output(BLUE_LED, True)
				time.sleep(0.1)
				GPIO.output(BLUE_LED, False)
				time.sleep(0.1)
			GPIO.output(BLUE_LED, True)
	
			#print("SNAP!")

			TakePicture(OutputDir)

			#try:
				
				#output = subprocess.call("gphoto2 --capture-image-and-download --keep --filename " + OutputDir + "%f.%C", shell=True)
				#print(output)
			#except ValueError:
			#	print "Something done fud up!"


			print("Finished processing")
	
			GPIO.output(BLUE_LED, False)

except KeyboardInterrupt:
	print("Keyboard Interrupt Detected")

finally:
	GPIO.cleanup()
