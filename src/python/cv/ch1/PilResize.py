__author__ = 'modoso'

from PIL import Image
import matplotlib.pyplot as plt
from pylab import array
import imtools

# read image into array
im = array(Image.open(imtools.imagePath('test.jpg')))

im2=imtools.imresize(im,(640,640))

#draw image
plt.imshow(im2)

#Set title
plt.title('Plotting: "test.jpg"')

#close axis
plt.axis('off')

#show image
plt.show()