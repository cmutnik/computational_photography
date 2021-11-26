#!/bin/python
import cv2

def save_file_out(filename, src, filepath="../../figs/paintings/"):
    cv2.imwrite(filepath+filename, src)

def photo_to_oil_painting(img, size=7, dynRatio=1):
    res = cv2.xphoto.oilPainting(img, size, dynRatio)
    filename = f"IMG_3477_1_oil_painting_{size}_{dynRatio}.png"
    save_file_out(filename, res)

def photo_to_water_color_painting(img, sigma_s=60, sigma_r=0.6):
    # sigma_s controls the size of the neighborhood. Range 1 - 200
    # sigma_r controls the how dissimilar colors within the neighborhood will be averaged. A larger sigma_r results in large regions of constant color. Range 0 - 1
    res = cv2.stylization(img, sigma_s, sigma_r)
    filename = f"IMG_3477_1_water_color_painting_{sigma_s}_{sigma_r}.png"
    save_file_out(filename, res)

def photo_to_color_pencil(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05, color=True):
    # sigma_s controls the size of the neighborhood. Range 1 - 200
    # sigma_r controls the how dissimilar colors within the neighborhood will be averaged. A larger sigma_r results in large regions of constant color. Range 0 - 1
    # shade_factor is a simple scaling of the output image intensity. The higher the value, the brighter is the result. Range 0 - 0.1
    dst_gray, dst_color = cv2.pencilSketch(img, sigma_s, sigma_r, shade_factor)
    if color:
        filename = f"IMG_3477_1_color_pencil_color_{sigma_s}_{sigma_r}_{shade_factor}.png"
        save_file_out(filename, dst_color)        
    else:
        filename = f"IMG_3477_1_color_pencil_bnw_{sigma_s}_{sigma_r}_{shade_factor}.png"
        save_file_out(filename, dst_gray)

img = cv2.imread("../../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg")
photo_to_color_pencil(img)
photo_to_water_color_painting(img)
# photo_to_oil_painting(img, 100, 20)# requires: pip install opencv-contrib-python==4.3.0.36
