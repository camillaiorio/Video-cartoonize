#!/usr/bin/env python
import cv2
import os
import sys


#print 'Argument List:', str(sys.argv)
if(len(sys.argv) < 3):
    exit (-1);
vid = sys.argv[1]
input_folder = sys.argv[2]
print("elaboro video ", vid, "e scrivo i frame in ", input_folder)

#/home/biar/video_cartoonize/create_frames.py

# /home/biar/video_cartoonize/Video/video_fiore_farfalla.mp4
vidcap = cv2.VideoCapture(vid)
success,image = vidcap.read()

os.system("rm -f  "+ input_folder +"/*.jpg");

count=0
while success:
    cv2.imwrite(input_folder+"/frame%00005d.jpg" % count,image) #save frame as JPEG file
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1

print('sono stati creati i  frame')

exit(0);