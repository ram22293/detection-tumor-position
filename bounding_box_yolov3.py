import numpy as np
import cv2
import os
import csv

def save_to_exel(lists, filename):
    if os.path.isfile(filename):
        os.remove(filename)
    with open(filename, 'a') as csvfile:
        fwriter = csv.writer(csvfile, delimiter=',',lineterminator='\n')
        fwriter.writerows(lists)
        csvfile.close()


root_file = "H:/train_mask/"
#exel = [["image_path","x_min" , "y_min","x_max", "y_max","class_id"]]
output_file = "H:/tensorflow-yolov3-master/data/dataset/"
counter = 1

for directory, subdirectories, files in os.walk(root_file):
    for file in files:
        name = os.path.splitext(file)[0]
        ext = os.path.splitext(file)[1]
        img = os.path.join(directory, file)
        print (counter)
        counter = counter+1
        im = cv2.imread(img)
        imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,127,255,0)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        areas = [cv2.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        cnt=contours[max_index]
        x,y,w,h = cv2.boundingRect(cnt)
        #cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
        #cv2.imshow("test",im)
        #cv2.waitKey(0)
        #exel.append([name, x, y, w, h])
        w=w+x
        h=y+h
        exel.append([root_file+name,x, y, w, h,"1"])

save_to_exel(exel, output_file + "/" + "voc_train.txt")
