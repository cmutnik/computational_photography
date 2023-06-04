#!/bin/python
import cv2
import os

# Define image paths
img = "../../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg"
out_path = "../../figs/edge_detection"

SAVE_IMAGE_BUT_DO_NOT_DISPLAY = True
SHOW_IMAGES_BUT_DO_NOT_SAVE = False

def mkdir_if_it_dne(path):
    if not os.path.isdir(path):
        print(f"{path} did not exist, so it was made")
        os.mkdir(path)
    return

mkdir_if_it_dne(out_path)

# Read the original image
img = cv2.imread(img,flags=0)  
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img,(3,3), sigmaX=0, sigmaY=0) 

# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) 

if SAVE_IMAGE_BUT_DO_NOT_DISPLAY:
    # Save Sobel and Canny Edge Detection Images
    cv2.imwrite(f'{out_path}/Sobel_X.png', sobelx)
    cv2.imwrite(f'{out_path}/Sobel_Y.png', sobely)
    cv2.imwrite(f'{out_path}/Sobel_X_Y_using_Sobel_function.png', sobelxy)
    cv2.imwrite(f'{out_path}/Canny_Edge_Detection.png', edges)

if SHOW_IMAGES_BUT_DO_NOT_SAVE:
    # Display Sobel Edge Detection Images
    cv2.imshow('Sobel X', sobelx)
    cv2.waitKey(0)

    cv2.imshow('Sobel Y', sobely)
    cv2.waitKey(0)

    cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
    cv2.waitKey(0)

    # Display Canny Edge Detection Image
    cv2.imshow('Canny Edge Detection', edges)
    cv2.waitKey(0)

