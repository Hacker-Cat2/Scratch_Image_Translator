from imageio import imread
import colorsys
import os

maxPixels = 4294967296

h = 0.0
l = 0.0
s = 0.0
a = 0.0

def add0s(value = "", length = 1):
    value = str(value)

    for i in range(value.__len__(), length):
      value = "0" + value

    return(value)

class imageToCode():
  def __init__(self, imgPath = "", codePath = ""):
    self.imgPath = str(imgPath)
    self.codePath = str(codePath) + ".txt"
    self.iImg = []
    self.size = []
    self.oImg = ""
    self.error = ""
    
    try:
      self.iImg = imread(self.imgPath).tolist()
      self.size = self.iImg[0].__len__(), self.iImg.__len__()
    except:
      self.error = "Error loading image. Make sure the path is correct, and that it is a normal image file type."

    if self.error == "":
      if self.size[0] * self.size[1] > maxPixels:
        self.error = "Error. Image is too large."

    if self.error == "":
      self.oImg = str(self.size[0]) + "," + str(self.size[1]) + ","

      for y in range(0, self.size[1]):
        temp = ""

        for x in range(0, self.size[0]):
          p = self.iImg[y][x]
          a = 255.0
    
          if p.__len__() > 3:
            a = p[3]

          h, s, v = colorsys.rgb_to_hsv(p[0] / 255, p[1] / 255, p[2] / 255)
          temp += add0s(str(round(h * 100)), 3) + add0s(str(round(s * 100)), 3) + add0s(str(round(v * 100)), 3) + add0s(str(100 - round(a / 2.55)), 3)

        self.oImg += temp
        print(str(round((y + 1) / self.size[1] * 10000) / 100))

  def printCode(self):
    if self.error == "":
      print(self.oImg)
      print("Here's the code! ↑")
    else:
      print(self.error)
      return(self.error)

  def saveToFile(self):
    if self.error == "":
      print("Saving file...")

      if os.path.exists(self.codePath):
        self.error = "Error. File already exists."
        print(self.error)
        print("Here is the code:")
        print(self.oImg)
        return(self.error)
      else:
        try:
          f = open(self.codePath, "w+")
          f.write(self.oImg)
          print("Succesfully saved the file!")
        except:
          self.error = "Error. Couldn't create the specified directory."
          print(self.error)
          print("Here is the code:")
          print(self.oImg)
          return(self.error)
    else:
      print(self.error)
      return(self.error)