import cv2#Importing the libraries

cap = cv2.VideoCapture(0)# Making an object of VideoCapture

while True:
    _, img = cap.read()# Read in the current frame
    cv2.imshow('img',img)# Displaying the frame
    if cv2.waitKey(10) & 0xFF ==ord(' '):# While the spacebar is not pressed, the feed will continue
        break

cap.release()
cv2.destroyAllWindows()# Destroys all windows
