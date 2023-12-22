#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Mon Dec 12 18:57:26 2022

@author: gulsumirembas
"""

import cv2 as cv
import numpy as np
import time as tm
import module as m
import serial

COUNTER =0
CLOSED_EYE_FRAME = 5
cameraID = 0
camera = cv.VideoCapture(cameraID)

# add the following lines to initialize the serial connection
bluetoothSerial = serial.Serial( "COM9", baudrate=9600, timeout=1 )
bluetoothSerial.flushInput()
bluetoothSerial.close()
bluetoothSerial.open()
bluetoothSerial.write(b'1')

# define the commands that will be sent to the Arduino
#CMD_LEFT = "left"
#CMD_RIGHT = "right"
#CMD_FORWARD = "forward"  # add this line to define the forward command
#CMD_STOP = "stop"


while True:
    
    ret,frame = camera.read()
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    image,face = m.faceDetector(frame , grayFrame)

    



    if face is not None:
        image, landmarks_list = m.faceLandmarkDetector(frame,grayFrame,face,False)
        
        Right_eye = landmarks_list[36:42]
        Left_eye = landmarks_list[42:48]
        
        right_ratio ,topMid_rigth,bottomMid_rigth =m.close_eye(Right_eye)
        left_ratio ,topMid_left,bottomMid_left =m.close_eye(Left_eye)
        
        blinkRaito = (left_ratio+right_ratio)/2
        if bluetoothSerial.isOpen():
            if blinkRaito > 4:
                cv.putText(image, f'closed', (50,50),m.fonts, 1, m.RED, 2)
                bluetoothSerial.write(b'q')
                print("sent stop command")
                # send a command to the Arduino to go right
                #if topMid_left[0] > topMid_rigth[0]:
                #    bluetoothSerial.write(b'a')
                #    print("sent right command")
                #else:
                #    bluetoothSerial.write(b'd')
                #    print("sent left command")
                #tm.sleep(1)
            else:
                #print("closed eyes")
                cv.putText(image, f'opened', (50,20),m.fonts, 1, m.RED, 2)
                # send a command to the Arduino to stop
                #bluetoothSerial.write(b'w')
                #print("sent forward command")
                # send a command to the Arduino to go forward
                mask , pos = m.eyeTracking(frame, grayFrame, Right_eye)
                maskleft, leftpos = m.eyeTracking(frame, grayFrame, Left_eye)
                #cv.imshow('mask', mask)
                #cv.imshow('threshold', thresh_eye)
                #cv.imshow('eyeImage', eyeImage)
                if pos == 'Center':
                    bluetoothSerial.write(b'w')
                elif pos == 'Right':
                    bluetoothSerial.write(b'd')
                elif pos == 'Left':
                    bluetoothSerial.write(b'a')
        
        for i in Right_eye:
            cv.circle(image, i, 3,m.RED,1)
        for i in Left_eye:
            cv.circle(image, i, 3,m.RED,1)
        
        
            cv.imshow('Frame', image)
    else:
        cv.imshow('Frame', frame)
        bluetoothSerial.write(b'q')
    
    
    
    
    key =cv.waitKey(1)
    if key == ord('q'):
        bluetoothSerial.write(b'q')
        bluetoothSerial.close()
        break
    
camera.release()
cv.destroyAllWindows()