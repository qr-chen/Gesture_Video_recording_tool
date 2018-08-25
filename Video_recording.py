# coding:utf-8
import os 
import cv2 
import time 

gesture_path = './gesture/'
#video_saved_path = './'
video_saved_path = './video_saved/'

def main():
	gesture_lst = os.listdir(gesture_path)
	gesture_len = len(gesture_lst)
	cnt = 0
	

	 
	
	while cnt != gesture_len :
		img = cv2.imread(gesture_path + gesture_lst[cnt])
		cv2.imshow('demo_gesture',img)
		
		
		
		while True:
			 
			key = cv2.waitKey(1) & 0xFF 
			if key == ord(' '):
				
				tic = time.time()
				cap0 = cv2.VideoCapture(0)  #调用笔记本摄像头，正前方
				cap1 = cv2.VideoCapture(1)  #调用左边柱摄像头    相对于录制人员
				cap2 = cv2.VideoCapture(2)  #调用中控台（靠右）摄像头
				cap3 = cv2.VideoCapture(3)  #调用右边柱（垫高）摄像头
				
				
				
				#fourcc = cv2.VideoWriter_fourcc(*"MPEG")
				#fourcc = cv2.VideoWriter_fourcc(*'mp4v')
				
				out0 = cv2.VideoWriter(video_saved_path + str(tic) + '_' + gesture_lst[cnt].split('.jpg')[0]+ '_view0'+'.avi', 1,20.0,(640,480))   
				out1 = cv2.VideoWriter(video_saved_path + str(tic) + '_' + gesture_lst[cnt].split('.jpg')[0]+ '_view1'+'.avi', 1,20.0,(640,480)) 
				out2 = cv2.VideoWriter(video_saved_path + str(tic) + '_' + gesture_lst[cnt].split('.jpg')[0]+ '_view2'+'.avi', 1,20.0,(640,480))   
				out3 = cv2.VideoWriter(video_saved_path + str(tic) + '_' + gesture_lst[cnt].split('.jpg')[0]+ '_view3'+'.avi', 1,20.0,(640,480)) 
				#out = cv2.VideoWriter('1.mp4', fourcc,20.0,(640,480),True)
				

				while True:
					ret0,frame0 = cap0.read()     ##开始录制
					ret1,frame1 = cap1.read()
					ret2,frame2 = cap2.read()     ##开始录制
					ret3,frame3 = cap3.read()
					if ret0==ret1==ret2==ret3 == True:
						frame0 = cv2.flip(frame0, 1)
						frame1 = cv2.flip(frame1, 1)
						frame2 = cv2.flip(frame2, 1)
						frame3 = cv2.flip(frame3, 1)
						# 在帧上进行操作
						# gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
						# 开始保存视频 
						out0.write(frame0)
						out1.write(frame1)
						out2.write(frame2)
						out3.write(frame3)
						# 显示结果帧
						cv2.namedWindow('VideoWindow0')
						frame0_ = cv2.resize(frame0,(320,240))
						cv2.imshow('VideoWindow0', frame0_)
						
						cv2.namedWindow('VideoWindow1')
						frame1_ = cv2.resize(frame1,(320,240))
						cv2.imshow('VideoWindow1', frame1_)
						
						cv2.namedWindow('VideoWindow2')
						frame2_ = cv2.resize(frame2,(320,240))
						cv2.imshow('VideoWindow2', frame2_)
						
						cv2.namedWindow('VideoWindow3')
						frame3_ = cv2.resize(frame3,(320,240))
						cv2.imshow('VideoWindow3', frame3_)
					else :
						print "capture get failed"
						exit(1)
					
						
					if cv2.waitKey(1) & 0xFF == ord(' '):
						cap0.release()
						out0.release()
						cap1.release()
						out1.release()		
						cap2.release()
						out2.release()
						cap3.release()
						out3.release()							
						
						##结束录制
						break
						
			elif key == ord('n'):	#下一个手势
				cnt += 1
				break
			elif key == ord('p'):	#上一个手势 删除上个视频
				video_lst = os.listdir(video_saved_path)
				latest_video_name = sorted(video_lst)[-4:]
				for video in latest_video_name:
					os.remove(video_saved_path + video)
				cnt -= 1
				break
			elif key == ord('q'):
				cv2.destroyAllWindows()
				exit()
			else :
				pass

			
				
		
		if cnt == gesture_len:
			cnt = 0
		if cnt == -1:
			cnt = gesture_len - 1

			
			


if __name__ == '__main__':
	main()