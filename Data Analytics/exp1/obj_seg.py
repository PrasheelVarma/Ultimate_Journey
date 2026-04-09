import cv2 
import numpy as np 
from skimage.segmentation import felzenszwalb 
import matplotlib.pyplot as plt 
# Load image 
image_path = r'C:\Users\datla\Pictures\wallpapers\pexels-souvenirpixels-414612.jpg'   
image = cv2.imread(image_path) 
# Check if image is loaded successfully 
if image is None: 
    raise FileNotFoundError(f"Error: Unable to load image at {image_path}. Please check the file path.") 
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
# Apply Felzenszwalb’s Hierarchical Segmentation 
segments = felzenszwalb(image, scale=100, sigma=0.5, min_size=50) 
# Display results 
plt.figure(figsize=(10, 5)) 
plt.subplot(1, 2, 1) 
plt.imshow(image) 
plt.title('Original Image') 
plt.subplot(1, 2, 2) 
plt.imshow(segments, cmap='jet') 
plt.title('Segmented Image') 
plt.show() 