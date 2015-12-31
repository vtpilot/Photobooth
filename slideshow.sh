#!/bin/bash

BaseDir=/home/pi/Pictures/$(date +"%Y-%m-%d")

if [ ! -d $BaseDir ]; then
	echo Creating $BaseDir
	mkdir $BaseDir
fi

if [ ! -f $BaseDir/banner.jpg ]; then
	echo Banner does not exist
	if [ -f /home/pi/Pictures/banner.jpg ]; then
		echo Copying Banner.jpg
		cp /home/pi/Pictures/banner.jpg $BaseDir
	fi
fi

pqiv --fullscreen --scale-images-up --fade --shuffle --watch-directories --slideshow --slideshow-interval=3 --hide-info-box  $BaseDir 
