# https://www.youtube.com/watch?v=lRJJEMSD7kI&list=PLA0M1Bcd0w8yv0XGiF1wjerjSZVSrYbjh&index=19
from keras.layers import Conv2D, UpSampling2D, InputLayer
from keras.models import Sequential
from skimage.color import rgb2lab, lab2rgb
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
def processed_image(img):
    if img.mode != 'RGB': img = img.convert("RGB")        
    image = img.resize( (256, 256), Image.BILINEAR)
    image = np.array(image, dtype=float)
    size = image.shape
    lab = rgb2lab(1.0/255*image)
    X, Y = lab[:,:,0], lab[:,:,1:]
    Y /= 128    # нормируем выходные значение в диапазон от -1 до 1
    X = X.reshape(1, size[0], size[1], 1)
    Y = Y.reshape(1, size[0], size[1], 2)
    return X, Y, size
img = Image.open('facegirl2Color.jpg')
plt.figure(0)
plt.imshow(img)
plt.show()
X, Y, size = processed_image(img)
model = Sequential()
model.add(InputLayer(input_shape=(None, None, 1)))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same', strides=2))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same', strides=2))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same', strides=2))
model.add(Conv2D(512, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(2, (3, 3), activation='tanh', padding='same'))
model.add(UpSampling2D((2, 2)))
model.compile(optimizer='adam', loss='mse')
model.fit(x=X, y=Y, batch_size=1, epochs=300)

'''
# Сүрөттү ак-кара кылып жазуу
imgColor = Image.open('facegirl2Color.jpg')  
imgGrey = imgColor.convert("L")
imgGrey.save('facegirl2Grey.jpg')
'''
imgColor = Image.open('facegirl2Grey.jpg') # facegirl2Color.jpg WB_Big2
imgGrey = imgColor # .convert("1")

sizeimgGrey = np.array(imgGrey, dtype=float).shape
X, Y, size = processed_image(imgGrey)
output = model.predict(X)
output *= 128
min_vals, max_vals = -128, 127
ab = np.clip(output[0], min_vals, max_vals)

cur = np.zeros((size[0], size[1], 3))
cur[:,:,0] = np.clip(X[0][:,:,0], 0, 255)
cur[:,:,1:] = ab
lab2rgbArray = lab2rgb(cur) # lab2rgb(cur).shape = (256, 256, 3)

imgC = Image.fromarray(np.uint8((lab2rgbArray)*255)) 
imgColorAI = imgC.resize((sizeimgGrey[1],sizeimgGrey[0]), Image.BILINEAR) # (256, 256, 3) дан эскисине өтөбүз

# =============================================================================
#Image.open('ColorPole.jpg').convert("L").save("ColorPoleGrey.jpg")
imgColorAI.save("WB_Big"+"AI.jpg")
# =============================================================================
plt.figure(2)
plt.subplot(1, 2, 1)
plt.imshow(imgGrey) 
plt.subplot(1, 2, 2)
plt.imshow(imgColorAI)
plt.show()