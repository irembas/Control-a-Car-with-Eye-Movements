#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:36:07 2022

@author: gulsumirembas
"""
import cv2 as cv
import numpy as np
import dlib
import math


YELLOW = (0, 247, 255)
CYAN = (255, 255, 0)
MAGENTA = (255, 0, 242)
GOLDEN = (32, 218, 165)
LIGHT_BLUE = (255, 9, 2)
PURPLE = (128, 0, 128)
CHOCOLATE = (30, 105, 210)
PINK = (147, 20, 255)
ORANGE = (0, 69, 255)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 255, 13)
LIGHT_CYAN = (255, 204, 0)
BLUE = (255, 0, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_RED = (2, 53, 255)

fonts = cv.FONT_HERSHEY_COMPLEX
detected_face = dlib.get_frontal_face_detector()

predictor= dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def midPoint(pts1, pts2):
    x, y = pts1
    x1, y1 = pts2
    xOut = int((x + x1)/2)
    yOut = int((y1 + y)/2)
    return (xOut, yOut)

def euclidianDistance(pts1, pts2):
    x, y = pts1
    x1, y1 = pts2
    euclidianDist = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    return euclidianDist

def faceDetector(image,gray, Draw = True):
    face1_coordinate = (0,0)
    face2_coordinate =(0,0)
    
    faces = detected_face(gray)
    
    face =None
    
    for face in faces:
        face1_coordinate = (face.left(), face.top())
        face2_coordinate = ( face.right(), face.bottom())
        if Draw ==True:
            cv.rectangle(image, face1_coordinate, face2_coordinate, RED, 2)        
    return image,face

def faceLandmarkDetector(image, gray, face, Draw = True):
    
    landmarks = predictor(gray, face)
    landmarks_list =[]
    
    for i in range(0,68):
        point = (landmarks.part(i).x, landmarks.part(i).y)
        landmarks_list.append(point)
        
        if Draw == True:
            cv.circle(image, point, 3 , RED, 2)
            
    return image, landmarks_list
            
def close_eye(eye_point):
    top = eye_point[1:3]
    bottom = eye_point[4:6]
    
    topMid = midPoint(top[0], top[1])
    bottomMid = midPoint(bottom[0], bottom[1])

    
    verticalDistance = euclidianDistance(topMid, bottomMid)
    horizontalDistance = euclidianDistance(eye_point[0], eye_point[3])
    blinkRatio = (horizontalDistance/verticalDistance)
    return blinkRatio, topMid, bottomMid

def eyeTracking(image, gray, eye_point):
    dim = gray.shape
    mask = np.zeros(dim , dtype= np.uint8)
    
    dim_points = np.array(eye_point, dtype=np.int32)
    cv.fillPoly(mask, [dim_points], 255)
    eyeImage = cv.bitwise_and(gray, gray,mask=mask)
    
    maxX = (max(eye_point, key=lambda item: item[0]))[0]
    minX = (min(eye_point, key=lambda item: item[0]))[0]
    maxY = (max(eye_point, key=lambda item: item[1]))[1]
    minY = (min(eye_point, key=lambda item: item[1]))[1]
    
    eyeImage[mask==0]=255
    
    croppedEye = eyeImage[minY:maxY, minX:maxX]
    
    height, width = croppedEye.shape
    divPart = int(width/3)
    
    ret,thresholdEye = cv.threshold(croppedEye,100,255,cv.THRESH_BINARY)
    
    rightPart = thresholdEye[0:height, 0:divPart]
    centerPart = thresholdEye[0:height, divPart:divPart+divPart]
    leftPart = thresholdEye[0:height, divPart+divPart:width]
    
    #counting the black pixels in eyes part:
    rightBlackpx = np.sum(rightPart==0)
    centerBlackpx = np.sum(centerPart==0)
    leftBlackpx = np.sum( leftPart==0)
    pos = Position([rightBlackpx, centerBlackpx, leftBlackpx])
    print(pos)
    return mask, pos
            
def Position(ValuesList):

    maxIndex = ValuesList.index(max(ValuesList))
    posEye = ''
    if maxIndex == 0:
        posEye = "Right"
    elif maxIndex == 1:
        posEye = "Center"
    elif maxIndex == 2:
        posEye = "Left"
    else:
        posEye = "Eye Closed"
    return posEye