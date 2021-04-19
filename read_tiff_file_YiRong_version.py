"""
@title Implementing Sliding Window on Huge Medical Slide
@author Yi Rong
@date 4/16/2021
"""
import sys
import openslide
import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib.figure import Figure
from PIL import Image


def get_small_batch(path):
    start_loc = (0, 10000)  # start location (0, 0)
    batch_size = (1000, 1000)  # batch size
    level_dimension = 0  # 0 for highest resolution

    # read file
    slide = openslide.OpenSlide(path)

    # get the size of image
    [end_x1, end_y1] = slide.level_dimensions[level_dimension]

    # fake size
    end_x1, end_y1 = 10000, 11000

    # sliding window
    for loc_y in range(start_loc[1], end_y1 + batch_size[1], batch_size[1]):
        for loc_x in range(start_loc[0], end_x1 + batch_size[0], batch_size[0]):
            tile = np.array(slide.read_region((loc_x, loc_y), level_dimension, batch_size))
            plt.figure(figsize=(8, 8))
            plt.imshow(tile)
            plt.title("Image loc: ({}, {})".format(loc_x, loc_y))
            plt.show()

    print("finished")


if __name__ == "__main__":
    get_small_batch('H:/test1.tiff')
    if len(sys.argv) == 2:
        get_small_batch(sys.argv[1])
    else:
        print(len(sys.argv))
        print("Usage: python sliding_window.py <Image Path>")