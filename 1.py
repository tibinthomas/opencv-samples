
import cv2
import numpy as np

# Read a color picture and save it in other name in grayscale
img = cv2.imread('si1.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('gsi1.jpg',img)

# Convert an image into a raw bytes
rawByteImage = bytearray(img)

# Convert it to numpy array and reshape and save as an image
grayImage = np.array(rawByteImage).reshape(768,1024)
cv2.imwrite('gsi1fromrawByte.jpg',grayImage)

# Print the numpy array
for i in grayImage:
    print(i)
