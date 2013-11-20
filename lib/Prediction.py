import matplotlib.nxutils as nx
import numpy as np
from SimpleCV import *

class Prediction:
  def __init__(self, blobs, motions, size):
    self.blobs = blobs
    self.motions = motions
    self.image = Image(size)

    self.makePrediction()

  def makePrediction(self):

    for blob in self.blobs:
      dxs = []
      dys = []
      #magnitudes = []
      #angles = []

      for motion in self.motions:
        if nx.pnpoly(motion.x, motion.y, blob.contour()):
          #dxs.append(motion.dx)
          #dys.append(motion.dy)
          (uvx, uvy) = motion.vector()
          dxs.append(uvx)
          dys.append(uvy)
          #angles.append(np.rad2deg(np.arctan(uvy/uvx)))
          #magnitudes.append(motion.magnitude())

      #if not math.isnan(np.mean(magnitudes)):
      if not math.isnan(np.mean(dxs)):
        mean_dx = np.mean(dxs)
        mean_dy = np.mean(dys)
        print("mean_dx" + str(mean_dx))
        print("mean_dy" + str(mean_dy))

        blob_img = blob.blobImage()
        (size_x, size_y) = blob_img.size()

        new_x = int(blob.x + mean_dx) - size_x/2
        new_y = int(blob.y + mean_dy) - size_y/2 

        alpha_mask = blob_img.binarize().invert()
        self.image = self.image.blit(blob_img, pos=(new_x, new_y), alphaMask=alpha_mask)
        #self.image.drawCircle( (blob.x - mean_dx, blob.y - mean_dy), 2, Color.RED, thickness=-1)
        #mean_mag = np.mean(magnitudes)
        #mean_ang = np.mean(angles)
        #self.image.drawText(text=str(mean_mag) + " " + str(mean_ang) , x=blob.x, y=blob.y, color=Color.RED)


  def show(self):
    self.image.show()

  def waitForClick(self, disp):
    while disp.isNotDone():
      if disp.mouseLeft:
        break

