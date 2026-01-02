# tutorial 1
import cv2

# read image
img = cv2.imread('assets/mash.jpg', 1)
# -1, cv2.IMREAD_COLOR : color image
# 0, cv2.IMREAD_GRAYSCALE : grayscale image
# 1, cv2.IMREAD_UNCHANGED : image as such including alpha channel

# resize image
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# rotate image
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# creates and saves a new image
cv2.imwrite('new_img.jpg', img)

# displays image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()