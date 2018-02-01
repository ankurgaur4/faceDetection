import os
import cv2
import time
faceDetect = cv2.CascadeClassifier('openCV_files\haarcascade_frontalface_default.xml');
data_folder_path = "training-data"
dirs = os.listdir(data_folder_path)
for dir_names in dirs:
        
       subject_dir_path = data_folder_path + "/" + dir_names
       subject_images_names = os.listdir(subject_dir_path)
       for image_name in subject_images_names:
                    if image_name.startswith("."):
                            continue;
                    image_path = subject_dir_path + "/" + image_name
                    image = cv2.imread(image_path)
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    print(image_name)
                    faces = faceDetect.detectMultiScale(gray,1.3,5);
                    for(x,y,w,h) in faces:
                            
                              cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
                              cv2.imshow("Faces",image)
                              print("yes")
                              cv2.waitKey(2000)
                              cv2.destroyAllWindows()
 


   
   


        
