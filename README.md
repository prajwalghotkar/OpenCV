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
---
#### 1. What Are RGB Color Channels?

#####  - Channel refers to a separate grayscale image for each primary color: one for red, one for green, one for blue.
#####  - When combined, these channels form a full-color image in the RGB color model.
#####  - Each channel contains values representing the intensity of that color at every pixel.
---
#### 2. Bit-Depth and Range

#####  - In standard 24-bit RGB images (the industry norm), each channel is represented by 8 bits.
#####  -- This allows intensity values from 0 (no color) to 255 (full intensity) per channel.
#####  -- So, a color is represented as (R, G, B), e.g., (255, 0, 0) for pure red.
#####  - Higher-end images may use 16 bits per channel (48-bit RGB), giving even greater precision.
---
#### 3. How Colors Are Formed

##### - Each pixel in an RGB image has three values (R, G, B), each ranging from 0 to 255.
##### - The combination of these values produces a specific color.
##### -- (255, 255, 255) = white
##### -- (0, 0, 0) = black
##### -- (255, 0, 0) = red
##### -- (0, 255, 0) = green
##### -- (0, 0, 255) = blue
##### -- Mixed values create millions of unique colors: 256×256×256=16,777,216, far more than the human eye can distinguish.
---
#### 4. Practical Example: Isolating Channels

##### - Isolating a channel means displaying only the intensity of that color for every pixel, setting others to zero.
##### -- For the red channel, only the red intensity is shown; green and blue are zeroed.
##### - In Python (e.g., using NumPy or PIL), this would look like:

python
r = image[:,:,0]
g = image[:,:,1]
b = image[:,:,2]
##### To visualize, set other channels to zero
red_image = np.stack([r, np.zeros_like(r), np.zeros_like(r)], axis=2)

##### - This helps you understand how each individual color contributes to the full image.
---
#### 5. Applications of RGB Channel Manipulation

##### - Image editing: Adjusting a single channel can alter image color balance, highlight specific elements, or create artistic effects.
##### - Machine learning: Feature extraction from different channels improves detection and classification.
##### - Image compression: Sometimes channels are treated or compressed differently based on visual importance.
##### - Visualization: Visualizing individual channels helps understand image structure and color composition.
---
#### 6. Device Dependence

##### - RGB is device-dependent: Different screens may render the same RGB values slightly differently due to hardware variation in how light is displayed.
##### - Printers do not use RGB but instead rely on CMYK (Cyan, Magenta, Yellow, Black) because they use inks, not light
---
#### 7. Quick Channel Reference Table

<img width="367" height="262" alt="image" src="https://github.com/user-attachments/assets/abbab86e-0ed3-4fb0-a72a-2b7c745bff40" />

<img width="1920" height="994" alt="Screenshot 2025-07-29 123648" src="https://github.com/user-attachments/assets/fb8ef951-c7c8-4b19-96b4-c6fdb33c3e7c" />
<img width="1920" height="1005" alt="Screenshot 2025-07-29 124312" src="https://github.com/user-attachments/assets/479838c3-a067-4480-9f0e-73e551ab523a" />
<img width="1920" height="1015" alt="Screenshot 2025-07-29 123749" src="https://github.com/user-attachments/assets/7b7e8104-c65a-4b04-b6c0-7cf90b79d2bc" />
<img width="1920" height="1018" alt="Screenshot 2025-07-29 133131" src="https://github.com/user-attachments/assets/d56929f4-420e-4e2d-a2ae-65a4dee8077a" />

---
# 5) Image Resizing

##### Image resizing is a fundamental operation in image processing, computer vision, and machine learning workflows. In OpenCV, it's performed with the cv2.resize() function. Here’s a detailed breakdown suitable for your GitHub documentation:

##### What Is Image Resizing?
- Image resizing changes the dimensions (width and height) of an input image.
- It can be used to scale images up (enlarge) or down (shrink), depending on the target size.

##### Why Resize Images?
- **Standardization**: Many algorithms and models (like neural networks) require images of a fixed size for consistent input.
- **Efficiency**: Smaller images reduce computation time and memory usage.
- **Visualization**: Making large images smaller for web or app display, or enlarging thumbnails for previews.

```
python
import cv2
import numpy as np

img = cv2.imread("image/praajwal.png")  # Read an image
img_resize = cv2.resize(img, (256, 256))  # Resize image
print(img_resize.shape)
cv2.imshow('prajwal_image', img_resize)
cv2.waitKey(0)
```
##### - Parameters:

