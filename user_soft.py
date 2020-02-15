

# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys


import serial
import time
import msvcrt
from threading import *
serialComm = serial.Serial('COM3',9600)
serialComm.timeout=1
from tkinter import *
import os
root= Tk()
total_price=0


sys.path.append("..")

# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util



MODEL_NAME = 'inference_graph'
IMAGE_NAME = 'a.jpg'


CWD_PATH = os.getcwd()


PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')


PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')


PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)


NUM_CLASSES = 6


label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Load the Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)


image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

ed
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

num_detections = detection_graph.get_tensor_by_name('num_detections:0')


image = cv2.imread(PATH_TO_IMAGE)
image_expanded = np.expand_dims(image, axis=0)



 
def takePhoto():
    cap = cv2.VideoCapture('http://192.168.43.1:8080/video')
    #cap = cv2.VideoCapture(0)
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    #cv2.imshow('frame',frame)
    #time.sleep(0.5)
    cv2.imwrite("a.jpg",frame)
    image = cv2.imread('C:\\tensorflow1\\models\\research\\object_detection\\a.jpg')
    image_expanded = np.expand_dims(image, axis=0)
    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: image_expanded})
    
    img,class_name=vis_util.visualize_boxes_and_labels_on_image_array(
        image,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8,
        min_score_thresh=0.80)

    global total_price
    for name in class_name:
        if name=='Chocolate-Cake':
            #print(name+"- 10 taka")
            textView.insert(0.0,name+"- 10 taka\n")
            total_price+=10
        elif name=='pops-biscuits':
            #print(name+"- 5 taka")
            textView.insert(0.0,name+"- 5 taka\n")
            total_price+=5
        elif name=='Toothpaste':
                #print(name+"- 35 taka")
                textView.insert(0.0,name+"- 35 taka\n")
                total_price+=35
        elif name=='Multimeter':
                #print(name+"- 200 taka")
                textView.insert(0.0,name+"- 200 taka\n")
                total_price+=200
        else:
            print("none")
    #print("Total payable = "+str(total_price)+" taka only.")
    print(total_price)
    
    cv2.imshow('Object detector', img)

    
    cv2.waitKey(1000)

    
    cv2.destroyAllWindows()



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

def state():
    global total_price
    total_price=0
    textView.delete(0.0,'end')
    


def total():
     #textView.delete(0.0,'end')
     textView.insert(0.0,"Total patable: "+str(total_price)+"\n")



root.geometry("300x350")

appName=Label(root,text="")
appName.grid(row=1,sticky=E)
btn=Button(root,text="Take Photo",bg='ivory3',fg='black',command=state)
btn.grid(row=1)
btn=Button(root,text="Total",bg='ivory3',fg='black',command=total)
btn.grid(row=2)
textView=Text(root,width=50,height=35)
textView.grid(row=3,columnspan=2,sticky=W)
root.mainloop()
