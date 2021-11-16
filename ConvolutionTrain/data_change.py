from data_Reader_T import dataRead_T

x_train, y_train = [], []
path = "C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\fer2013原-csv\\test.csv"

data_size_begin = 0
data_size_end = 1000
res = dataRead_T(path, x_train, y_train, data_size_begin, data_size_end)

import matplotlib.pyplot as plt

for i in range(4):
    plt.subplot(221 + i)
    plt.gray()
    temp = res[0][i].reshape([48,48])
    plt.imshow(temp)
plt.show()