- **img**: The input image (as a NumPy array).
- **(256, 256)**: The new size in pixels as a tuple `(width, height)`.

##### How It Works

###### Interpolation: Resizing requires recalculating pixel values.
- **Shrinking**: Combines information from several pixels into one (risk of information loss).
- **Enlarging**: Computes new pixels based on neighbors (can lead to blurring).
###### OpenCV offers several interpolation methods (like cv2.INTER_LINEAR, cv2.INTER_NEAREST, etc.), each affecting the result’s sharpness and quality.

<img width="1920" height="1003" alt="Screenshot 2025-07-29 134834" src="https://github.com/user-attachments/assets/bbb84443-0820-4f33-8e29-3e1ab857f74d" />

---

# 6) Flipping:

##### Image flipping in OpenCV is the process of reversing an image along a particular axis, effectively creating a mirror image, turning it upside down, or both. This operation is performed with the cv2.flip() function and is widely used for data augmentation, visualization, or correcting image orientation.

##### Why Flip Images?
- **Augmentation**: Flipping images can help expand datasets for machine learning, making models more robust.
- **Correction**: Fix images that are mirrored or upside down.
- **Visualization**: Quickly view how an image looks from a different perspective.

##### The OpenCV Flip Function :
```
flipped_img = cv2.flip(src, flipCode)
```

##### src: The input image (NumPy array).
##### flipCode: Integer specifying the axis:

- **0** = Flip vertically (up/down, around the x-axis)

```
import cv2
import numpy as np
# Read an image
img = cv2.imread("image/Airplane-2.png")
# Flipping
img_flip = cv2.flip(img,0)
final_img_flip=cv2.resize(img_flip,(256,256))
cv2.imshow('Airplan_image',final_img_flip)
cv2.waitKey(0)
```
<img width="1920" height="1013" alt="Screenshot 2025-07-29 143236" src="https://github.com/user-attachments/assets/080de9fa-4f57-4425-a4ef-3b27773a1c82" />

---

- **1** = Flip horizontally (left/right, around the y-axis)

```
import cv2
import numpy as np
# Read an image
img = cv2.imread("image/Airplane-2.png")
# Flipping
img_flip = cv2.flip(img,1)
final_img_flip=cv2.resize(img_flip,(256,256))
cv2.imshow('Airplan_image',final_img_flip)
cv2.waitKey(0)
```
<img width="1920" height="1005" alt="Screenshot 2025-07-29 143548" src="https://github.com/user-attachments/assets/04c00bc7-14be-49a9-b8ff-277e6da929c8" />

---

- **-1** = Flip both vertically and horizontally (180-degree rotation)

```
import cv2
import numpy as np
# Read an image
img = cv2.imread("image/cat.png")
# Flipping
img_flip = cv2.flip(img,-1)
final_img_flip=cv2.resize(img_flip,(256,256))
cv2.imshow('cat_image',final_img_flip)
cv2.waitKey(0)
```
<img width="1920" height="988" alt="Screenshot 2025-07-29 143910" src="https://github.com/user-attachments/assets/fc866f7d-5092-45ce-ab29-a05d774bc807" />
---

# 7) Cropping:
##### Image cropping in OpenCV is the process of extracting a specific region from an image by specifying its pixel boundaries. This is a vital operation in image processing for focusing on areas of interest, removing unnecessary parts, or preparing images for further analysis.

##### Why Crop Images?
- **Highlight Regions of Interest**: Focus on a subject or important area.
- **Remove Unwanted Areas**: Eliminate backgrounds, logos, or artifacts.
- **Data Preparation**: Create consistent input dimensions for machine learning or computer vision tasks.

##### Cropping in OpenCV
- ***OpenCV does not provide a dedicated cropping function. Instead, you crop images using NumPy array slicing, since images in OpenCV (Python) are represented as NumPy arrays.***

```
import cv2
import numpy as np
# Read an image
img = cv2.imread("image/Airplane-2.png")
# cropping
img_crop =img[100:300,200:500]
cv2.imshow('Airplane_image',img_crop)
cv2.waitKey(0)
```
<img width="1920" height="1013" alt="Screenshot 2025-07-29 190200" src="https://github.com/user-attachments/assets/81976bf6-3f08-428a-bdb1-f265b2495c01" />

---
# 8) Saving using imwrite:

