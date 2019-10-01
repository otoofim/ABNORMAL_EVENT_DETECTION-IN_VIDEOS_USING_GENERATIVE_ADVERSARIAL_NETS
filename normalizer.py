import cv2
import numpy as np




class normalize:
    def __init__(self, fra_list):
        self.frames = fra_list
        self.find_max()
        
        
    def find_max(self):
        #vidcap = cv2.VideoCapture(add)
        #success,frame = vidcap.read()
        maxValue = -1
        #frames = []
        for i in range(self.frames.shape[0]):
            #frames.append(frame)
            if np.amax(self.frames[i]) > maxValue:
                maxValue = np.amax(self.frames[i])
            #success,frame = vidcap.read()
        self.maxValue = maxValue
        #self.frames = np.array(frames)
