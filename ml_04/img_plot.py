import cv2
from matplotlib import pyplot as plt

fname = './HYNN/image/iu05.jpg'

image_color = cv2.imread(fname, cv2.IMREAD_COLOR)

b, g, r = cv2.split(image_color)
image_color2 = cv2.merge([r, g, b])

plt.imshow(image_color2)
plt.xticks([])
plt.yticks([])
plt.show()
