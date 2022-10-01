# Image Stacking Script from
# http://onlyjus-photopy.blogspot.com/2012/09/image-stacking.html
# may wanna also try subtracting frames as shown on site


from PIL import Image
import glob
import numpy as np


# CHANGE IF NOT PNG
imgList = glob.glob('./*.png')

first = True
for i in imgList:
    temp = np.array(Image.open(i)) #overcome overflow (pixel values between 0-255) by making array
    temp = temp.astype('uint32')   #1000 photos- 255*1000=255,000...unit32 hold 0-4294967295
    # make new variable to hold sum, or add current image to summed image
    if first:
        sumImage = temp
        first = False
    else:
        sumImage = sumImage + temp

# calc avg image...CAST AS FLOAT?????
avgArray = sumImage/len(imgList)

# convert back to unit8 data type then into PIL class
avgImg = Image.fromarray(avgArray.astype('uint8'))

# shows image...CAN ALSO SAVE
avgImg.show()


