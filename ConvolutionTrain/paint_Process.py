import matplotlib.pyplot as plt


def paint_process(history,name):
    epoch = len(history.history['loss'])  #迭代的次数
    plt.plot(range(epoch), history.history['loss'], label='loss')
    plt.plot(range(epoch), history.history['accuracy'], label='train_acc')
    plt.plot(range(epoch), history.history['val_accuracy'], label='val_acc')
    plt.plot(range(epoch), history.history['val_loss'], label='val_loss')
    plt.legend()
    path = "C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\trian_image\\"
    plt.savefig(path+name);
    plt.show()
