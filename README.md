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

<img width="1920" height="983" alt="Screenshot 2025-07-28 131241" src="https://github.com/user-attachments/assets/588b785c-151d-4cc0-9ee2-39d9f4253c70" />
<img width="1920" height="998" alt="Screenshot 2025-07-28 131356" src="https://github.com/user-attachments/assets/c3b8d8b2-2a0b-4c0f-9916-b4826f694483" />
<img width="1920" height="990" alt="Screenshot 2025-07-28 131545" src="https://github.com/user-attachments/assets/6503d41f-592c-47bd-92a6-e858806d740c" />
<img width="1920" height="1000" alt="Screenshot 2025-07-28 131954" src="https://github.com/user-attachments/assets/ba093396-f064-423c-b3d1-c33c5b70904b" />











