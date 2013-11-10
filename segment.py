from lib.Radar import *
from lib.RadarColor import *
from SimpleCV import *

disp = Display()

range_px = 578
range_miles = 142


# sample-data
#img1 =  Image("sample_data/DTX_20131021_2247_NCR.gif")
#img2 =  Image("sample_data/DTX_20131021_2302_NCR.gif")

# heavy started at 13:34

img1 = Image("sample_data/DTX_20131106_1327_NCR.gif")
img2 = Image("sample_data/DTX_20131106_1333_NCR.gif")

radar1 = Radar(img1.copy())
radar2 = Radar(img2.copy())

rain1 = radar1.findRain().smooth();
rain1.image.drawCircle( (350,290), 2, Color.FUCHSIA, thickness=-1)

rain2 = radar2.findRain().smooth();
rain2.image.drawCircle( (350,290), 2, Color.FUCHSIA, thickness=-1)



motion = rain2.image.findMotion(rain1.image, method="HS")

mags = []

for m in motion:
  if m.magnitude() > 0 and rain2.image.getPixel(int(m.x), int(m.y)) != Color.WHITE:
    print "x:", m.x, "y:", m.y, "mag:", m.magnitude(), "vec:", m.vector(), rain2.image.getPixel(int(m.x),int(m.y))
    mags.append(m.magnitude())
    m.draw(color=Color.RED,normalize=False)

#rain1.image.show();
#raw_input("press any key....")
rain2.image.show();


average = np.average(mags)
maximum = np.amax(mags)

print "average px: " + str(average)
print "average miles: " + str(average*142/578*4)

print "largest px: " + str(maximum)
print "largest miles: " + str(maximum*142/578*4)


while disp.isNotDone():
  if disp.mouseLeft:
    break



#img1.sideBySide(rain1.image).show()
#rain1.image.sideBySide(rain2.image).show()

