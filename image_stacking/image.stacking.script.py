#!/bin/python
from PIL import Image
import glob
import numpy as np

imgList = glob.glob("./*.JPG")

first = True
for i in imgList:
    temp = np.array(
        Image.open(i)
    )  # overcome overflow (pixel values between 0-255) by making array
    temp = temp.astype(
        "uint32"
    )  # 1000 photos- 255*1000=255,000...unit32 hold 0-4294967295
    # make new variable to hold sum, or add current image to summed image
    if first:
        sumImage = temp
        first = False
    else:
        sumImage = sumImage + temp

avgArray = sumImage / len(imgList)
avgImg = Image.fromarray(avgArray.astype("uint8"))

avgImg.save("_stack_all_" + str(len(imgList)) + ".JPG")
