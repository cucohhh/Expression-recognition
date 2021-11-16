import numpy as np
import pandas as pd
from data_Reader import dataRead

# 加载测试集
# train_data = pd.read_csv('../fer2013原-csv/val.csv')
# num_of_instances = len(train_data)
# min_data = train_data.iloc[0:4000]
# pixels = min_data['pixels']
# emotions = min_data['emotion']
# print("测试集加载完成，大小：")
# print(len(pixels))
#
# num_classes = 7  # 表情类别数
# x_train, y_train = [], []
# x_test, y_test = [], []
# import os
# import keras
#
# for emotion, img in zip(emotions, pixels):
#     try:
#         emotion = keras.utils.to_categorical(emotion, num_classes)  # 独热向量编码
#         val = img.split(" ")
#         pixels = np.array(val, 'float32')
#         x_train.append(pixels)
#         y_train.append(emotion)
#     except:
#         print("111")
#
# print("表情分类完成 数据量：")
# print(len(x_train))
# # 数据格式转换
# x_train = np.array(x_train)
# y_train = np.array(y_train)
# x_train = x_train.reshape(-1, 48, 48, 1)
# print("数据格式转换完成")

x_train, y_train = [], []
path = "C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\fer2013原-csv\\test.csv"

data_size_begin = 0
data_size_end = 10000
res = dataRead(path, x_train, y_train, data_size_begin, data_size_end)

import matplotlib.pyplot as plt

for i in range(4):
    plt.subplot(221 + i)
    plt.gray()
    plt.imshow(res[0][i].reshape([48, 48]))
plt.show()

from keras.models import load_model

model2 = load_model('C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\trian_or_Test\\my_base_model_relu2_L2.h5')

test_score = model2.evaluate(res[0], res[1], verbose=0)
print('Test loss:', test_score[0])
print('Test accuracy:', 100 * test_score[1])
