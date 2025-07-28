import cv2
import numpy as np

# Read an image

img = cv2.imread("image/cat.png")

print(type(img))

print(img.shape)

# Display image

cv2.imshow("prajwal_data_image_reading",img)


# What it does:

# cv2.imshow() is a function from OpenCV that displays an image in a window.

# "prajwal_data_image_processing" is the name of the window.

# img is the image data that you want to display (loaded using cv2.imread()).

# Without cv2.waitKey(0), the image window will open and close immediately.

# 🔴 Problem--> 1) Window opens and closes immediately becouse of Missing cv2.waitKey(). solution of that  problem is Add cv2.waitKey(0) after imshow()
# 🔴 Problem--> 2) Black screen or no image shown becouse of Image img is None. solution of that  problem is Make sure cv2.imread() loaded the image successfully.
# 🔴 Problem--> 3) Error on headless system (e.g., servers, Docker) becouse of No display environment (GUI not available) solution of that  problem is Use opencv-python-headless or skip imshow() in such systems.
# 🔴 Problem--> 4) Freeze or crash on some IDEs (like VSCode/IDLE) becouse of GUI conflict. solution of that problem is Run from terminal (Command Prompt) instead of inside the IDE.
# 🔴 Problem--> 5) Long delay when using cv2.waitKey() becouse of Using waitKey(0) without destroyAllWindows(). solution of that problem is Always call cv2.destroyAllWindows() after key press.

cv2.waitKey(0)