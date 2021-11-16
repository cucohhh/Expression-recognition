import keras
import pandas as pd
import numpy as np


def dataRead(path, x_data, y_data, data_size_begin, data_size_end):
    # 加载训练集
    train_data = pd.read_csv(path)
    num_of_instances = len(train_data)
    min_data = train_data.iloc[data_size_begin:data_size_end]
    pixels = min_data['pixels']
    emotions = min_data['emotion']
    print("数据集加载完成，数据集大小")
    print(len(pixels))

    # 表情类别数
    num_classes = 7
    # x_train, y_train = [], []
    # x_test, y_test = [], []
    import os
    import keras

    for emotion, img in zip(emotions, pixels):
        try:
            emotion = keras.utils.to_categorical(emotion, num_classes)  # 独热向量编码
            val = img.split(" ")
            pixels = np.array(val, 'float32')
            x_data.append(pixels)
            y_data.append(emotion)
        except:
            print("111")

    print("表情 分类完成 finish")
    print(len(x_data))

    x_data = np.array(x_data)
    y_data = np.array(y_data)
    x_data = x_data.reshape(-1, 48, 48, 1)
    print("数据集 格式转换完成")
    print(len(x_data))
    res = [];
    res.append(x_data)
    res.append(y_data)
    return res;


# path = "C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\fer2013原-csv\\test.csv"
# x_test = [];
# y_test = [];
#
# res = dataRead(path, x_test, y_test, 0, 1000)
#
# import matplotlib.pyplot as plt
#
# for i in range(4):
#     plt.subplot(221 + i)
#     plt.gray()
#     plt.imshow(res[0][i].reshape([48, 48]))
# plt.show()
