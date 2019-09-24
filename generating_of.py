import os
import importlib
#importlib.import_module('optical_flow')

from optical_flow import *


def generator(addstr):
    #addstr = '/media/mohammad/2CE86D4BE86D13FC/UCF-Anomaly-Detection-Dataset/UCF_Crimes/Videos/'
    files = os.listdir(addstr)
    add = "/media/mohammad/2CE86D4BE86D13FC/UCF-Anomaly-Detection-Dataset/UCF_Crimes/Videos/Normal_frame_optical/img"
    img_files = open(add,"r+")
    img_names = img_files.read().splitlines()
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
                if not (FILE2.split('.')[0] in img_names):
                    videopath = new_path + "/" + FILE2
                    optical_flow(videopath, dest, 10)
                    img_names.append(FILE2)
                    open(add, "a+").write(FILE2.split('.')[0]+"\n")
                else:
                    print(FILE2.split('.')[0])



def main(addstr):
    generator(addstr)

if __name__ == "__main__":
    main(sys.argv[1])
