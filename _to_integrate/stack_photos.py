# script for stacking images by comparing each image to the other images in the folder
# pixel by pixel, and taking the lighter ones


from PIL import Image, ImageChops
import glob

imgList = glob.glob('./*.jpg')

im = Image.open(imgList[0])

for i in range(1,len(imgList)):
    tempIm = Image.open(imgList[i])
    resultIm = ImageChops.lighter(im, tempIm)

resultIm.show()
