import sys
import cv2
from colordetection import ColorDetector
import os
import sys
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(10, 200)
a= cap.get(10)
print(a)
while(True):
    ret, img = cap.read()
    a= cap.get(10)
    print(a)
    cv2.imshow("input", img)
    key = cv2.waitKey(10)
    if key == 27:
        break
cv2.destroyAllWindows()
cv2.VideoCapture(0).release()
