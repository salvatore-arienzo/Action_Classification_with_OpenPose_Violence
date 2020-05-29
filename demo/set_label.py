import cv2
import os

def set_label(predictions):
    
    count=0
    for pred in predictions:
        if pred==0:
            count=count+1
    
    if ((100 * count ) / len(predictions) >= 20):
        return print ('\033[1m \033[91m \033[5m' +  "Label: Violence" + '\033[0m')
    else: 
        return print ('\033[3m \033[92m \033[5m' +  "Label: Non Violence" + '\033[0m')

    