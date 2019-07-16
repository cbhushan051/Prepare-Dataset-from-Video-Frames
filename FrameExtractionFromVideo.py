#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:39:44 2019

@author: chandra
"""

'''
You can create your own dataset by extracting frames from the video.
Also labels will be given on the basis of the video name for example:
If the video name is human.mp4 then it will automatically create folder human 
if the human folder does not exist and you can use it as label while training your model
'''
import cv2
import os
#####Listing the video files
from os import listdir
from os.path import isfile, join
mypath= "Webcam/"   #Path to your video folder
fileslist = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for video_name in fileslist:
    #video_name = 'sample2.mp4'
    video_name = mypath+video_name
    
    vid_frame_path = video_name.split(".")[0]
    
    if not os.path.exists(vid_frame_path):
        os.makedirs(vid_frame_path)
        
    vidcap = cv2.VideoCapture(video_name)
    
    success,image = vidcap.read()
    
    count = 0
    
    success = True
    
    while success:
        success,image = vidcap.read()
        cv2.imwrite(vid_frame_path+"/frame%d.jpg" % count, image)   # save frame as JPEG file
        if cv2.waitKey(10) == 27:        # exit if Escape is hit
            break
        count += 1
        
'''
Congratulations! You have created your own dataset from scratch
'''
  
  
  

  