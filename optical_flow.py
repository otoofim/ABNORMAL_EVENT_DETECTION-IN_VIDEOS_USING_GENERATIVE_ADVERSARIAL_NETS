import cv2
from subprocess import call
import os
import os.path
import sys
import numpy as np

def optical_flow(video_dir, dest_add, skip_frames=10):


	skip_frames = int(skip_frames)
	video_name = video_dir.split('/')[-1].split('.')[0]


	main_dir = os.path.abspath(os.path.join(video_dir, '..'))
	#main_dir = os.path.abspath(os.path.join(main_dir, '..'))
	main_dir = os.path.abspath(os.path.join(main_dir, '..'))
	main_dir = main_dir + '/Normal_frame_optical'

	print(video_name)

	if not (os.path.exists(main_dir)):
		os.mkdir(main_dir)
	if not (os.path.exists(main_dir+'/'+dest_add)):
		os.mkdir(main_dir+'/'+dest_add)

	main_dir = main_dir+'/'+dest_add



	vidcap = cv2.VideoCapture(video_dir)
	success,t1 = vidcap.read()
	if success:
		t1 = cv2.resize(t1, (256,256), interpolation = cv2.INTER_AREA)
		count = 0
		cv2.imwrite(main_dir+"/t1.ppm", t1)



	while success:

		success, t2 = vidcap.read()

		if success:

			t2 = cv2.resize(t2, (256,256), interpolation = cv2.INTER_AREA)
			cv2.imwrite(main_dir+"/t2.ppm", t2)
			count += 1

		if (count%skip_frames == 0) and (not(os.path.exists("{}/{}_{}.jpg".format(main_dir, video_name, count-skip_frames)))) and (success):



			call('./optical/of {}/t1 {}/t2'.format(main_dir, main_dir), shell=True)
			im_AB = np.concatenate([cv2.imread('{}/t1.ppm'.format(main_dir), 1), cv2.imread("{}/t1Flow.ppm".format(main_dir), 1)], 1)
			os.remove("{}/t1.flo".format(main_dir))
			os.remove("{}/t1.ppm".format(main_dir))
			os.rename("{}/t2.ppm".format(main_dir), "{}/t1.ppm".format(main_dir))
			os.remove("{}/t1Flow.ppm".format(main_dir))

			cv2.imwrite("{}/{}_{}.jpg".format(main_dir, video_name, count-skip_frames), im_AB)

		elif (os.path.exists("{}/{}_{}.jpg".format(main_dir, video_name, count-skip_frames))) and success:
			os.remove("{}/t1.ppm".format(main_dir))
			os.rename("{}/t2.ppm".format(main_dir), "{}/t1.ppm".format(main_dir))
		#print(count)

	if (os.path.exists("{}/t1.ppm".format(main_dir))):
		os.remove("{}/t1.ppm".format(main_dir))
	if (os.path.exists("{}/t2.ppm".format(main_dir))):
		os.remove("{}/t2.ppm".format(main_dir))


# def main(add, dest_add, skip_frames):
#   	optical_flow(add, dest_add, skip_frames)
#
# if __name__ == "__main__":
#   	main(sys.argv[1], sys.argv[2], sys.argv[3])
