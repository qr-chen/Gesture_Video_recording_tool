# coding=utf-8
import cv2
import os 
import glob	

GESTURE_PATH = '..\\gesture\\' # 手势例图地址 *.jpg
VIDEO_PATH = '..\\video_saved\\' # 视频地址
EXTRACT_FREQUENCY = 3 # 帧提取频率


def extract_frames(video_path, dst_folder, video_name, index, drop_frame=0):
    video = cv2.VideoCapture()
    if not video.open(video_path):
        print("can not open the video")
        exit(1)
    count = 1
	
    for i in range(drop_frame): # 为保证数据质量，丢弃视频开始的帧数
        _, frame = video.read()
		
    while True:
        _, frame = video.read()
        if frame is None:
            break
        if count % EXTRACT_FREQUENCY == 0:
            save_path = '{}/{}_{:>03d}.jpg'.format(dst_folder, video_name, index)
            cv2.imwrite(save_path, frame)
            index += 1
        count += 1
    video.release()  
    print('{} Totally save {:d} pics'.format(video_name, index-1)) # 打印出所提取帧的总数


def main():
	gesture_lst = []
	for img in os.listdir(GESTURE_PATH):
		gesture_lst.append(img.split('.jpg')[0]) #读取手势名
	video_lst = os.listdir(VIDEO_PATH)
	for video in video_lst:
		for gesture_name in gesture_lst:
			if video.split('_')[1] == gesture_name:
				save_path = gesture_name + '\\'
				if not os.path.exists(save_path): #保存路径在当前目录下，根据手势名新建文件夹。
					os.mkdir(save_path)
				video_name = video.split('.avi')[0]
				extract_frames(VIDEO_PATH+video, save_path, video_name, 1, drop_frame=15)
			

if __name__ == '__main__':
    main()