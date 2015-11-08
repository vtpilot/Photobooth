#!/bin/bash

BaseDir=/home/pi/Photos/Photobooth/$(date +"%Y-%m-%d")

if [ ! -d $BaseDir ]; then
	echo Creating $BaseDir
	mkdir $BaseDir
fi

if [ ! -f $BaseDir/banner.jpg ]; then
	if [ -f /home/pi/Photos/banner.jpg ]; then
		echo Copying Banner.jpg
		cp /home/pi/Photos/banner.jpg $BaseDir
	fi
fi

pqiv --shuffle --watch-directories --slideshow --slideshow-interval=3 --hide-info-box -f $BaseDir 
