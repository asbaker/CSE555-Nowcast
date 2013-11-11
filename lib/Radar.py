from RadarColor import *
from SimpleCV import *
import numpy as np

class Radar:
  def __init__(self, image):
    self.image = image;

  def removeReflectivity(self, *colors):
    copy = self.image.copy()

    for color in colors:
      distance = copy.colorDistance(color=color).binarize(0)
      copy = copy + distance

    return Radar(copy)

  def findRain(self):
    return self.removeReflectivity(RadarColor.Z0, RadarColor.Z5, RadarColor.Z10, RadarColor.Z15, RadarColor.Z20)

  def smooth(self):
    return Radar(self.image.copy().smooth())

  def placePoi(self, point):
    copy = self.image.copy()
    copy.drawCircle(point, 2, Color.RED, thickness=-1)
    return Radar(copy)

  def show(self):
    self.image.show()

  def waitForClick(self, disp):
    while disp.isNotDone():
      if disp.mouseLeft:
        break

  def getCells(self):
    copy = self.image.copy()

    palette = copy.getPalette(bins=2)
    palette = np.array(filter(lambda c: c[0] < 200, palette))

    blobs = copy.findBlobsFromPalette(palette)

    if (blobs is not None):
      print "wooooooooo"
      for b in blobs:
        b.drawOutline(color=Color.HOTPINK, width=-1,alpha=128)

    return (Radar(copy), blobs)

  def getMotion(self, prior):
    copy = self.image.copy()

    motion = copy.findMotion(prior.image, method="HS")
    filtered_motion = filter(lambda m: m.magnitude() > 0 and copy.getPixel(int(m.x), int(m.y)) != Color.WHITE, motion)

    for m in filtered_motion:
      m.draw(color=Color.PLUM,normalize=False)

    return (Radar(copy), filtered_motion)

