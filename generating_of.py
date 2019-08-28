import os
import importlib
#importlib.import_module('optical_flow')

from optical_flow import *

addstr = 'F:/UCF-Anomaly-Detection-Dataset/UCF_Crimes/Videos/'
files = os.listdir(addstr)
Database = []
for FILE in files:
    if FILE in ['Normal_Videos_event', 'Training_Normal_Videos_Anomaly','Testing_Normal_Videos_Anomaly']:
        new_path = addstr + FILE
        files2 = os.listdir(new_path)
        for FILE2 in files2:
            if not (FILE2 in ['frames', 'opticalFlow']):
                videopath = new_path + "/" + FILE2
                optical_flow(videopath,1)
                #print(videopath)
