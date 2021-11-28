#!/bin/python

from moviepy.editor import ImageSequenceClip
from tqdm import tqdm
from PIL import Image
import argparse, os

parser = argparse.ArgumentParser(description="Convert Photoset to Video Montage")
parser.add_argument("-i", "--img_path", type=str, default=r"./testall/", metavar="str",
                    help="path to set of images for video (default: ./testall/)")
parser.add_argument("-t", "--thumbnail_dir", type=str, default="./thumbnails/", metavar="str",
                     help="path to where thumbnails will be saved (default: ./thumbnails/)")
parser.add_argument("-o", "--output_video", type=str, default=r"./thumbnails/final_pic_to_vid.mp4", metavar="str",
                    help="file path to save video results (default: ./thumbnails/final_pic_to_vid.mp4)")
parser.add_argument("-f", "--fps", type=float, default=1.15, metavar="float",
                    help="fps rate of exported video (default: 1.15)")
parser.add_argument("-x", "--x_resize_dim", type=int, default=1000, metavar="int",
                    help="x dimension to be used in resizing images and adding boarder (default: 1000)")
parser.add_argument("-y", "--y_resize_dim", type=int, default=1000, metavar="int",
                    help="y dimension to be used in resizing images and adding boarder (default: 1000)")
args = parser.parse_args()

def mkdir_if_it_dne(path):
    if not os.path.isdir(path):
        print(f"{path} did not exist, so it was made")
        os.mkdir(path)
    else:
        pass

def convert_images_to_thumbnails(img_path, outname, x, y):
    img = Image.open(img_path)
    img.thumbnail([x, y], Image.ANTIALIAS)
    # img.save(outname)
    return img

def add_background_to_image_to_standardize_sizes(inFilename, outFilename, x, y):
    if isinstance(inFilename, str):
        img = Image.open(inFilename)
    else:
        img = inFilename
    # x1, y1, x2, y2 = -5, -5, 1000, 1000  # cropping coordinates
    x1, y1, x2, y2 = 0, 0, x, y
    im = Image.new("RGB", (x2 - x1, y2 - y1), (0, 0, 0))
    im.paste(img, (-x1, -y1))
    im.save(outFilename)

def turn_photos_into_video_montage(filepaths, output_video, fps):
    clip = ImageSequenceClip(filepaths, fps=fps)
    clip.write_videofile(output_video)

if __name__ == "__main__":
    SAMPLE_INPUT_IMAGE_SET = args.img_path
    thumbnail_dir = args.thumbnail_dir
    output_video = args.output_video
    fps = args.fps
    x, y = args.x_resize_dim, args.y_resize_dim

    mkdir_if_it_dne(thumbnail_dir)
    # input_images = [x for x in os.walk(SAMPLE_INPUT_IMAGE_SET) if fname.endswith("jpg")]
    # for root, dirs, files in tqdm(input_images):
    for root, dirs, files in tqdm(os.walk(SAMPLE_INPUT_IMAGE_SET)):
        for fname in files:
            filepath = os.path.join(root, fname)
            outname = fname.split(".")[0]+"_thumbnail.jpg"
            outname = os.path.join(thumbnail_dir, outname)
            if os.path.isfile(outname):
                print(f"{outname} already exists, no thumbnail made")
            else:
                try:
                    img = convert_images_to_thumbnails(filepath, outname, x, y)
                    add_background_to_image_to_standardize_sizes(img, outname, x, y)
                except Exception as e:
                    # print(e.message, e.args)
                    print(f"failed to use: {filepath}")
    this_dir = os.listdir(thumbnail_dir)
    filepaths = [os.path.join(thumbnail_dir, fname) for fname in this_dir if fname.endswith("jpg")]

    turn_photos_into_video_montage(filepaths, output_video, fps)