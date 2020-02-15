import cv2
import serial
import time
import msvcrt
from threading import *

serialComm = serial.Serial('COM3',9600)
serialComm.timeout=1

import Object_detection_image

from tkinter import *
import os
root= Tk()
total_price=0
def takePhoto():
    cap = cv2.VideoCapture('http://192.168.43.1:8080/video')
    #cap = cv2.VideoCapture(0)
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    cv2.imshow('frame',frame)

    cv2.imwrite("a.jpg",frame)
    li=os.popen('python C:\\tensorflow1\\models\\research\\object_detection\\Object_detection_image.py',"r")
    # When everything done, release the capture  
    
    cap.release()
    cv2.destroyAllWindows()
    #textView.delete(0.0,'end')

    
    while 1:
        global total_price
        line=li.readline()
        if not line:
            break
        print("a"+line+"a")
        #print(type(line))
        if line.strip().isdigit():
            total_price+=int(line)
        else:
            textView.insert(0.0,line)


def stateChange():
    while 1:
        if msvcrt.kbhit():
            if ord(msvcrt.getch()) == 27:
                break
        fromBoard=serialComm.readline().decode('ascii').strip()
        print("a"+fromBoard+"a")
        if fromBoard=="product":
            print("Taking Photo")
            time.sleep(0.5)
            takePhoto()
            
            i="run"
            serialComm.write(i.encode())
    
            #textView.delete(0.0,'end')
            #textView.insert(0.0,"Total patable: "+total_price)
            #break

    serialComm.close()
    print("end of while")

t1=Thread(target=stateChange)
t1.start()

def total():
     #textView.delete(0.0,'end')
     textView.insert(0.0,"  Total patable: "+str(total_price)+"\n")

def closeAll():
    textView.delete(0.0,'end')
    #t1.stop()
    global total_price
    total_price=0

root.geometry("300x350")

appName=Label(root,text="Super Shop Product Teacker")
appName.grid(row=1,sticky=E)
btn=Button(root,text="New/Clear",bg='gray',fg='black',command=closeAll)
btn.grid(row=1)
btn=Button(root,text="Total",bg='gray',fg='black',command=total)
btn.grid(row=2)
textView=Text(root,width=50,height=35)
textView.grid(row=3,columnspan=2,sticky=W)
root.mainloop()
