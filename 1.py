# Read a color picture and save it in other name in grayscale
import cv2

img = cv2.imread('si1.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('gsi1.jpg',img)