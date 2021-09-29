#!/bin/python
from PIL import Image

imfile = "../figs/zoom_virtual_backgrounds/David.jpg"
img = Image.open(imfile)

_sizewanted = Image.open("../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg")
width, height = _sizewanted.size
img.thumbnail((width, height), Image.ANTIALIAS)

background = Image.new("RGB", (width, height))

w, h = img.size

background.paste(img, (int((width - w) / 2), int((height - h) / 2)))# overlay desired image on black background

background.save("../figs/zoom_virtual_backgrounds/David_cropped.jpg")
