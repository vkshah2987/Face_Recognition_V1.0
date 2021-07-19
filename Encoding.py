import os
import cv2
import numpy as np
import face_recognition


def initiate():

    path = "Train_Data"
    images = []
    className = []
    myList = os.listdir(path)

    for cl in myList:
        curImg = cv2.imread(f"{path}/{cl}")
        images.append(curImg)
        className.append(os.path.splitext(cl)[0])

    return images, className


def UpdateEncoding(images):

    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    arr = np.array(encodeList)
    list1 = arr.tolist()

    return list1