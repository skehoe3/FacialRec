"""
Author: Shannon Kehoe
Date: December 2020

Experimenting with OpenCV.  Used the DataCamp article as a reference.

https://www.datacamp.com/community/tutorials/face-detection-python-opencv
"""
# base imports
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
# load the file

#!Tiff images need to be converted to a different data type!
FOLDER = "/Users/shannonkehoe/Desktop/Git/FacialRec/test_one"
FILES = [f for f in os.listdir(
    FOLDER) if os.path.isfile(os.path.join(FOLDER, f)) and f != ".DS_Store"]  # filters out the MAC file
HAARCC = cv2.CascadeClassifier(
    'haarcascade_frontalface_alt2.xml')


def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


face_locations = {}
# ; throw this into a function, then throw the function inside of tqdm())
for i in FILES:
    #  Loading the image to be tested
    # print(
    #     FOLDER + '/' + i == "/Users/shannonkehoe/Desktop/Git/FacialRec/test_one/IMG_2078.JPG")
    image = cv2.imread(
        FOLDER + '/' + i)
  #  print(i)
    # Converting to grayscale as opencv expects detector takes in input gray scale images
    test_image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # print(test_image_gray)
    # ; orig
    faces_rects = HAARCC.detectMultiScale(
        test_image_gray)
    face_locations[i] = faces_rects
    print(len(faces_rects))
   # print(faces_rects)
    # #! only for testing!
    # # subset the faces out and save as seperate images.
    # print(faces_rects[1])
    # print(faces_rects[0][0])
    xstart = faces_rects[0][0]
    xstop = xstart + faces_rects[0][2]
    ystart = faces_rects[0][1]
    ystop = ystart + faces_rects[0][3]

    # ; faces_rects --> (x, y, w, h)
    cropped = test_image_gray[xstart:xstop, ystart:ystop]
    cv2.imwrite('face.png',
                convertToRGB(cropped))
# ; so this is my "dataset" containing the locations of all faces in the folder.
# print(face_locations)

# ; for efficiency, make a subfolder called "faces" and store the faces we found, and ONLY the faces we found, in that location.
# ; this will make it faster to compare the faces later.
