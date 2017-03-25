__author__ = 'modoso'

from PIL import Image
import matplotlib.pyplot as plt
from pylab import array, histogram, interp

import imtools


def showImage(im):
    # create a image in plt
    plt.figure()
    # no color
    plt.gray()
    # show image from left
    plt.contour(im, origin='image')

    plt.axis('equal')
    plt.axis('off')
    plt.figure()
    plt.hist(im.flatten(), 128)


# convert to gray and read into array
im = array(Image.open(imtools.imagePath('test.jpg')).convert('L'))
showImage(im)

im1 = array(Image.open(imtools.imagePath('test.jpg')).convert('L'))
a = im1.flatten()
im2, cdf = imtools.histeq(a, im1, 256)

showImage(im2)
plt.show()