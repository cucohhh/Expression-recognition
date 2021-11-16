import cv2

import numpy as np
import os
from tensorflow import keras



def resize_image(image):
    if len(image) != 0:
        image = cv2.resize(image, (48, 48))

    #print(image.shape)
    # ima=change_image_channels(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #print(gray.shape)
    x = np.array(gray).reshape(48, 48, 1)

    x = np.expand_dims(x, axis=0)

    return x


def displayText(img, result):
    text1 = "W:" + str(result[0][0])
    cv2.putText(img, text1, (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (10, 10, 210), 2)
    text2 = "W:" + str(result[0][1])
    cv2.putText(img, text2, (40, 80), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
    text3 = "W:" + str(result[0][2])
    cv2.putText(img, text3, (40, 110), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
    text4 = "W:" + str(result[0][3])
    cv2.putText(img, text4, (40, 140), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
    text5 = "W:" + str(result[0][4])
    cv2.putText(img, text5, (40, 170), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
    text6 = "W:" + str(result[0][5])
    cv2.putText(img, text6, (40, 200), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
    text7 = "W:" + str(result[0][6])
    cv2.putText(img, text7, (40, 230), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)


def displayEmotion(img, result,x,y,w,h):
    a = max(result)
    l = a.tolist()
    c = l.index(max(l))
    if c == 0:
        text = "anger:" #+ str(result[0][0])
    if c == 1:
        text = "disgust:" #+ str(result[0][1])
    if c == 2:
        text = "fear:" #+ str(result[0][2])
    if c == 3:
        text = "happy:" #+ str(result[0][3])
    if c == 4:
        text = "sad:" #+ str(result[0][4])
    if c == 5:
        text = "surprised:" #+ str(result[0][5])
    if c == 6:
        text = "normal:" #+ str(result[0][6])
    cv2.rectangle(img, (x-5, y), (x+w+5, y-20), (228, 181, 240), thickness=-1)
    cv2.putText(img, text, (x+20, y), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 0), 2)


def findMax(result):
    a = max(result)
    l = a.tolist()
    c = l.index(max(l))
    if c == 0:
        return "anger"
    if c == 1:
        return "disgust"
    if c == 2:
        return "fear"
    if c == 3:
        return "happy"
    if c == 4:
        return "sad"
    if c == 5:
        return "surprised"
    if c == 6:
        return "normal"



# from keras.preprocessing import image
from matplotlib.pyplot import imshow

face_cascade = cv2.CascadeClassifier(r'C:\ProgramData\Anaconda3\envs\tfenv\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
# face_cascade.load("D:\Build\OpenCV\opencv-4.1.2\modules\core\src\persistence_xml\haarcascade_frontalface_alt.xml")
# eye_cascade = cv2.CascadeClassifier("D:\face_recognized\haarcascade_eye.xml")

model2 = keras.models.load_model("../Model/my_VGG_11_model_10000_256_100.h5")

cap = cv2.VideoCapture(-1)
result=""

def facial_expression_check(cap):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    result=[]
    #cv2.imshow("img", img)
    if len(faces) > 0:
        for faceRect in faces:
            x, y, w, h = faceRect
            image = img[y - 10: y + h + 10, x - 10: x + w + 10]

            image = resize_image(image)

            result = model2.predict(image)
            # print(result)
            # print(model2.predict(image))


            cv2.rectangle(img, (x-5, y-5), (x + w+5, y + h+5), (228, 181, 240), 2)
            displayEmotion(img, result, x, y, w, h)
            roi_gray = gray[y:y + h // 2, x:x + w]
            roi_color = img[y:y + h // 2, x:x + w]

            # eyes = eye_cascade.detectMultiScale(roi_gray,1.1,1,cv2.CASCADE_SCALE_IMAGE,(2,2))
        # for (ex,ey,ew,eh) in eyes:
        # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.namedWindow("facial_expression",0)

    cv2.resizeWindow("facial_expression", 300, 200);
    cv2.imshow("facial_expression", img)
    x='Noface'
    if len(result)!=0:
        x = findMax(result)

    return x



def main():
    while True:
        facial_expression_check(cap)
        if cv2.waitKey(10) & 0xFF == ord('q'):
             break


#main()

# while True:
#     ret, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 5)
#     cv2.imshow("img", img)
#     if len(faces) > 0:
#         for faceRect in faces:
#             x, y, w, h = faceRect
#             image = img[y - 10: y + h + 10, x - 10: x + w + 10]
#             # cv2.imshow("face",image)
#
#             image = resize_image(image)
#             result = model2.predict(image)
#             #print(result)
#             # print(model2.predict(image))
#             displayEmotion(img, result,x,y,w,h)
#             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             roi_gray = gray[y:y + h // 2, x:x + w]
#             roi_color = img[y:y + h // 2, x:x + w]
#
#             # eyes = eye_cascade.detectMultiScale(roi_gray,1.1,1,cv2.CASCADE_SCALE_IMAGE,(2,2))
#         # for (ex,ey,ew,eh) in eyes:
#         # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#     cv2.imshow("facial_expression", img)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break



