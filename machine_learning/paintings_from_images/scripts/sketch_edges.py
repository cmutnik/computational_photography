#!/bin/python
import cv2

infile = "../../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg"
outfile = "../../figs/paintings/IMG_3477_1_sketch_edges.jpg"

image = cv2.imread(infile,0)
inverted = 255 - image
inverted_blured = 255 - cv2.GaussianBlur(inverted,(21,21),0)
sketch = 255 * (image / inverted_blured)

cv2.imwrite(outfile,sketch)