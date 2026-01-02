import cv2

img = cv2.imread('assets/mash.jpg', 1)
img = cv2.resize(img, (400,400))

# -1, cv2.IMREAD_COLOR : color image
# 0, cv2.IMREAD_GRAYSCALE : grayscale image
# 1, cv2.IMREAD_UNCHANGED : image as such including alpha channel

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()