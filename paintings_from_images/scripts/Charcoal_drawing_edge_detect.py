#!/bin/python
import matplotlib.pyplot as plt
import argparse, cv2, os
import numpy as np

parser = argparse.ArgumentParser(description="Turn Image into Cartoon")
parser.add_argument("-i", "--img_path", type=str, default=r"../../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg", metavar="str",
                    help="paths to input image (default: '../../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg')")
parser.add_argument("-o", "--output_path", type=str, default=r"../../figs/paintings/IMG_3477_1_charcoal.jpg", metavar="str",
                    help="dir to save resized image results (default: ../../figs/paintings/)")
parser.add_argument("-w", "--weak_thresh", type=int, default=10, metavar="int",
                    help="weak threshold value (default 10)")
parser.add_argument("-s", "--strong_thresh", type=int, default=1000, metavar="int",
                    help="strong threshold value (default 1000)")
args = parser.parse_args()


def Canny_detector(img, weak_th = None, strong_th = None):
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (5, 5), 1.4)
    gx = cv2.Sobel(np.float32(img), cv2.CV_64F, 1, 0, 3)
    gy = cv2.Sobel(np.float32(img), cv2.CV_64F, 0, 1, 3)
    mag, ang = cv2.cartToPolar(gx, gy, angleInDegrees = True)
    
    # thresholding for tuning edge detection
    mag_max = np.max(mag)
    if not weak_th:weak_th = mag_max * 0.1
    if not strong_th:strong_th = mag_max * 0.5
    print(f"weak_threshold: {weak_th}")
    print(f"strong_threshold: {strong_th}")
    
    height, width = img.shape
    
    for i_x in range(width):
        for i_y in range(height):
            
            grad_ang = ang[i_y, i_x]
            grad_ang = abs(grad_ang-180) if abs(grad_ang)>180 else abs(grad_ang)
            
            # selecting the neighbors of the target pixel
            # according to the gradient direction
            # In the x axis direction
            if grad_ang<= 22.5:
                neighb_1_x, neighb_1_y = i_x-1, i_y
                neighb_2_x, neighb_2_y = i_x + 1, i_y
            
            # top right (diagonal-1) direction
            elif grad_ang>22.5 and grad_ang<=(22.5 + 45):
                neighb_1_x, neighb_1_y = i_x-1, i_y-1
                neighb_2_x, neighb_2_y = i_x + 1, i_y + 1
            
            # In y-axis direction
            elif grad_ang>(22.5 + 45) and grad_ang<=(22.5 + 90):
                neighb_1_x, neighb_1_y = i_x, i_y-1
                neighb_2_x, neighb_2_y = i_x, i_y + 1
            
            # top left (diagonal-2) direction
            elif grad_ang>(22.5 + 90) and grad_ang<=(22.5 + 135):
                neighb_1_x, neighb_1_y = i_x-1, i_y + 1
                neighb_2_x, neighb_2_y = i_x + 1, i_y-1
            
            # Now it restarts the cycle
            elif grad_ang>(22.5 + 135) and grad_ang<=(22.5 + 180):
                neighb_1_x, neighb_1_y = i_x-1, i_y
                neighb_2_x, neighb_2_y = i_x + 1, i_y
            
            # Non-maximum suppression
            if width>neighb_1_x>= 0 and height>neighb_1_y>= 0:
                if mag[i_y, i_x]<mag[neighb_1_y, neighb_1_x]:
                    mag[i_y, i_x]= 0
                    continue

            if width>neighb_2_x>= 0 and height>neighb_2_y>= 0:
                if mag[i_y, i_x]<mag[neighb_2_y, neighb_2_x]:
                    mag[i_y, i_x]= 0

    weak_ids = np.zeros_like(img)
    strong_ids = np.zeros_like(img)            
    ids = np.zeros_like(img)
    
    # double thresholding
    for i_x in range(width):
        for i_y in range(height):
            
            grad_mag = mag[i_y, i_x]
            
            if grad_mag<weak_th:
                mag[i_y, i_x]= 0
            elif strong_th>grad_mag>= weak_th:
                ids[i_y, i_x]= 1
            else:
                ids[i_y, i_x]= 2
    return mag

if __name__ == "__main__":
    # frame = cv2.imread("../../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg")
    frame = cv2.imread(args.img_path)
    canny_img = Canny_detector(frame, args.weak_thresh, args.strong_thresh)
    cv2.imwrite("../../figs/paintings/IMG_3477_1_charcoal.jpg", canny_img)