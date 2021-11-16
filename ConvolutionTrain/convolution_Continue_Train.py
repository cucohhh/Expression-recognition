import numpy as np

import pandas as pd
#加载训练集
train_data = pd.read_csv('../fer2013原-csv/train.csv')
num_of_instances = len(train_data)
min_data = train_data.iloc[0:30000]
pixels = min_data['pixels']
emotions =min_data['emotion']
print("训练集加载完成，数据集大小")
print(len(pixels))


# 表情类别数
num_classes = 7
x_train, y_train = [], []
x_test, y_test = [], []
import os
import keras

for emotion, img in zip(emotions, pixels):
    try:
        emotion = keras.utils.to_categorical(emotion, num_classes)  # 独热向量编码
        val = img.split(" ")
        pixels = np.array(val, 'float32')
        x_train.append(pixels)
        y_train.append(emotion)
    except:
        print("111")

print("表情 分类完成 finish")
print(len(x_train))


x_train = np.array(x_train)
y_train = np.array(y_train)
x_train = x_train.reshape(-1,48,48,1)
print("数据集 格式转换完成")
print(len(x_train))




from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Activation, Dropout, Flatten, Dense
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

batch_size = 128;
epochs = 200;

from keras.models import load_model

model = load_model('../Model/my_base_model2.h5')
model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs)

train_score = model.evaluate(x_train, y_train, verbose=0)
print('Train loss:', train_score[0])
print('Train accuracy:', 100 * train_score[1])

model.save('my_model_28709_128_200_BN_L2.h5')

##输入图片 测试模型正确性

# import os
# import numpy as np
# from keras.preprocessing import image
# from matplotlib.pyplot import imshow
# import cv2
# from keras.applications.imagenet_utils import preprocess_input
#
# img_path = 'img/test.jpg'

# img = image.load_img(img_path, target_size=(48, 48))
#
#
# def change_image_channels(image):
#     # 3通道转单通道
#     if image.mode == 'RGB':
#         r, g, b = image.split()
#     return r
#
#
# ima = change_image_channels(img)
#
# imshow(ima)
#
# x = np.array(ima).reshape(48, 48, 1)
# print(x.shape)
# x = np.expand_dims(x, axis=0)
#
# print("a")
# print(model.predict(x))
