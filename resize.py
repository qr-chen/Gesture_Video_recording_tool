# coding:utf-8
import cv2 
import glob

IMG_PATH = './gesture/'
cnt = 1

for img in glob.iglob(IMG_PATH+'*.jpg'):
	im = cv2.imread(img)	
	im = cv2.resize(im, (170, 227))
	cv2.putText(im, '%d' %cnt, (5, 40),   
				cv2.FONT_HERSHEY_COMPLEX,
				1, (0, 255, 0), 4) # 给例图添加标号
	cv2.imwrite(img.split('/')[-1], im)
	cnt += 1
	