import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import matplotlib.pyplot as plt 

# creates random values
x = data = np.linspace(-1.0, 1.0, 200)
y = 4.0*x +4.0 +np.random.randn(*x.shape) * 0.5

# simple model layer by layer
model = Sequential()
model.add(Dense(1, input_dim=1, activation='linear')) # input_dim - quantity of inputs

# choosing specific model for our training
model.compile(optimizer='sgd', loss='mse', metrics=['mse']) # sgd is gradient decent model and mse is quadratic loss
model.summary()

# setting up weights for them usually we use zero
weights = model.layers[0].get_weights()
w_init = weights[0][0][0]
b_init = weights[1][0]
print('Linear regression model is initialized with weights w: %.2f, b: %.2f' % (w_init, b_init)) 

# actual training of our model
model.fit(x,y, batch_size=1, epochs=30, shuffle=True)

# outputs 
weights = model.layers[0].get_weights()
w_final = weights[0][0][0]
b_final = weights[1][0]
print('Linear regression model is trained to have weight w: %.2f, b: %.2f' % (w_final, b_final))
predict = model.predict(data)
plt.plot(data, predict, 'b', data , y, 'k.')
plt.show()