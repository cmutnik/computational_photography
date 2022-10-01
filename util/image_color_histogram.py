#!/bin/python
import matplotlib.pyplot as plt
import numpy as np
import skimage


def img_color_hist(image_path="../figs/image_stacking/first_stacked_image.JPG", savefig=False):
    """Generate a histogram with three lines, one for each color. 

    Args:
        image_path (str, optional): Path to input image. Defaults to "../figs/image_stacking/first_stacked_image.JPG".
    """

    image = skimage.io.imread(image_path)

    # Tuple to select colors of each channel line.
    colors = ("red", "green", "blue")
    channel_ids = (0, 1, 2)

    # Create the histogram plot with three lines, one for each color.
    plt.figure()
    plt.xlim([0, 256])
    for channel_id, c in zip(channel_ids, colors):
        histogram, bin_edges = np.histogram(
            image[:, :, channel_id], bins=256, range=(0, 256)
        )
        plt.plot(bin_edges[0:-1], histogram, color=c)

    plt.title("Color Histogram")
    plt.xlabel("Color value")
    plt.ylabel("Pixel count")

    if savefig:
        plt.savefig(savefig)
    else:
        plt.show()
    return
