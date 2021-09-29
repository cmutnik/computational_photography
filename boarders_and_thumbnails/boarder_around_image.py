#!/bin/python
from PIL import Image, ImageOps

inFilename = "../figs/boarders_and_thumbnails/Obs_PS_lsum_aitoff_map.png"
outFilename = "../figs/boarders_and_thumbnails/out_boarder_around_image.png"

ImageOps.expand(Image.open(inFilename), border=30, fill="white").save(outFilename)
