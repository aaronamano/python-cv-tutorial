# tutorial 2
import cv2
import random

img = cv2.imread('assets/mash.jpg', -1)

# print(img) -> 2d array representation of image, each sub array is a BGR (blue, green, red) pixel
# print(img.shape) # -> (height (rows), width (columns), channels (colorspace))
# [0, 0, 0] -> [blue, green, red] with each value ranging from 0 to 255

# manipulate image by changing color of pixels
'''
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
'''

# (1200, 555, 3)

# manipulate image by copying part of an image and pasting it on a different part of an image
tag = img[100:300, 50:250]
img[400:600, 300:500] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()