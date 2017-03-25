__author__ = 'modoso'
from PIL import Image
import matplotlib.pyplot as plt
from pylab import array
import imtools

im = array(Image.open(imtools.imagePath('test.jpg')).thumbnail((128,128)))

#draw image
plt.imshow(im)

#Set title
plt.title('Plotting: "test.jpg"')

#close axis
plt.axis('off')

#show image
plt.show()