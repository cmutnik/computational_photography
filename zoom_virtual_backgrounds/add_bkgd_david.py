#!/bin/python
from PIL import Image

imfile = "David.jpg"

# open desired image
img = Image.open(imfile)
# img.crop((-10, -20, 1000, 500)).save("output.jpg")

# get dimensions of image that fits well in zoom
_sizewanted = Image.open("IMG_3477_1.jpg")
width, height = _sizewanted.size

# resize desired images
img.thumbnail((width, height), Image.ANTIALIAS)

# make black background of size from image that fits well
background = Image.new("RGB", (width, height))

# overlay desired image on black background
# background.paste(img, (int(width*.5), int(.5*height)))
w, h = img.size
background.paste(img, (int((width - w) / 2), int((height - h) / 2)))

# save
background.save("David_cropped.jpg")

# width, height = 1920, 1080
# background.save("David_cropped2.jpg")