##### Saving Images Using cv2.imwrite() in OpenCV: Description for GitHub Documentation Image saving is a critical step in image processing workflows, allowing you to write processed or generated images from memory to storage devices such as your hard drive. OpenCV provides the cv2.imwrite() function to save images in various file formats simply and efficiently.

##### What is cv2.imwrite()?

- cv2.imwrite() saves an image stored as a NumPy array to a specified file.
- The image format is automatically determined by the filename’s extension (e.g., .jpg, .png, .bmp).
- It works primarily with 8-bit single-channel (grayscale) or 3-channel (color, BGR order) images.
- Returns True if the image is saved successfully; otherwise, it returns False.

##### Why Save Images?
- **Persist results**: Save your processed images for later use, sharing, or documentation.
- **Data storage**: Store modified images after applying filters, resizing, cropping, or other transformations.
- **Experiment tracking**: Keep a historical record of outputs and augment datasets.
- **Integration**: Prepare images for external applications or web display in standard formats.

```
Syntax:
cv2.imwrite(filename, image, params=None)
```

- **filename**: String representing the path and file name to save the image, including extension to specify format.
- **image**: Image data as a NumPy array, typically obtained from OpenCV functions or image processing steps.
- **params (optional)**: Format-specific parameters like compression level (e.g., JPEG quality), passed as a list of pairs.

```
import cv2
import numpy as np
# Read an image
img = cv2.imread("image/cat.png")
img_crop=img[0:300,0:300]
# Save the image in png format
cv2.imwrite('cat_small.png', img_crop)
cv2.imshow('cat_image',img_crop)
cv2.waitKey(0)

```
---
# 9) Drawing shapes (rectangles,circles,lines) and Texts:

##### Drawing Shapes (Rectangles, Circles, Lines) and Texts in OpenCV: GitHub-Ready Guide OpenCV offers simple, powerful functions for drawing basic shapes and adding text directly on images. These drawing tools are essential for visualizing annotations, marking points of interest, or creating simple graphics for documentation and debugging.

##### Why Draw on Images?
- **Annotation**: Highlight regions, objects, or important features.
- **Debugging**: Visualize steps in computer vision pipelines.
- **Presentation**: Make results more understandable for others.

##### Drawing a Rectangle
- **Draw rectangles to highlight objects or areas**:
```
v2.rectangle(image, pt1, pt2, color, thickness)
```

- **image**: The target image (NumPy array).
- **pt1**: Top-left corner (x1, y1).
- **pt2**: Bottom-right corner (x2, y2).
- **color**: Tuple in BGR format, e.g., (0, 255, 0) for green.
- **thickness**: Border thickness (set -1 to fill the rectangle).

