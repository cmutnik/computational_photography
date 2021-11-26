#!/bin/python
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import string

siz = 200
im = Image.open("../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg").resize([siz, siz])
im2 = im.convert(mode = 'L')
im4 = np.array(im2.getdata()).reshape([siz, siz])

asci =  r"QG@#$%?*+^)/;:!,'.` "
# asci2 = r"B8&WM#YXQO{}[]()I1i!pao;:,.    "

im7 = []
for i in range(siz):
    imtemp = ""
    for j in range(siz):
        imtemp+= asci[(len(asci)-1)*im4[i,j]//256]
    im7.append(imtemp)

with open('./ascii_art.txt', 'w') as text:
    for i in im7:
        text.write(i)
        text.write('\n')
# print('Image written to .txt file.')