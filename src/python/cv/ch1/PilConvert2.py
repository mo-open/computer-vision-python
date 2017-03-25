__author__ = 'modoso'
from PIL import Image
import matplotlib.pyplot as plt
from pylab import array
import imtools

def showFigure(im):
    plt.figure()
    plt.gray()
    plt.contour(im, origin='image')
    print int(im.min()), int(im.max())

# convert to gray and read into array
im1 = array(Image.open(imtools.imagePath('test.jpg')).convert('L'))
# create a image in plt
showFigure(im1)

im2 = 255 - im1
showFigure(im2)

im3 = (100.0 / 255) * im1 + 100
showFigure(im3)

im4 = 255.0 * (im1 / 255.0) ** 2
showFigure(im4)

plt.show()