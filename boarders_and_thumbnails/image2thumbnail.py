#!/bin/python
from PIL import Image

inFilename = "../figs/boarders_and_thumbnails/Obs_PS_lsum_aitoff_map.png"
outFilename = "../figs/boarders_and_thumbnails/out_img2thumbnail.png"

img = Image.open(inFilename)
img.thumbnail([500, 500], Image.ANTIALIAS)
img.save(outFilename)
