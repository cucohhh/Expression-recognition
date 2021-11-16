import cv2
import joint

from aip import AipBodyAnalysis


# """ 你的 APPID AK SK """
# APP_ID = '23411049'
# API_KEY = 'LNCh4Tz8Yq5LaMGj2qWLFH9Q'
# SECRET_KEY = 'f4FEXEHZQ2T0HVkK4GXDGPZibZHjrch5 '
#
# client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
# """ 读取图片 """
#
# with open('C:\\Users\\Administrator\\Pictures\\Camera Roll\\test3.jpeg', 'rb') as fp:
#     image = fp.read()
#
# ##image = get_file_content('example.jpg')
#
# """ 调用人体关键点识别 """
# client.bodyAnalysis(image);
# # result = client.bodyAnalysis(image)['person_info'][2]['body_parts'] ### 数字决定到底是第几个人物的关键点渲染结果
# result = client.bodyAnalysis(image)


def bodyAnalysis():
    """ 你的 APPID AK SK """
    APP_ID = '23411049'
    API_KEY = 'LNCh4Tz8Yq5LaMGj2qWLFH9Q'
    SECRET_KEY = 'f4FEXEHZQ2T0HVkK4GXDGPZibZHjrch5 '

    client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
    """ 读取图片 """

    with open('C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\test_img\\test1.jpg', 'rb') as fp:
        image = fp.read()

    ##image = get_file_content('example.jpg')

    """ 调用人体关键点识别 """
    result = client.bodyAnalysis(image)
    return result;


#my_result = bodyAnalysis()


def draw_line(result, img):
    # nose--->neck;
    cv2.line(img, (int(result['nose']['x']), int(result['nose']['y'])),
             (int(result['neck']['x']), int(result['neck']['y'])), (0, 225, 0), 2)

    # neck --> left_shoulder
    cv2.line(img, (int(result['neck']['x']), int(result['neck']['y'])),
             (int(result['left_shoulder']['x']), int(result['left_shoulder']['y'])), (0, 255, 0), 2)
    # neck --> right_shoulder
    cv2.line(img, (int(result['neck']['x']), int(result['neck']['y'])),
             (int(result['right_shoulder']['x']), int(result['right_shoulder']['y'])), (0, 255, 0), 2)
    # left_shoulder --> left_elbow
    cv2.line(img, (int(result['left_shoulder']['x']), int(result['left_shoulder']['y'])),
             (int(result['left_elbow']['x']), int(result['left_elbow']['y'])), (0, 255, 0), 2)
    # left_elbow --> left_wrist
    cv2.line(img, (int(result['left_elbow']['x']), int(result['left_elbow']['y'])),
             (int(result['left_wrist']['x']), int(result['left_wrist']['y'])), (0, 255, 0), 2)
    # right_shoulder --> right_elbow
    cv2.line(img, (int(result['right_shoulder']['x']), int(result['right_shoulder']['y'])),
             (int(result['right_elbow']['x']), int(result['right_elbow']['y'])), (0, 255, 0), 2)
    # right_elbow --> right_wrist
    cv2.line(img, (int(result['right_elbow']['x']), int(result['right_elbow']['y'])),
             (int(result['right_wrist']['x']), int(result['right_wrist']['y'])), (0, 255, 0), 2)
    # # neck --> left_hip
    # cv2.line(img, (int(result['neck']['x']), int(result['neck']['y'])),
    #          (int(result['left_hip']['x']), int(result['left_hip']['y'])), (0, 255, 0), 2)
    # # neck --> right_hip
    # cv2.line(img, (int(result['neck']['x']), int(result['neck']['y'])),
    #          (int(result['right_hip']['x']), int(result['right_hip']['y'])), (0, 255, 0), 2)
    # # left_hip --> left_knee
    # cv2.line(img, (int(result['left_hip']['x']), int(result['left_hip']['y'])),
    #          (int(result['left_knee']['x']), int(result['left_knee']['y'])), (0, 255, 0), 2)
    # # right_hip --> right_knee
    # cv2.line(img, (int(result['right_hip']['x']), int(result['right_hip']['y'])),
    #          (int(result['right_knee']['x']), int(result['right_knee']['y'])), (0, 255, 0), 2)
    # # left_knee --> left_ankle
    # cv2.line(img, (int(result['left_knee']['x']), int(result['left_knee']['y'])),
    #          (int(result['left_ankle']['x']), int(result['left_ankle']['y'])), (0, 255, 0), 2)
    # # right_knee --> right_ankle
    # cv2.line(img, (int(result['right_knee']['x']), int(result['right_knee']['y'])),
    #          (int(result['right_ankle']['x']), int(result['right_ankle']['y'])), (0, 255, 0), 2)
    #
    # cv2.line(img, (int(result['nose']['x']), int(result['nose']['y'])),
    #          (int(result['neck']['x']), int(result['neck']['y'])), (0, 225, 255), 2)
    ##cv2.imshow("image", img)
    ##cv2.waitKey(0);


