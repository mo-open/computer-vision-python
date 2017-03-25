__author__ = 'modoso'

from PIL import Image
import matplotlib.pyplot as plt
from pylab import array
import imtools

#read image into array
im = array(Image.open(imtools.imagePath('test.jpg')))

#draw image
plt.imshow(im)

#4 dots (x[0,y[0]), (x[1],y[1]) ...
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

#draw 4 dot
plt.plot(x[0], y[0], 'b*')
plt.plot(x[1], y[1], 'r*')
plt.plot(x[2], y[2], 'y*')
plt.plot(x[3], y[3], 'w*')

#draw line
plt.plot(x[:4], y[:4],'y-')

#Set title
plt.title('Plotting: "test.jpg"')

#close axis
plt.axis('off')

#show image
plt.show()