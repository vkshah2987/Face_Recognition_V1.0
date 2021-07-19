import cv2
import json
import imutils
import requests
import numpy as np
import face_recognition

with open("metadata.json") as F1:
    Data = json.load(F1)

choice = int(input("1. Web Cam\n2. Phone Camera\nEnter you choice: "))

if choice == 1:
    print("Initializing Web cam.....................")
    cap = cv2.VideoCapture(0)
    print("Done Initializing")
else:
    print("\n\nOpen Ip Webcam App on your Android Device and Start the Service.\n")
    ip = input("Enter the Cam Ip Address[XXX.XXX.XXX.XXX]: ")
    port = input("Enter the port[XXXX]: ")

while True:

    if choice == 1:
        success, img = cap.read()
        img = cv2.flip(img, 1)
    else:
        img_resp = requests.get("http://" + str(ip) + ":" + str(port) + "/shot.jpg")
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        img = imutils.resize(img, width=1000, height=1800)

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(Data["data"], encodeFace)
        faceDis = face_recognition.face_distance(Data["data"], encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = Data["name"][matchIndex].upper()
            y1, x1, y2, x2 = faceLoc
            y1, x1, y2, x2 = y1*4, x1*4, y2*4, x2*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x2 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

    cv2.imshow("WebCam", img)
    cv2.waitKey(1)