```
import cv2
img = cv2.imread("image/cat.png")
cv2.rectangle(img, (50, 40), (200, 180), (0, 255, 0), 2)
```
---
##### Drawing a Circle
###### Use circles for center-points or highlights:
```
cv2.circle(image, center, radius, color, thickness)
```
- **radius**: Circle’s radius in pixels.
- **center**: (x, y) coordinates for the circle’s center.
```
import cv2
import numpy as np
# Create a black image
img = np.zeros((512,512,3), dtype=np.uint8)
# Circle
cv2.circle(img, (100,400), 70, (0,0,255), -1)
cv2.imshow('blue_rectangle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
<img width="1920" height="1007" alt="Screenshot 2025-07-30 154914" src="https://github.com/user-attachments/assets/ad0a0360-e290-4f1b-9798-b8aa4d7015bf" />
<img width="1920" height="1013" alt="Screenshot 2025-07-30 154842" src="https://github.com/user-attachments/assets/39459bb2-7f29-4da3-ba15-7cfca9d942ac" />

---
##### Drawing a Rectangle
###### Draw rectangles to highlight objects or areas:
```cv2.rectangle(image, pt1, pt2, color, thickness)```
- **image**: The target image (NumPy array).
- **pt1**: Top-left corner (x1, y1).
- **pt2**: Bottom-right corner (x2, y2).
- **color**: Tuple in BGR format, e.g., (0, 255, 0) for green.
- **thickness**: Border thickness (set -1 to fill the rectangle).

```
import cv2
import numpy as np
# Create a black image
img = np.zeros((512,512,3), dtype=np.uint8)
# Rectangle
cv2.rectangle(img, (100,100), (300,300), (255,0,0), -1)
cv2.imshow('blue_rectangle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

<img width="1920" height="1024" alt="Screenshot 2025-07-30 152527" src="https://github.com/user-attachments/assets/7ee5671c-ec1f-4c6a-b148-ec864a0413bb" />
<img width="1920" height="1011" alt="Screenshot 2025-07-30 152616" src="https://github.com/user-attachments/assets/a10d6d6c-4835-45a2-a6d8-4f9189396d70" />

---
##### Drawing a Line
###### To connect points (paths, axes):

```
cv2.line(image, pt1, pt2, color, thickness)
```
- **pt1**: Starting point.
- **pt2**: Ending point.

```
import cv2
import numpy as np
# Create a black image
img = np.zeros((512,512,3), dtype=np.uint8)
# Line
cv2.line(img, (0,0), (512,512), (0,255,0), 2)
cv2.imshow('blue_rectangle',img)
cv2.waitKey(0)
```
<img width="1920" height="998" alt="Screenshot 2025-07-30 155334" src="https://github.com/user-attachments/assets/99ad922a-2aec-497e-9c80-76fc4b0ed9ca" />

---
##### Adding Text
###### Display information or labels on images:

```
cv2.putText(image, text, org, font, fontScale, color, thickness, lineType)
```
- **text**: String to draw.
- **org**: Bottom-left corner of text (x, y).
- **font**: Font type (e.g., cv2.FONT_HERSHEY_SIMPLEX).
- **fontScale**: Multiplier for text size.
- **color**: Text color in BGR.
- **thickness**: Line thickness.

```
import cv2
import numpy as np
# Create a black image
img = np.zeros((512,512,3), dtype=np.uint8)
# Rectangle
cv2.rectangle(img, (100,100), (300,300), (255,0,0), -1)
# Circle
cv2.circle(img, (100,400), 70, (0,0,255), -1)
# Line
cv2.line(img, (0,0), (512,512), (0,255,0), 2)
# Text
cv2.putText(img, 
    'Hello Prajwal Ghotkar', 
    (100,100), 
    cv2.FONT_ITALIC, 
    4, 
    (0,255,255), 
    2, 
    cv2.LINE_AA
)
cv2.imshow('blue_rectangle',img)
cv2.waitKey(0)
```
<img width="1920" height="1017" alt="Screenshot 2025-07-30 162755" src="https://github.com/user-attachments/assets/d0220d64-66c0-424e-9eca-04d88d2dee07" />

##### Common Applications
- Visualizing detections or predictions in object detection and tracking.
- Annotating datasets or creating teaching material.
- Debugging coordinate and area calculations.
---
# 10) Live Direct Drawing:
##### Live Direct Drawing in OpenCV: Interactive Drawing with the Mouse Live direct drawing in OpenCV refers to capturing user interaction (usually mouse events) in real time, allowing the user to draw shapes directly onto a displayed window. This is a common feature for annotation tools, prototyping, or simple paint-style applications.

###### Why Use Live Drawing?
- **Interactive annotation**: Mark regions of interest on frames or live video.
- **Data labeling**: Quick drawing over images for dataset creation.
- **Creative applications**: Build live sketch or paint tools in Python.

###### How Live Drawing Works
- OpenCV can track mouse events (click, drag, release) in a window using cv2.setMouseCallback.
- The program updates the displayed image based on current mouse position and drawing actions in real time.

```
import cv2
import numpy as np

# Mouse callback function
def draw(event, x, y, flags, param):
    if event == 1:
        cv2.circle(img,center=(x,y),radius=50,color=(0,0,255),thickness=-1)

cv2.namedWindow("window")
cv2.setMouseCallback("window", draw)

img = np.zeros((512,512,3), dtype=np.uint8)

while True:
    cv2.imshow("window", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()

```
<img width="1920" height="1009" alt="Screenshot 2025-07-30 233527" src="https://github.com/user-attachments/assets/04064031-274f-4980-9d9f-141da671e288" />
"C:\Users\pmgho\Videos\Screen Recordings\Screen Recording 2025-07-30 231848.mp4"

- Press and hold the left mouse button to draw a rectangle.
- Rectangle is shown dynamically as you drag.
- Release the button to finalize the rectangle.

##### Additional Applications
- Draw lines, circles, or freehand curves by extending the mouse event logic.
- Combine with webcam frames (cv2.VideoCapture) for live annotation on video.
- Add keyboard controls to switch drawing modes or save results.

##### Workflow
- Display image or frame in a window.
- Listen for real-time mouse events/clicks.
- Draw/update shapes on mouse move and finalize on release.
- Show updates instantly in the window.
--- 
