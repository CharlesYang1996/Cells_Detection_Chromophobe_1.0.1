import os
import time
import numpy
from PIL import Image
from multiprocessing import Pool

# Path to where my test images are stored
img_folder = os.path.join(os.getcwd(), "test2.jpg")

# Collects all of the filenames for the images
# I want to process
images = [os.path.join(img_folder,f)
        for f in os.listdir(img_folder)
        if '.jpeg' in f]

# Your code, but wrapped up in a function
def convert(filename):
    im = Image.open(filename)
    w,h = im.size
    imc = im.crop((w-50,h-50,w+50,h+50))
    return numpy.array(imc)

def main():
    # This is the hero of the code. It creates pool of
    # worker processes across which you can "map" a function
    pool = Pool()

    t = time.time()
    # We run it normally (single core) first
    np_arrays = map(convert, images)
    print ('Time to open %i images in single thread: %.4f seconds'%(len(images), time.time()-t))

    t = time.time()
    # now we run the same thing, but this time leveraging the worker pool.
    np_arrays = pool.map(convert, images)
    print ('Time to open %i images with multiple threads: %.4f seconds'%(len(images), time.time()-t))

if __name__ == '__main__':
    main()