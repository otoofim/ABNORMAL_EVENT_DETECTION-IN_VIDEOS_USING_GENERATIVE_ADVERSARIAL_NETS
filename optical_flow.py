import cv2
from subprocess import call
import os
import os.path
import sys

def optical_flow(video_dir, skip_frames):

	skip_frames = int(skip_frames)
	video_name = video_dir.split('/')[-1].split('.')[0]
	vidcap = cv2.VideoCapture(video_dir)
	success,t1 = vidcap.read()
	#t1 = cv2.resize(t1, (256,256), interpolation = cv2.INTER_AREA)


	main_dir = os.path.abspath(os.path.join(video_dir, '..'))

	os.mkdir(main_dir+'/opticalFlow')
	os.mkdir(main_dir+'/frames')


	cv2.imwrite(main_dir+"/frames/t1_0.ppm", t1)
	count = 0

	while success:
		success, t2 = vidcap.read()
		if success:
			#t2 = cv2.resize(t2, (256,256), interpolation = cv2.INTER_AREA)
			pass
		count += 1
		if count%skip_frames == 0:
			cv2.imwrite(main_dir+"/frames/t2_{}.ppm".format(count), t2)
			call('./optical/of {}/frames/t1_{} {}/frames/t2_{}'.format(main_dir, count-skip_frames, main_dir, count), shell=True)
			os.rename("{}/frames/t1_{}.ppm".format(main_dir, count-skip_frames), "{}/frames/{}_{}.ppm".format(main_dir, video_name, count-skip_frames))
			os.rename("{}/frames/t1_{}Flow.ppm".format(main_dir, count-skip_frames), "{}/opticalFlow/{}_{}_Flow.ppm".format(main_dir, video_name, count-skip_frames))
			os.remove("{}/frames/t1_{}.flo".format(main_dir, count-skip_frames))
			os.rename("{}/frames/t2_{}.ppm".format(main_dir, count), "{}/frames/{}_{}.ppm".format(main_dir, video_name, count))
			cv2.imwrite("{}/frames/t1_{}.ppm".format(main_dir, count), t2)
			#print(count)
	os.remove("{}/frames/t1_{}.ppm".format(main_dir, count - (count%skip_frames)))



# def main(add, skip_frames):
# 	optical_flow(add, skip_frames)
#
# if __name__ == "__main__":
# 	main(sys.argv[1], sys.argv[2])
