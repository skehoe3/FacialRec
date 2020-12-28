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
FOLDER = "/Users/shannonkehoe/Desktop/Git/FacialRec/2017_Portugal"
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

    image = cv2.imread(
        FOLDER + '/' + i)
  #  print(i)
    # Converting to grayscale as opencv expects detector takes in input gray scale images
    test_image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # ; orig
    faces_rects = HAARCC.detectMultiScale(
        test_image_gray)
    face_locations[i] = faces_rects

# ; so this is my "dataset" containing the locations of all faces in the folder.
print(face_locations)

# ; for efficiency, make a subfolder called "faces" and store the faces we found, and ONLY the faces we found, in that location.
# ; this will make it faster to compare the faces later.
