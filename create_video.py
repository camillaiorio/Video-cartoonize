#!/usr/bin/env python
import cv2
import os
import numpy as np
import glob
import sys

if(len(sys.argv) < 2):
     exit (-1);
input_folder = sys.argv[1]

img_array=[]
image_files = input_folder+"/*.jpg"


list_of_files = sorted( glob.glob(image_files) )
for filename in list_of_files:
        img=cv2.imread(filename)
        height, width, layers= img.shape
        size= (width, height)
        img_array.append(img)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(* 'DIVX'), 30,size)

for i in range(len(img_array)):
    out.write(img_array[i])

out.release()

exit(0);