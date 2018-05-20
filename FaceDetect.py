import cv2
import os
import time
cap = cv2.VideoCapture(0)
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
if not cap.isOpened():
    print("Cannot open webcam")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("Faces",frame)

    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
        
    
   
cap.release()
cv2.destroyAllWindows()
