#!/bin/python
from PIL import Image

imfile = "../figs/zoom_virtual_backgrounds/Cambodia.jpg"
img = Image.open(imfile)
width, height = 1920, 1080
img.thumbnail((width, height), Image.ANTIALIAS)
background = Image.new("RGB", (width, height))
w, h = img.size
background.paste(img, (int((width - w) / 2), int((height - h) / 2)))
background.save("../figs/zoom_virtual_backgrounds/Cambodia_resized.jpg")
