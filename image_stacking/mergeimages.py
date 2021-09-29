# https://bespokeblog.wordpress.com/category/programming/python/
import sys
from PIL import Image


def imageblend(imdir, numimages=54, blendwidth=0):
    if not blendwidth % 2 == 0:
        raise Exception("blendwidth not even")

    im = Image.open(imdir + "im1.jpg")
    (width, height) = im.size

    for i in range(1, numimages):
        imnum = i + 1
        centre = i * width / numimages - 1

        im_i = Image.open(imdir + "im%d.jpg" % imnum)

        for x in range(blendwidth):
            col_ind = centre - (blendwidth / 2) + x + 1
            col_box = (col_ind, 0, col_ind + 1, height - 1)
            col_o = im.copy().crop(col_box)
            col_i = im_i.copy().crop(col_box)
            col = Image.blend(col_o, col_i, float(x) / blendwidth)
            im.paste(col, col_box)

        rest_box = (centre + blendwidth / 2 + 1, 0, width - 1, height - 1)
        rest = im_i.copy().crop(rest_box)
        im.paste(rest, rest_box)

    im.save(imdir + "im_output.jpg")


def main():
    imdir = sys.argv[1]
    imageblend(imdir)


if __name__ == "__main__":
    main()
