import cv2
import numpy as np
#detect face
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
#detect eyes
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#video capture from camera
cap=cv2.VideoCapture(0)
#jb tk camera chlega
while cap.isOpened():
#captured image ko read kiya
    status,img=cap.read()
#transparency of image bnaayi
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#detect multiple fACES
    faces = face_cascade.detectMultiScale(gray,1.3,5)
#coordinates for rectangle
    for(x,y,s,p) in faces:
#img, dimensions(start,end) , colour , width of edges
        cv2.rectangle(img,(x,y),(x+s,y+p),(0,0,255),2)
#region of image ko gray mein chnage kia 
        roi_gray=gray[y:y+p, x:x+s]
#transparent image mein colour daala
        roi_color=img[y:y+p, x:x+s]
#detect multiple eyes
        eyes=eyes_cascade.detectMultiScale(roi_gray)
        for(ex,ey,es,ep) in eyes:
         	cv2.rectangle(roi_color,(ex,ey),(ex+es,ey+ep),(255,0,0),2)
#to show image		
    cv2.imshow('img',img)
#to hold image on window
    k = cv2.waitKey(30)

    if (k ==27):
           break
 #releasing all resources    
cap.release()
cv2.destroyAllWIndow()