def draw_one_line(result1, i, img):
    # nose--->neck;
    cv2.line(img, (int(result1['person_info'][i]['body_parts']['nose']['x']),
                   int(result1['person_info'][i]['body_parts']['nose']['y'])),
             (int(result1['person_info'][i]['body_parts']['neck']['x']),
              int(result1['person_info'][i]['body_parts']['neck']['y'])), (0, 225, 0), 2)

    # neck --> left_shoulder
    cv2.line(img, (int(result1['person_info'][i]['body_parts']['neck']['x']),
                   int(result1['person_info'][i]['body_parts']['neck']['y'])),
             (int(result1['person_info'][i]['body_parts']['left_shoulder']['x']),
              int(result1['person_info'][i]['body_parts']['left_shoulder']['y'])), (0, 255, 0), 2)
    # neck --> right_shoulder
    cv2.line(img, (int(result1['person_info'][i]['body_parts']['neck']['x']),
                   int(result1['person_info'][i]['body_parts']['neck']['y'])),
             (int(result1['person_info'][i]['body_parts']['right_shoulder']['x']),
              int(result1['person_info'][i]['body_parts']['right_shoulder']['y'])), (0, 255, 0), 2)
    # left_shoulder --> left_elbow
    cv2.line(img, (int(result1['person_info'][i]['body_parts']['left_shoulder']['x']),
                   int(result1['person_info'][i]['body_parts']['left_shoulder']['y'])),
             (int(result1['person_info'][i]['body_parts']['left_elbow']['x']),
              int(result1['person_info'][i]['body_parts']['left_elbow']['y'])), (0, 255, 0), 2)
    # left_elbow --> left_wrist
    cv2.line(img, (int(result1['person_info'][i]['body_parts']['left_elbow']['x']),
                   int(result1['person_info'][i]['body_parts']['left_elbow']['y'])),
             (int(result1['person_info'][i]['body_parts']['left_wrist']['x']),
              int(result1['person_info'][i]['body_parts']['left_wrist']['y'])), (0, 255, 0), 2)
    # right_shoulder --> right_elbow
    cv2.line(img, (int(result1['person_info'][i]['body_parts']['right_shoulder']['x']),
                   int(result1['person_info'][i]['body_parts']['right_shoulder']['y'])),
             (int(result1['person_info'][i]['body_parts']['right_elbow']['x']),
              int(result1['person_info'][i]['body_parts']['right_elbow']['y'])), (0, 255, 0), 2)
    # right_elbow --> right_wrist
    cv2.line(img, (int(result1['person_info'][i]['body_parts']['right_elbow']['x']),
                   int(result1['person_info'][i]['body_parts']['right_elbow']['y'])),
             (int(result1['person_info'][i]['body_parts']['right_wrist']['x']),
              int(result1['person_info'][i]['body_parts']['right_wrist']['y'])), (0, 255, 0), 2)
    # neck --> left_hip
    cv2.line(img, (int(result1['person_info'][i]['body_parts']['neck']['x']),
                   int(result1['person_info'][i]['body_parts']['neck']['y'])),
             (int(result1['person_info'][i]['body_parts']['left_hip']['x']),
              int(result1['person_info'][i]['body_parts']['left_hip']['y'])), (0, 255, 0), 2)
    # neck --> right_hip
    cv2.line(img, (int(result1['person_info'][i]['body_parts']['neck']['x']),
                   int(result1['person_info'][i]['body_parts']['neck']['y'])),
             (int(result1['person_info'][i]['body_parts']['right_hip']['x']),
              int(result1['person_info'][i]['body_parts']['right_hip']['y'])), (0, 255, 0), 2)
    # left_hip --> left_knee
    cv2.line(img, (int(result1['person_info'][i]['body_parts']['left_hip']['x']),
                   int(result1['person_info'][i]['body_parts']['left_hip']['y'])),
             (int(result1['person_info'][i]['body_parts']['left_knee']['x']),
              int(result1['person_info'][i]['body_parts']['left_knee']['y'])), (0, 255, 0), 2)
    # right_hip --> right_knee
    cv2.line(img, (int(result1['person_info'][i]['body_parts']['right_hip']['x']),
                   int(result1['person_info'][i]['body_parts']['right_hip']['y'])),
             (int(result1['person_info'][i]['body_parts']['right_knee']['x']),
              int(result1['person_info'][i]['body_parts']['right_knee']['y'])), (0, 255, 0), 2)
    # left_knee --> left_ankle
    cv2.line(img, (int(result1['person_info'][i]['body_parts']['left_knee']['x']),
                   int(result1['person_info'][i]['body_parts']['left_knee']['y'])),
             (int(result1['person_info'][i]['body_parts']['left_ankle']['x']),
              int(result1['person_info'][i]['body_parts']['left_ankle']['y'])), (0, 255, 0), 2)
    # right_knee --> right_ankle
    cv2.line(img, (int(result1['person_info'][i]['body_parts']['right_knee']['x']),
                   int(result1['person_info'][i]['body_parts']['right_knee']['y'])),
             (int(result1['person_info'][i]['body_parts']['right_ankle']['x']),
              int(result1['person_info'][i]['body_parts']['right_ankle']['y'])), (0, 255, 0), 2)

    # cv2.imshow("image", img)
    # cv2.waitKey(0);


def draw_all_line(personnum, result,img_painted):
    for i in range(personnum):
        draw_one_line(result, i - 1, img_painted);


# src = cv2.imread("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\test_img\\test6.jpg")
# my_result = bodyAnalysis()
# img_painted = src;
# personnum = my_result['person_num'];
# draw_all_line(personnum, my_result,img_painted);
# cv2.imshow("image", src);
# cv2.waitKey(0);
#
# print(my_result)
#
# print(my_result['person_info'][0]['body_parts']['nose']['x']);
