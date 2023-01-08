#!/bin/python
"""Script for resizing and formatting images, to better display on web.
    Example use case:
        ```py
        python manipulate_images_for_web.py -i test/* -o test/. -oe webp -sf 0.5
        ```
    - convert all images in `test/`
    - store the outputs in `test/`
    - scale each image by a factor of 0.5
    - save output images as `*.webp` files
"""

from PIL import Image
from glob import glob
from tqdm import tqdm
import argparse, os

parser = argparse.ArgumentParser(description="Manipulate Images")
parser.add_argument("-i", "--img_path", type=str, default=r"./*", metavar="str",
                    help="paths to set of images that need to be resized (default: ./*)")
parser.add_argument("-o", "--output_dir", type=str, default=r"./", metavar="str",
                    help="dir to save resized image results (default: ./)")
parser.add_argument("-sf", "--scale_factor", type=float, default=1, metavar="float",
                    help="scale factor to multiply image dimensions by (default: 1)")
parser.add_argument("-oe", "--output_extension", type=str, default="webp", metavar="str",
                    help="extension type of resized image (default: webp)")
parser.add_argument("-ee", "--excluded_extensions", action='append', default=["py"], metavar="list of strings",
                    help="list of str that make consists of file extensions to ignore in img_path dir (default: [\"py\"])")
parser.add_argument("-r", "--rotate_image", type=int, default=False, metavar="int",
                    help="bool option to rotate image by $-90\deg$ (default: False)")
args = parser.parse_args()

def make_output_dir_if_it_DNE(output_dir):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

def get_list_of_input_images(filepath, excluded_extensions):
    return [file for file in glob(filepath) if file.split(".")[-1] not in excluded_extensions and not os.path.isdir(file)]
     
def resize_image(image, scale_factor):
    return image.resize( (int(image.size[0]*scale_factor), int(image.size[1]*scale_factor)) )

def get_final_output_name(filename, output_dir, output_extension):
    output_dir = output_dir if output_dir[-1]=="/" else output_dir + "/"
    basename = filename.split("/")[-1].split(".")[0]
    final_output_name = output_dir + basename + "_resized." + output_extension
    return final_output_name

def save_resized_image(image, final_output_name, output_extension):
    image.save(final_output_name, format=output_extension)

def rotate_image(image, degrees_to_rotate_by=-90):
    return image.rotate(degrees_to_rotate_by, Image.NEAREST, expand = 1) 

if __name__ == "__main__":
    output_extension = args.output_extension
    make_output_dir_if_it_DNE(args.output_dir)
    filelist = get_list_of_input_images(filepath=args.img_path, excluded_extensions=args.excluded_extensions)
    for filename in tqdm(filelist):
        img = Image.open(filename)
        new_image = resize_image(img, scale_factor=args.scale_factor)
        final_output_name = get_final_output_name(filename, output_dir=args.output_dir, output_extension=output_extension)
        if args.rotate_image:
            new_image = rotate_image(new_image, args.rotate_image)
        save_resized_image(new_image, final_output_name, output_extension)