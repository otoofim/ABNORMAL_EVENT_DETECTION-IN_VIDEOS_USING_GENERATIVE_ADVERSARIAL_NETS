import os
import importlib
#importlib.import_module('optical_flow')

from optical_flow import *


def generator(addstr):
    #addstr = '/media/mohammad/2CE86D4BE86D13FC/UCF-Anomaly-Detection-Dataset/UCF_Crimes/Videos/'
    files = os.listdir(addstr)
    Database = []
    dest = ''
    for FILE in files:
        if FILE in ['Normal_Videos_event', 'Training_Normal_Videos_Anomaly','Testing_Normal_Videos_Anomaly']:
            if FILE == "Training_Normal_Videos_Anomaly":
                dest = "train"
            elif FILE == "Testing_Normal_Videos_Anomaly":
                dest = 'test'
            else:
                dest = "val"
            new_path = addstr + FILE
            files2 = os.listdir(new_path)
            for FILE2 in files2:
                #if not (FILE2 in ['fo']):
                videopath = new_path + "/" + FILE2
                optical_flow(videopath, dest, 10)
                #print(videopath)



def main(add):
   	optical_flow(add)

if __name__ == "__main__":
   	main(sys.argv[1])
