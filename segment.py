from lib.Radar import *
from lib.RadarColor import *
from lib.Prediction import *
from SimpleCV import *


range_px = 578
range_miles = 142
disp = Display()


# sample-data
#img1 =  Image("sample_data/DTX_20131021_2247_NCR.gif")
#img2 =  Image("sample_data/DTX_20131021_2302_NCR.gif")

# heavy started at 13:34
img1 = Image("sample_data/DTX_20131106_1223_NCR.gif")
img2 = Image("sample_data/DTX_20131106_1229_NCR.gif")
img3 = Image("sample_data/DTX_20131106_1235_NCR.gif")
#img = Image("sample_data/DTX_20131106_1241_NCR.gif")
#img = Image("sample_data/DTX_20131106_1247_NCR.gif")
#img = Image("sample_data/DTX_20131106_1252_NCR.gif")
#img = Image("sample_data/DTX_20131106_1258_NCR.gif")
#img = Image("sample_data/DTX_20131106_1304_NCR.gif")
#img = Image("sample_data/DTX_20131106_1310_NCR.gif")
#img = Image("sample_data/DTX_20131106_1316_NCR.gif")
#img = Image("sample_data/DTX_20131106_1321_NCR.gif")
#img = Image("sample_data/DTX_20131106_1327_NCR.gif")
#img = Image("sample_data/DTX_20131106_1333_NCR.gif")
#img = Image("sample_data/DTX_20131106_1339_NCR.gif")

radar1 = Radar(img1.copy())
rain1 = radar1.findRain().smooth();
#rain1 = rain1.placePoi((350,290))

radar2 = Radar(img2.copy())
rain2 = radar2.findRain().smooth();
(rain2, rain2_blobs) = rain2.getCells()
(rain2, rain2_motion) = rain2.getMotion(rain1)
rain2 = rain2.placePoi((350,290))


radar3 = Radar(img3.copy())
rain3 = radar3.findRain().smooth();

prediction = Prediction(rain2_blobs, rain2_motion, rain2.image.size())

rain1.show()
rain1.waitForClick(disp)
rain1.image.save("1.png")

rain2.show()
rain2.waitForClick(disp)
rain2.image.save("2.png")

rain3.show()
rain3.waitForClick(disp)
rain3.image.save("3.png")

prediction.show()
prediction.waitForClick(disp)
prediction.image.save("4.png")


###

actual_binary = rain3.image.binarize()
actual_binary.show()
actual_binary.save("5.png")
prediction.waitForClick(disp)

predicted_binary = prediction.image.binarize().invert()
predicted_binary.show()
predicted_binary.save("6.png")
prediction.waitForClick(disp)

error = actual_binary - predicted_binary
error.show()
error.save("7.png")
prediction.waitForClick(disp)

