import cv2
import os
from ipywidgets import IntProgress
from IPython.display import display

def get_frames(inputpath, outputpath):
    
    imgX = 224   
    imgY = 224
    size = (imgX,imgY)
    nFrame = 0
    cap = cv2.VideoCapture(inputpath)
    while(cap.isOpened()):
        ret,frame = cap.read()
        if ret == False:
            break
        resize = cv2.resize(frame,size)
        cv2.imwrite(outputpath +"img"+str(nFrame)+".jpg",resize)
        nFrame+=1
    cap.release()
    cv2.destroyAllWindows()
    return nFrame
    