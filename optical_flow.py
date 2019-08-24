import cv2
from subprocess import call
import os
import os.path
import sys

def optical_flow(video_dir):

	vidcap = cv2.VideoCapture(video_dir)
	success,t1 = vidcap.read()

	main_dir = os.path.abspath(os.path.join(video_dir, '..'))

	os.mkdir(main_dir+'/opticalFlow')

	cv2.imwrite(main_dir+"/opticalFlow/t1_0.ppm", t1)
	count = 1

	while success:
		success,t2 = vidcap.read()
		count += 1
		if count%10 == 0:
			cv2.imwrite(main_dir+"/opticalFlow/t2_{}.ppm".format(count), t2)     # save frame as JPEG file
			call('./optical/of {}/opticalFlow/t1_{} {}/opticalFlow/t2_{}'.format(main_dir, count-10, main_dir, count), shell=True)
			os.remove("{}/opticalFlow/t1_{}.ppm".format(main_dir, count-10))
			os.remove("{}/opticalFlow/t1_{}.flo".format(main_dir, count-10))
			os.remove("{}/opticalFlow/t2_{}.ppm".format(main_dir, count))
			cv2.imwrite("{}/opticalFlow/t1_{}.ppm".format(main_dir, count), t2)
			print(count)
	os.remove("{}/opticalFlow/t1_{}.ppm".format(main_dir, count - (count%10)))



def main(add):
	optical_flow(add)

if __name__ == "__main__":
	main(sys.argv[1])
