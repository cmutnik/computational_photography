#!/bin/python
from PIL import Image
from glob import glob
from tqdm import tqdm
import argparse, os

parser = argparse.ArgumentParser(description="Resize Images")
parser.add_argument("-i", "--img_path", type=str, default=r"./*", metavar="str",
                    help="paths to set of images that need to be resized (default: ./*)")
parser.add_argument("-o", "--output_dir", type=str, default=r"./", metavar="str",
                    help="dir to save resized image results (default: ./)")
parser.add_argument("-sf", "--scale_factor", type=float, default=0.25, metavar="float",
                    help="scale factor to multiply image dimensions by (default: 0.25)")
parser.add_argument("-oe", "--output_extension", type=str, default="png", metavar="str",
                    help="extension type of resized image (default: png)")
parser.add_argument("-ee", "--excluded_extensions", action='append', default=["py"], metavar="list of strings",
                    help="list of str that make consists of file extensions to ignore in img_path dir (default: [\"py\"])")
args = parser.parse_args()

def make_output_dir_if_it_DNE(output_dir):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

def get_list_of_input_images(filepath, excluded_extensions):
    return [file for file in glob(filepath) if file.split(".")[-1] not in excluded_extensions and not os.path.isdir(file)]
     
def resize_image(image, scale_factor):
    return image.resize( (int(image.size[0]*scale_factor), int(image.size[1]*scale_factor)) )

def save_resized_image(image, filename, output_dir, output_extension):
    output_dir = output_dir if output_dir[-1]=="/" else output_dir + "/"
    basename = filename.split("/")[-1].split(".")[0]
    final_output_name = output_dir + basename + "_resized." + output_extension
    image.save(final_output_name)

if __name__ == "__main__":
    make_output_dir_if_it_DNE(args.output_dir)
    filelist = get_list_of_input_images(filepath=args.img_path, excluded_extensions=args.excluded_extensions)
    for filename in tqdm(filelist):
        img = Image.open(filename)
        new_image = resize_image(img, scale_factor=args.scale_factor)
        save_resized_image(new_image, filename, output_dir=args.output_dir, output_extension=args.output_extension)
