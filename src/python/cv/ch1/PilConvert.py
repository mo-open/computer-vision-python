# coding=utf-8
__author__ = 'modoso'

from PIL import Image
import matplotlib.pyplot as plt
from pylab import array
import imtools

# read image into array
im = array(Image.open(imtools.imagePath('test.jpg')).convert('L'))

#draw image
plt.imshow(im)

#Set title
plt.title('Plotting: "test.jpg"')

#close axis
plt.axis('off')

#show image
plt.show()