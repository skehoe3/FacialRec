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
import uuid
# load the file

#!Tiff images need to be converted to a different data type!
SOURCE_FOLDER = "/Users/shannonkehoe/Desktop/Git/FacialRec/test_one"
FILES = [f for f in os.listdir(
    SOURCE_FOLDER) if os.path.isfile(os.path.join(SOURCE_FOLDER, f)) and f != ".DS_Store"]  # filters out the MAC file
HAARCC = cv2.CascadeClassifier(
    'haarcascade_frontalface_alt2.xml')


def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def crop(narray, image):
    """
    Takes a single numpy array of x,y,w,h and selects only that area from the image. 
    Args:
        narray (numpy array): a numpy array of x-coord,y-coord,width,height 
        image ([type]): numpy array representation of an image

    Returns:
        numpy array: subset of the input image
    """
    xstart = faces_rects[0][0]
    xstop = xstart + faces_rects[0][2]
    ystart = faces_rects[0][1]
    ystop = ystart + faces_rects[0][3]
    return image[xstart:xstop, ystart:ystop]


face_locations = {}
# ; throw this into a function, then throw the function inside of tqdm())
for i in FILES:
    image = cv2.imread(SOURCE_FOLDER + '/' + i)
    test_image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces_rects = HAARCC.detectMultiScale(
        test_image_gray)
    imname = i.split(".")[0]
    # ; loopd crops
    for row in range(0, len(faces_rects)):
        print(row)
        cropped = crop(faces_rects[row], image)
        # save faces to a folder using the original image name and a unique id seperated by a '|'
        # pipe was used as some photos have a uuid style id already ( lots of dashes ) and wanted to be able to
        # differentiate between an images given name and its id as assigned through this program
        guid = str(uuid.uuid4())
        cv2.imwrite('faces/' + imname+'|' +
                    guid + '.png', cropped)
