from aip import AipBodyAnalysis
from Test import draw_line
from datetime import datetime

import math
import cv2
import time

from tensorflow import keras
from face_check import facial_expression_check
from DocumentGeneration import generateDocument
from SMTP_send import SMTPSend

face_cascade = cv2.CascadeClassifier(
    r'C:\ProgramData\Anaconda3\envs\tfenv\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
# face_cascade.load("D:\Build\OpenCV\opencv-4.1.2\modules\core\src\persistence_xml\haarcascade_frontalface_alt.xml")
# eye_cascade = cv2.CascadeClassifier("D:\face_recognized\haarcascade_eye.xml")

model2 = keras.models.load_model("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\trian_or_Test\\my_base_model6.h5")

expression = {'anger': 0, 'disgust': 0, 'fear': 0, 'happy': 0, 'sad': 0, 'surprised': 0, 'normal': 0, 'Noface': 0}
posture = {'cross_arms': 0, 'shoulder_drop': 0}


# total = 0 #总共表情和姿态的检测次数


# 将opencv读取图片转换成字符串

def ChangeToString(image):
    # image_str = cv2.imencode('.jpg',image)[1].tostring();

    print("图片转字节中...")
    a = datetime.now();
    image_str = cv2.imencode('.jpg', image)[1].tobytes();
    b = datetime.now();
    changeTime = (b - a).seconds;
    print(changeTime);
    return image_str;


def BodyAnalysis(img_str):
    print("分析数据中...");
    """ 你的 APPID AK SK """
    APP_ID = '23411049'
    API_KEY = 'LNCh4Tz8Yq5LaMGj2qWLFH9Q'
    SECRET_KEY = 'f4FEXEHZQ2T0HVkK4GXDGPZibZHjrch5 '

    client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
    """ 读取图片 """
    image = img_str;
    """ 调用人体关键点识别 """
    a = datetime.now();
    result = client.bodyAnalysis(image);

    b = datetime.now();
    bodyAnalysisTime = (b - a).seconds;

    print(bodyAnalysisTime);
    return result;


# 分析是否交叉手臂 判断手腕关键点的横坐标
def cross_arms(left_wrist, right_wrist):
    if left_wrist <= right_wrist:
        posture['cross_arms'] = posture['cross_arms'] + 1;
        return True
    else:
        return False


# 分析肩部高低差，左右肩部关键点纵坐标差不能大于50px
def shoulder_drop(left_shoulder, right_shoulder):
    if math.fabs(left_shoulder - right_shoulder) > 20:
        posture['shoulder_drop'] = posture['shoulder_drop'] + 1;
        return True
    else:
        return False


def Body_posture_check(frame):
    img_str = ChangeToString(frame);
    my_result = BodyAnalysis(img_str);
    person = my_result['person_info'][0]['body_parts'];
    draw_line(person, frame)
    cv2.namedWindow("body_posture", 0)
    cv2.resizeWindow("body_posture", 300, 200)
    cv2.imshow("body_posture", frame)
    cross_arms_count = 0
    shoulder_drop_count = 0
    if cross_arms(int(person['left_wrist']['x']), int(person['right_wrist']['x'])):
        print("存在交叉双臂动作")
        cross_arms_count = cross_arms_count + 1
    if shoulder_drop(int(person['left_shoulder']['y']), int(person['right_shoulder']['y'])):
        print("左右肩部高低差过大")
        shoulder_drop_count = shoulder_drop_count + 1


def facial_expression_statistics(result):
    expression[result] = expression[result] + 1


# 设置摄像头捕获
cap = cv2.VideoCapture(0);

flag = True

def GetView():
    print("dainji")

    var = 30;  # 每1000毫秒检测一次
    person = None;
    my_result = None;
    total = 0;

    while flag:
        var = var + 1;
        ret, frame = cap.read();
        # cv2.imshow("image", frame)

        # img_str = ChangeToString(frame);
        # my_result = BodyAnalysis(img_str);
        # person = my_result['person_info'][0]['body_parts'];
        result = facial_expression_check(cap)
        facial_expression_statistics(result)
        total = total + 1
        if (var % 30 == 0):
            # img_str = ChangeToString(frame);
            # my_result = BodyAnalysis(img_str);
            # person = my_result['person_info'][0]['body_parts'];
            # draw_line(person, frame);
            # cv2.imshow("body_posture", frame)

            Body_posture_check(frame)

        if cv2.waitKey(10) & 0xff == ord('q'):
            print(expression)
            print(posture)
            print(var)
            #cap.release()
            cv2.destroyAllWindows()
            generateDocument(expression, posture, total)
            time.sleep(2)
            SMTPSend()

            break
    return



def stopLearning():
    print("dainji stop Learning")
    flag = False;
    cap.release()
    cv2.destroyAllWindows()

    time.sleep(10)
    SMTPSend()



def mytest():
    img = cv2.imread('C:\\Users\\Administrator\\Pictures\\Camera Roll\\test3.jpeg');
    # draw_line(result,img);

    str = ChangeToString(img);

    result = BodyAnalysis(str);
    result1 = result['person_info'][0]['body_parts'];
    draw_line(result1, img);

    cv2.imshow('result', img);
    cv2.waitKey(0);
    print(result['person_info'][0]['body_parts']['nose']['x']);
