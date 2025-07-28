import cv2
import numpy as np

# Read an image

img = cv2.imread("image/prajwal.png.jpg")
#img = cv2.imread("image/cat.png")
#img = cv2.imread("image/Airplane-2.png")
#img = cv2.imread("image/fruits.png")

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# Display image
# Converting it to grayscale
cv2.imshow("prajwal_data_image_reading",img_gray)


cv2.waitKey(0)