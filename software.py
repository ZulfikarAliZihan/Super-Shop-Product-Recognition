import cv2
import sys
import os
image_path = sys.argv[1]
a=cv2.imread(image_path)
cv2.imshow('image',a)
cv2.waitKey(0) 
cv2.destroyAllWindows()