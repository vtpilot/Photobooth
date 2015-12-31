#!/usr/bin/python

import time
import subprocess
import datetime
import os.path
import shutil
from CameraFunctions import CheckFolder, CheckFile

now = datetime.datetime.now().strftime('%Y-%m-%d')
SlideshowDir = "/home/pi/Pictures/" + now + "/"

InitialPicture = SlideshowDir + "banner.jpg"
DefaultPicture =  "/home/pi/Pictures/banner.jpg"

CheckFolder(SlideshowDir)
CheckFile(InitialPicture, DefaultPicture)

subprocess.call("pqiv --fullscreen --scale-images-up --fade --shuffle --watch-directories --slideshow --slideshow-interval=3 --hide-info-box " + SlideshowDir, shell=True)	
