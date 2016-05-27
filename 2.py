import cv2
import numpy as np
import os

randomByteArray = bytearray(os.urandom(120000))

flatNumpyArray = np.array(randomByteArray)
print(flatNumpyArray)

grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('RandomGray.png', grayImage)
print(grayImage)

bgrImage = flatNumpyArray.reshape(100,400,3)
cv2.imwrite('RandomColor.png', bgrImage)
print(bgrImage)