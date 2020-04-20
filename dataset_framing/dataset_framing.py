#!/usr/bin/env python
# coding: utf-8

# # Dataset Framing

# Download the Violence/Non violence dataset on [Kaggle](https://www.kaggle.com/mohamedmustafa/real-life-violence-situations-dataset/data).

# In[1]:


import cv2
import os
from ipywidgets import IntProgress
from IPython.display import display


# Set your input/output paths here

# In[7]:


inputDataViolence = "dataset/Violence/"
inputDataNonViolence = "dataset/NonViolence/"
outputDataViolence = "framed_dataset/Violence/"
outputDataNonViolence = "framed_dataset/Non/Violence/"


# Set your image width and height and the total number of videos

# In[9]:


imgX = 224   
imgY = 224
size = (imgX,imgY)
totalVideos = 1001 #total numeber of Videos


# In[10]:


nVideo = 1 #currentVideo
f = IntProgress(min=0, max=totalVideos) # instantiate the ProgressBar
display(f) # display the progressBar
for nVideo in range(totalVideos):
    cap = cv2.VideoCapture(inputDataViolence +"V_"+str(nVideo)+".mp4")
    i = 0
    while(cap.isOpened()):
        ret,frame = cap.read()
        if ret == False:
            break
        resize = cv2.resize(frame,size)
        cv2.imwrite(outputDataViolence +"video"+str(nVideo)+"img"+str(i)+".jpg",resize)
        i+=1
    cap.release()
    cv2.destroyAllWindows()
    nVideo+=1
    f.value+=1


# In[11]:


nVideo = 1 #currentVideo
f = IntProgress(min=0, max=totalVideos) # instantiate the ProgressBar
display(f) # display the progressBar
for nVideo in range(totalVideos): 
    cap = cv2.VideoCapture(inputDataNonViolence +"NV_"+str(nVideo)+".mp4")
    i = 0
    while(cap.isOpened()):
        ret,frame = cap.read()
        if ret == False:
            break
        resize = cv2.resize(frame,size)
        cv2.imwrite(outputDataNonViolence+"video"+str(nVideo)+"img"+str(i)+".jpg",resize)
        i+=1
    cap.release()
    cv2.destroyAllWindows()
    nVideo+=1
    f.value+=1


# In[ ]:




