#  Берилишти алуу
from keras.datasets import mnist
from PIL import Image, ImageDraw
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
imagen = Image.fromarray(train_images[5])
numbertrain = train_images.shape

# Берилиштерди даярдоо
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255


# Вывод n-цифры на экран
digit = train_images[10].reshape((28,28))
import matplotlib.pyplot as plt
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()


# Модел тузүү
from keras import models
from keras import layers
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(512, activation='relu'))
network.add(layers.Dropout(0.3))
network.add(layers.Dense(32, activation='relu'))
network.add(layers.Dense(10, activation='softmax'))

# Комптляция жасоо
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# Категрияны түзүү
from keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# тармакты үйрөтүү
history = network.fit(train_images, train_labels, epochs=5, batch_size=128) 

# тармакты тест берилишинде текшерүү
test_loss, test_acc = network.evaluate(test_images, test_labels)


# Үйрөтүү процесси
plt.figure(100)
plt.plot(history.history['loss'],label = 'loss')
plt.plot(history.history['accuracy'],label = 'accuracy')
plt.xlabel('Epochs')
plt.ylabel('loss and accuracy')
plt.show()

'''
# Проверим:
digit = test_images[11].reshape((28,28))
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()
import numpy as np
res = network(digit.reshape((1,28*28)))
print(res)
print(np.argmax(res))
'''