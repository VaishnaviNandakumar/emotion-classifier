import cv2 
import os 
import math 
# Read the video from specified path 
count = 0
videoFile = "C:\\Users\\ACER\\Desktop\\EmotionDetection\\Dataset\\TestCartoon.mp4"
cap = cv2.VideoCapture(videoFile) # capturing the video from the given path
frameRate = cap.get(5) #frame rate
x=1
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename ="test%d.jpg" % count;    count+=1
        cv2.imwrite(filename, frame)
cap.release()