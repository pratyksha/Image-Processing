# import libraries
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    edges = cv2.Canny(img, 100, 200) # apply canny edge detection 
    print(edges)
    cv2.imshow('edges', edges)
    if cv2.waitKey(1)&0xFF == ord('q'): # quit if q is pressed
        break
cap.release()
cv2.destroyAllWindows()
