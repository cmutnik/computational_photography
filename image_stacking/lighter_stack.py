# http://onlyjus-photopy.blogspot.com/
from PIL import Image, ImageChops
import glob

imgList = glob.glob("./*.JPG")

resultIm = Image.open(imgList[0])
for i in range(1, len(imgList)):
    tempIm = Image.open(imgList[i])
    resultIm = ImageChops.lighter(resultIm, tempIm)

resultIm.show()
