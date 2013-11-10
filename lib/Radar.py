from RadarColor import *

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

