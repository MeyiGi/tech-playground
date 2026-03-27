import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import matplotlib.pyplot as plt 
 
x = data = np.linspace(-1.0, 1.0, 1000)
y = 20.0*x -30.0 +np.random.randn(*x.shape) * 0.5


model = Sequential()
model.add(Dense(1, input_dim=1, activation='linear'))


model.compile(optimizer='sgd', loss='mse', metrics=['mse']) #Стохастический градиентный спуск ,среднеквадратическая ошибка

weights = model.layers[0].get_weights()
w_init = weights[0][0][0]
b_init = weights[1][0]
print('Linear regression model is initialized with weights w: %.2f, b: %.2f' % (w_init, b_init)) 


model.fit(x,y, batch_size=10, epochs=10, shuffle=True)

weights = model.layers[0].get_weights()
w_final = weights[0][0][0]
b_final = weights[1][0]
print('Linear regression model is trained to have weight w: %.2f, b: %.2f' % (w_final, b_final))

predict = model.predict(data)

plt.plot(data, predict, 'r', data , y, 'k.')
plt.show()