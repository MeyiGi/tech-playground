import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import matplotlib.pyplot as plt 

# preparing dataset
x = data = np.linspace(-1.0, 1.0, 500)
x1 = x
x2 = x*x
x3 = x*x*x # we are trying to convert our function to linear
t = np.array([[j,k,l] for j,k,l in zip(x1,x2,x3)])


y = x3 - x1 + np.random.randn(*x.shape) * 0.05


model = Sequential()
model.add(Dense(1, input_dim=3, activation='linear')) # Чыгыш - 1, кириш -3 
optimayzer1 = keras.optimizers.SGD(learning_rate=0.01)
model.compile(optimizer=optimayzer1, loss='mse', metrics=['mse'])
model.fit(t,y, batch_size=1, epochs=50, shuffle=True)
weights = model.layers[0].get_weights() # Найденные веса графа
predict = model.predict(t)
plt.plot(x, predict, 'b', x , y, 'r.')
plt.show()
# =============================================================================
# #Тестируем программу
# for k in range(10):
#     i=np.random.randint(0,len(x))
#     print(i,t[i])
#     print(weights[0][0]*t[i][0]+weights[0][1]*t[i][1]+weights[0][2]*t[i][2]+weights[1][0]-predict[i])
# =============================================================================
