#!/bin/python
from PIL import Image

inFilename = "../figs/boarders_and_thumbnails/Obs_PS_lsum_aitoff_map.png"
outFilename = "../figs/boarders_and_thumbnails/out_addBackground.jpg"

img = Image.open(inFilename)
x1, y1, x2, y2 = -10, -20, 1000, 1000  # cropping coordinates
im = Image.new("RGB", (x2 - x1, y2 - y1), (255, 255, 255))
im.paste(img, (-x1, -y1))
im.save(outFilename)
