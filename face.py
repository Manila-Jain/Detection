import cv2
import numpy as np

cap=cv2.VideoCapture(0)
face_cas=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
#eye_cas=cv2.CascadeClassifier('')
while cap.isOpened():
	status,img= cap.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=face_cas.detectMultiScale(gray,1.3,5)
	#eyes=
	for (x,y,z,w) in faces:
		cv2.rectangle(img,(x,y),(x+z,y+w),(255,0,0),2)
		roi_gray=gray[y:y+w,x:x+z]
		roi_color=img[y:y+w,x:x+z]
	cv2.imshow('img',img)
	k=cv2.waitKey(30) 
	if k==27:
		break

cv2.release()
cv2.destroyAllWindow()
