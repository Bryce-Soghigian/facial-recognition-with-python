import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import os
import sys


#Initalizing our camera object
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 30 

rawCapture = PiRGBArray(camera,size=(640,480))
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

name = input("What is the name of the user boi")

dirName= "./images/"+ name
print(dirName)
if not os.path.exists(dirName):
    os.makedirs(dirName)
    print("Directory Created")
else:
    print("Name Already Exists")
    sys.exit()

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame = frame.array
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
