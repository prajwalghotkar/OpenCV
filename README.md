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

-- 

## 1) What is an image:

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

