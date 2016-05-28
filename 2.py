#Create an image with random numbers between 0 and 255 (byte array)
import cv2
import numpy as np
import os

#Generate 120000 random numbers between 0 and 255
randomByteArray = bytearray(os.urandom(120000))

#Convert byte array to numpy array
flatNumpyArray = np.array(randomByteArray)

#Reshape numpy array
grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('RandomGray.png', grayImage)

#Reshape numpy array to make array of array
bgrImage = flatNumpyArray.reshape(100,400,3)
cv2.imwrite('RandomColor.png', bgrImage)