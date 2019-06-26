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
root_file = "F:/all-mias/"
exel = [["image_path","x_min" , "y_min","x_max", "y_max","class_id"]]
output_file = "F:/mytest/"
f = open("list.txt", "r")        
for line in f:
    new=line.split()       
    print(new)
    imgname = new[0]+'.pgm'
    image = cv2.imread(root_file+imgname)
    imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    x=new[4]
    x = int(x)
    y=new[5]
    y = int(y)
    y=1024-y
    r=new[6]
    r = int(r)
    print(x,y)
    z=x+r
    g=y+r
    if(z>1024):
        z=1024
    if(g>1024):
        g=1024
    b=x-r
    f=y-r
    if(b<1):
        b=1
    if(f<1):
        f=1
    cv2.rectangle(imgray,(z,g),(b,f),(0,255,0),2)
    exel.append([root_file+imgname, b, f, z, g,"1"])

save_to_exel(exel, output_file + "/" + "test1.txt")

