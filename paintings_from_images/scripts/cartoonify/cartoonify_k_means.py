#!/bin/python
import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser(description="Turn Image into Cartoon")
parser.add_argument("-i", "--img_path", type=str, default=r"../../../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg", metavar="str",
                    help="paths to input image (default: '../../../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg')")
parser.add_argument("-o", "--output_dir", type=str, default=r"../../../figs/paintings/", metavar="str",
                    help="dir to save resized image results (default: ../../../figs/paintings/)")
parser.add_argument("-l", "--line_size", type=int, default=7, metavar="int",
                    help="line size to be used (default: 7)")
parser.add_argument("-b", "--blur_value", type=int, default=7, metavar="int",
                    help="blur value to be used (default: 7)")
parser.add_argument("-k", "--total_color", type=int, default=9, metavar="int",
                    help="total colors to be used for k value in k-means (default: 9)")
args = parser.parse_args()


def read_file(filename):
    return cv2.imread(filename)

def save_out_cartoon_image(cartoon, filename=args.img_path, output_dir=args.output_dir):
    output_dir = output_dir if output_dir is not None and output_dir[-1]=="/" else output_dir + "/"
    basename = filename.split("/")[-1].split(".")[0]
    filename = output_dir + basename + "_cartoonified.png"
    cv2.imwrite(filename, cartoon)

def edge_mask(img, line_size=args.line_size, blur_value=args.blur_value):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, blur_value)
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
    return edges

def color_quantization(img, k=args.total_color):
    data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

    # Implementing K-Means
    ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result

if __name__ == "__main__":
    filename = args.img_path
    img = read_file(filename)
    edges = edge_mask(img)
    img = color_quantization(img)
    blurred = cv2.bilateralFilter(img, d=7, sigmaColor=200,sigmaSpace=200)
    cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
    save_out_cartoon_image(cartoon)
    cv2.destroyAllWindows()
