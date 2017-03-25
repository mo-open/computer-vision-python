__author__ = 'modoso'
from PIL import Image
import matplotlib.pyplot as plt
from pylab import array
import imtools

# read image into array
im = array(Image.open(imtools.imagePath('test.jpg')))

plt.imshow(im)

print 'Please click 3 points'
x = plt.ginput(3)
print 'you clicked:', x
plt.show()