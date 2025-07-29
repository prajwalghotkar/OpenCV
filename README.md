# OpenCV
--

***1) What is an image*** 

***2) Reading an image*** 

***3) Converting it to grayscale***

***4) Playing with RGB color channels***

***5) Resize*** 

***6) Flipping***

***7) Cropping***

***8) Saving using imwrite***

***9) Stacking multiple images***

***10) Drawing shapes(rectangles,circles,lines) and Texts***

***11) Live Direct Drawing***

***12) Fetching webcam stream(in black and white)***

***13) Recording live stream shape***

***14) Working with videos shapes***

***15) Writing on live video***

***16) Image Processing Operations***

***17) Object Detection and Tracking***

--- 

# 1) What is an image:

#### **An image is a two-dimensional array (matrix) of pixels, where each pixel represents a color or intensity value.**
##### - In grayscale images, each pixel is a single value from 0 (black) to 255 (white).
##### - In colored images (RGB/BGR), each pixel is a combination of three values (Red, Green, and Blue or Blue, Green, and Red), each ranging from 0 to 255.

#### 💡 In Simple Terms:

##### - An image is made up of small dots called pixels
##### - Each pixel stores color or brightness information
##### - A computer sees an image as numbers, not pictures

#### 📁 Why Is This Important?
##### ***Understanding how images work at a pixel level is crucial for:***

##### - Image processing
##### - Computer vision
##### - Machine learning with image data
##### - Augmented reality
##### - Medical image analysis

### 🖼️ Types of Images 
#### ***OpenCV supports different types of images based on color channels and data types. Understanding these types is essential for performing image processing tasks effectively.***

### 📌 1. Grayscale Image (1 Channel)

#### - Description: Contains only shades of gray (black to white).
#### - Pixel value: From 0 (black) to 255 (white).
#### - Shape: (height, width)
#### - Use case: Faster processing, commonly used in edge detection, face detection, etc.

### 📌 2. Color Image (3 Channels - BGR)

#### - Description: Most common image type; each pixel has 3 color components: Blue, Green, and Red.
#### - Pixel value: Each channel ranges from 0 to 255.
#### - Shape: (height, width, 3)
#### - Note: OpenCV uses BGR, not RGB.

### 📌 3. Alpha Channel Image (4 Channels - BGRA)

#### - Description: Adds transparency to BGR image.
#### - Pixel value: BGRA → Blue, Green, Red, Alpha (opacity)
#### - Shape: (height, width, 4)
#### - Use case: Used for overlays, masks, etc.

### 📌 4. Binary Image (Black & White)

#### - Description: Only 2 pixel values: 0 or 255.
#### - Use case: Thresholding, object detection.
#### - Shape: (height, width)

### 📌 5. Floating Point Image

#### - Description: Pixel values are stored in float32 instead of uint8.
#### - Use case: Used in image normalization, mathematical operations, and filters.
#### - Range: Often between 0.0 and 1.0 or other custom ranges.

---
# 2) Reading an image:

<img width="1920" height="979" alt="Screenshot 2025-07-28 121521" src="https://github.com/user-attachments/assets/8d2672f6-53c8-45ed-ab61-54cd0ec7ab54" />
<img width="1920" height="997" alt="Screenshot 2025-07-28 125135" src="https://github.com/user-attachments/assets/7b404fb7-5fa7-40b7-aa65-c81bac81270b" />
<img width="1920" height="983" alt="Screenshot 2025-07-28 125250" src="https://github.com/user-attachments/assets/b2a9e01b-4fcc-41ff-87ad-76413dff47e5" />

https://github.com/prajwalghotkar/OpenCV/blob/main/prajwal_main.py

---
#  3) Converting it to grayscale:

#### > code:
import cv2

import numpy as np

img = cv2.imread("image/prajwal.png.jpg") # Read an image

img = cv2.imread("image/cat.png")

img = cv2.imread("image/Airplane-2.png")

img = cv2.imread("image/fruits.png")

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("prajwal_data_image_reading",img_gray) # Converting it to grayscale

cv2.waitKey(0)

