# tutorial 4
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # drawing lines 
    # cv2.line(source image, starting position, color, thickness)
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)

    # drawing rectangle
    # cv2.rectangle(source image, center position, radius, color, thickness)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)

    # drawing circle
    # cv2.circle(source image, center position, radius, color, thickness)
    # for thickness, -1 means to fill
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)

    # drawing text
    # cv2.putText(source image, text message, center position, font, font scale, color, thickness, type)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Aaron is the goat!', (10, height - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()