import cv2
import serial
import time
serialComm = serial.Serial('COM6',9600)
serialComm.timeout=1

cap = cv2.VideoCapture('http://192.168.43.1:8080/video')
# Capture frame-by-frame


count = 0
# Display the resulting frame
#cv2.imshow('frame',frame)


for j in range(1,10):
    ret, frame = cap.read()
    #fromBoard=serialComm.readline().decode('ascii').strip()
    #print("a"+fromBoard+"a")
    print(j)
    i="ok"
    serialComm.write(i.encode())
    time.sleep(2)
    print("Taking Photo")
    cv2.imwrite("C:\\tensorflow1\\models\\research\\object_detection\\taken_photo\\a"+str(j)+".jpg",frame)



    



'''
import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):c
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("C:\\tensorflow1\\models\\research\\object_detection\\taken_photo\\a.jpg",frame)
        #break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
'''