<img width="1920" height="983" alt="Screenshot 2025-07-28 131241" src="https://github.com/user-attachments/assets/588b785c-151d-4cc0-9ee2-39d9f4253c70" />
<img width="1920" height="998" alt="Screenshot 2025-07-28 131356" src="https://github.com/user-attachments/assets/c3b8d8b2-2a0b-4c0f-9916-b4826f694483" />
<img width="1920" height="990" alt="Screenshot 2025-07-28 131545" src="https://github.com/user-attachments/assets/6503d41f-592c-47bd-92a6-e858806d740c" />
<img width="1920" height="1000" alt="Screenshot 2025-07-28 131954" src="https://github.com/user-attachments/assets/ba093396-f064-423c-b3d1-c33c5b70904b" />

https://github.com/prajwalghotkar/OpenCV/blob/main/prajwal_main.py

---

# 4) Playing with RGB color channels

#### Playing with RGB Color Channels: The RGB color model is a core concept in computer graphics, image processing, and display technology. It's an additive color model, meaning colors are created by combining light of three primary colors: Red (R), Green (G), and Blue (B). Understanding how these channels work is crucial for anyone interested in image manipulation, digital art, or programming for screens.https://en.wikipedia.org/wiki/RGB_color_model,https://en.wikipedia.org/wiki/Channel_(digital_image)

#### 1. What Are RGB Color Channels?
--
#####  - Channel refers to a separate grayscale image for each primary color: one for red, one for green, one for blue.
#####  - When combined, these channels form a full-color image in the RGB color model.
#####  - Each channel contains values representing the intensity of that color at every pixel.

#### 2. Bit-Depth and Range
--
#####  - In standard 24-bit RGB images (the industry norm), each channel is represented by 8 bits.
#####  -- This allows intensity values from 0 (no color) to 255 (full intensity) per channel.
#####  -- So, a color is represented as (R, G, B), e.g., (255, 0, 0) for pure red.
#####  - Higher-end images may use 16 bits per channel (48-bit RGB), giving even greater precision.

#### 3. How Colors Are Formed
--
##### - Each pixel in an RGB image has three values (R, G, B), each ranging from 0 to 255.
##### - The combination of these values produces a specific color.
##### -- (255, 255, 255) = white
##### -- (0, 0, 0) = black
##### -- (255, 0, 0) = red
##### -- (0, 255, 0) = green
##### -- (0, 0, 255) = blue
##### -- Mixed values create millions of unique colors: 256×256×256=16,777,216, far more than the human eye can distinguish.

#### 4. Practical Example: Isolating Channels
--
##### - Isolating a channel means displaying only the intensity of that color for every pixel, setting others to zero.
##### -- For the red channel, only the red intensity is shown; green and blue are zeroed.
##### - In Python (e.g., using NumPy or PIL), this would look like:

python
r = image[:,:,0]
g = image[:,:,1]
b = image[:,:,2]
# To visualize, set other channels to zero
red_image = np.stack([r, np.zeros_like(r), np.zeros_like(r)], axis=2)

##### - This helps you understand how each individual color contributes to the full image.

#### 5. Applications of RGB Channel Manipulation
--
##### - Image editing: Adjusting a single channel can alter image color balance, highlight specific elements, or create artistic effects.
##### - Machine learning: Feature extraction from different channels improves detection and classification.
##### - Image compression: Sometimes channels are treated or compressed differently based on visual importance.
##### - Visualization: Visualizing individual channels helps understand image structure and color composition.

#### 6. Device Dependence
--
##### - RGB is device-dependent: Different screens may render the same RGB values slightly differently due to hardware variation in how light is displayed.
##### - Printers do not use RGB but instead rely on CMYK (Cyan, Magenta, Yellow, Black) because they use inks, not light

Color	R	G	B	Description
Black	0	0	0	All channels off
White	255	255	255	All maxed out
Red	255	0	0	Max red
Green	0	255	0	Max green
Blue	0	0	255	Max blue
Yellow	255	255	0	Red + Green
Magenta	255	0	255	Red + Blue
Cyan	0	255	255	Green + Blue
<img width="367" height="262" alt="image" src="https://github.com/user-attachments/assets/abbab86e-0ed3-4fb0-a72a-2b7c745bff40" />








