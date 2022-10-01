#!/bin/python
from PIL import Image, ImageOps
from glob import glob
from tqdm import tqdm
import argparse, os

parser = argparse.ArgumentParser(description="Add border around images")
parser.add_argument("-i", "--img_path", type=str, default=r"./original/", metavar="str",
                    help="path to set of images that need a boarder added around them (default: ./original/)")
parser.add_argument("-o", "--output_dir", type=str, default="./with_100pixel_black_boarder/", metavar="str",
                     help="path to where output images will be saved (default: ./with_100pixel_black_boarder/)")
parser.add_argument("-b", "--border_width", type=int, default=100, metavar="int",
                    help="width of border to add, in pixels (default: 100px)")
parser.add_argument("-f", "--fill_color", type=str, default="black", metavar="str",
                    help="color for the border (default: black)")
args = parser.parse_args()

def mkdir_if_it_dne(path):
    if not os.path.isdir(path):
        # print(f"{path} did not exist, so it was made")
        os.mkdir(path)
    else:
        pass

def add_border_to_image(img_path, border_width, fill_color, out_path):
    ImageOps.expand(Image.open(img_path), border=border_width, fill=fill_color).save(out_path)

if __name__ == "__main__":
    img_path = args.img_path
    output_dir = args.output_dir
    border_width = args.border_width
    fill_color = args.fill_color
    
    mkdir_if_it_dne(output_dir)
    
    for root, dirs, files in os.walk(img_path):
        for fname in tqdm(files):
            filepath = os.path.join(root, fname)
            out_name = fname.split(".")[0] + "_" + str(border_width) + str(fill_color) + ".jpg"
            out_path =  os.path.join(output_dir, out_name)
            try:
                add_border_to_image(filepath, border_width, fill_color, out_path)
            except:
                # print(f"fname: {fname}\nout_path: {out_path}")
                print(f"failed to make: {out_name}")



