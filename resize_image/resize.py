#!/bin/python
from PIL import Image
from glob import glob
from tqdm import tqdm

def get_list_of_input_images(filepath="./*", excluded_extensions=["py"]):
    return [file for file in glob(filepath) if file.split(".")[-1] not in excluded_extensions]
     
def resize_image(image, scale_factor=0.25):
    return image.resize( (int(image.size[0]*scale_factor), int(image.size[1]*scale_factor)) )

def save_resized_image(image, filename):
    image.save(filename.split("/")[-1].split(".")[0]+"_resized.png")

if __name__ == '__main__':
    filelist = get_list_of_input_images()
    for filename in tqdm(filelist):
        img = Image.open(filename)
        new_image = resize_image(img)
        save_resized_image(new_image, filename)