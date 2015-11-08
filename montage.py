def CreateMontage(now_string):
	print("Creating montage " + now_string)
	command = "montage " + basedir + "/" + now_string + "*.jpg -tile 2x2 -geometry 1920x1280+10+10 " + basedir + "/montages/" + now_string + "_montage.jpg"

def CreateMontage(now_string):
	print("Creating montage " + now_string)
	command = "montage " + basedir + "/" + now_string + "*.jpg -tile 2x2 -geometry 1920x1280+10+10 " + basedir + "/montages/" + now_string + "_montage.jpg"
 	subprocess.call(command, shell=True)
	command = "convert " + basedir + "/montages/" + now_string + "_montage.jpg" + " " + basedir + "/wedding_footer.jpg -gravity south -append " + basedir + "/mo    ntages/" + now_string + "_print.jpg"
 	subprocess.call(command, shell=True)
 
def PrintMontage(now_string):
	print("Printing montage " + now_string)
	command = "convert " + basedir + "/montages/" + now_string + "_montage.jpg" + " " + basedir + "/wedding_footer.jpg -gravity south -append " + now_string + "    _print.jpg"
 	subprocess.call(command, shell=True)
def Upload():
	command = "rsync -azP -e ssh /home/pi/photobooth_images/ eric@www.soteria-solutions.com:/var/www/magichardimuth.com/public_html/images/gallery_images/"
	subprocess.call(command, shell=True)

