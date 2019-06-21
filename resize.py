import os
import cv2
import numpy as np
from skimage.color import rgb2gray, rgb2hsv
from scipy.misc import imresize
from scipy.misc import imread, imsave
from skimage.exposure import equalize_adapthist


dir_name='F:/IMAGES/faster_RcNN/train_mask/'
dir_out = 'F:/IMAGES/yolo/train_mask/'

counter= 0
for filename in os.listdir(dir_name):
     if filename.endswith(".png"):
        img = cv2.imread(dir_name + filename)
        img = cv2.resize(img, (416,416))
        cv2.imwrite(dir_out+filename, img)
        counter=counter+1
        print (counter)

