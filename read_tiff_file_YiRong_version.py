"""
@title Implementing Sliding Window on Huge Medical Slide
@author Yi Rong
@date 4/16/2021
"""
import sys
import openslide
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import pylab
from matplotlib.figure import Figure
from PIL import Image
import cv2 as cv
import glob
from get_entropy import get_entropy
import time


def judge(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow("gray", gray)

    gauss = cv.GaussianBlur(gray, (5, 5), 5)
    # cv.imshow("gauss1",gauss)

    ret, thresh = cv.threshold(gauss, 180, 255, 0)

def get_small_batch(path):



    start_loc = (10000, 40000)  # start location (0, 10000)
    batch_size = (5000, 5000)  # batch size
    level_dimension = 0  # 0 for highest resolution

    # read file
    slide = openslide.OpenSlide(path)
    [m, n] = slide.dimensions  # 得出高倍下的（宽，高）(97792,219648)
    print("Tiff file image size: [width-%d height-%d]"%(m,n))
    # get the size of image
    [end_x1, end_y1] = slide.level_dimensions[level_dimension]

    #fake size
    end_x1, end_y1 = 50000, 61000
    processed_images_counter=0
    # sliding window
    for loc_y in range(start_loc[1], end_y1 + batch_size[1], batch_size[1]):
        for loc_x in range(start_loc[0], end_x1 + batch_size[0], batch_size[0]):
            tile = np.array(slide.read_region((loc_x, loc_y), level_dimension, batch_size))
            plt.figure(figsize=(8, 8))
            plt.imshow(tile)
            plt.title("Image loc: ({}, {})".format(loc_x, loc_y))
            path_file_number = glob.glob('silde_imgs/*.png')
            path_file_number1 = glob.glob('silde_empty_imgs/*.png')
            #plt.savefig("silde_imgs/%d.png"%(len(path_file_number)+1))
            #plt.show()
            tile = cv.cvtColor(tile, cv.COLOR_BGR2GRAY)

            entropy=get_entropy(tile)
            print("Entropy 熵：%f"%(entropy))
            plt.title("Image loc: ({}, {},{})".format(loc_x, loc_y,entropy))

            if entropy>5:
                plt.savefig("silde_imgs/%d.png" % (len(path_file_number) + 1))
            else:
                plt.savefig("silde_empty_imgs/%d.png" % (len(path_file_number1) + 1))
            #plt.show()
            #cv.imshow("1",tile)
            #cv.waitKey()

    print("finished")
    print("Normal images：%d, Blank images：%d"%(len(path_file_number),len(path_file_number1)))
    end_time = time.clock()
    print('Average time: %f per img' % ((end_time - start_time)/(len(path_file_number)+len(path_file_number1))))
    print('Running time: %s Seconds' % (end_time - start_time))
if __name__ == "__main__":
    start_time = time.clock()
    os_path = os.getcwd()
    if not os.path.exists(os_path+'\\silde_imgs'):
        os.makedirs(os_path+'\\silde_imgs')
    else:
        shutil.rmtree(os_path+'\\silde_imgs')
        os.mkdir(os_path+'\\silde_imgs')
    if not os.path.exists(os_path+'\\silde_empty_imgs'):
        os.makedirs(os_path+'\\silde_empty_imgs')
    else:
        shutil.rmtree(os_path+'\\silde_empty_imgs')
        os.mkdir(os_path+'\\silde_empty_imgs')

    get_small_batch('H:/test1.tiff')
    if len(sys.argv) == 2:
        get_small_batch(sys.argv[1])
    else:
        print(len(sys.argv))
        print("Usage: python sliding_window.py <Image Path>")