import numpy as np
from SimpleCV import *

img1 =  Image("sample_data/DTX_20131021_2247_NCR.gif")#.smooth()
img2 =  Image("sample_data/DTX_20131021_2302_NCR.gif")#.smooth()
#
#grey = img1.greyscale()
#grey.show()


#img1 = Image("1.tif")
#img2 = Image("2.tif")

#img1 = Image("taxi01.pgm")
#img2 = Image("taxi04.pgm")

print "images imported"
#
#motion = img2.findMotion(img1, window=11, method="BM", aggregate=True)
#motion = img2.findMotion(img1, window=11, method="LK", aggregate=True)
motion = img2.findMotion(img1, window=10, method="HS", aggregate=True)


blobs = img2.findBlobs()
blobs.draw()


#
#print "found motion"
##
##motion.draw(color=Color.RED, width=2)#, autocolor=True)#, normalize=False)
##
##
###f = open("out.txt", 'w')
##
##
#mags = []
#
#for m in motion:
#	if m.magnitude() > 0:
#		mags.append(m.magnitude())
#		m.draw(color=Color.RED,normalize=False)
##	#if m.magnitude() > biggest:
##	#	biggest = m.magnitude()
##	#m.draw()
##	#if(m.magnitude() > 0):
##	#f.write(str(m.magnitude()) + " " + str(m.vector()) + "\n")
##
#print "average: " + str(np.average(mags))
#print "largest: " + str(np.amax(mags))
###f.close()
img2.show()
##
###motion.save("out.tif")
##
raw_input("press any key...")
