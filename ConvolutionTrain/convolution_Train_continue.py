import numpy as np

import pandas as pd

from keras import regularizers
from data_Reader_T import dataRead_T
from data_Reader import dataRead
# 加载训练集
path_train = "C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\fer2013原-csv\\train.csv"
train_data_x =[];
train_data_y =[];
train_size_begin = 0;
train_size_end = 30000;
train = dataRead(path_train,train_data_x,train_data_y,train_size_begin,train_size_end)
# 加载测试集
path_test = "C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\fer2013原-csv\\test.csv"
test_data_x=[]
test_data_y=[]
test_size_begin = 0;
test_size_end = 10000;
test = dataRead(path_test,test_data_x,test_data_y,test_size_begin,test_size_end)

from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Activation, Dropout, Flatten, Dense, BatchNormalization
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

batch_size = 256;
epochs = 30;

from keras.models import load_model

model = load_model('C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\trian_or_Test\\my_base_model_relu2_Dropout_Normalization.h5')

# 进行训练
model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])
history = model.fit(train[0], train[1], batch_size=batch_size, epochs=epochs, validation_data=(test[0],test[1]),shuffle='true')

train_score = model.evaluate(train[0], train[1], verbose=0)
print('Train loss:', train_score[0])
print('Train accuracy:', 100 * train_score[1])

model.save('my_base_model_relu2_L2_2twice.h5')

from paint_Process import paint_process

name = "my_base_model_relu2_L2_2twice"
paint_process(history, name);


