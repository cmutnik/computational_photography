#!/bin/python
'''
from PIL import Image

#imfile='Cambodia.jpg'
imfile='20131114_154806.jpg'
# open desired image
img = Image.open(imfile)

width, height = 1920, 1080

img.thumbnail((width, height),Image.ANTIALIAS)

img.save("cambodia_1920w_1080h.jpg")


'''
########################################################
from PIL import Image
imfile='20131114_154806.jpg'
# open desired image
img = Image.open(imfile)
#_, height = img.size
# 768 is the height of the original image
#width = 1920
width, height = 1920, 1080
# resize desired images
img.thumbnail((width, height),Image.ANTIALIAS)
# make black background of size from image that fits well
background = Image.new('RGB', (width, height))
# overlay desired image on black background
#background.paste(img, (int(width*.5), int(.5*height)))
w,h=img.size
background.paste(img, (int((width-w)/2),int((height-h)/2)))
# save
background.save("cambodia_2.jpg")


#width, height = 1920, 1080
#background.save("c2.jpg")
