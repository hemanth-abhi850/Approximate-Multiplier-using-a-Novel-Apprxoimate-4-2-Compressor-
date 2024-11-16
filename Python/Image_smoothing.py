import numpy as np
import cv2
import matplotlib.pyplot as plt 

# Define the kernel size for smoothing
kernel_size = (5, 5)  # Size of the kernel (must be odd)

# Define the approximate multiplier function
def approximate_multiply(a, b):
    # Placeholder for an approximate multiplication function
    # Replace this with your actual approximation logic
    return a * b  # This is exact multiplication, replace with your logic

# Custom smoothing function
def smooth_image(image, kernel_size, approximate_multiply):
    # Create the kernel with equal values for averaging
    kernel = np.ones(kernel_size, dtype=np.float64) / (kernel_size[0] * kernel_size[1])

    # Get the dimensions of the image and kernel
    rows, cols = image.shape
    k_rows, k_cols = kernel.shape
    k_center_x = k_cols // 2
    k_center_y = k_rows // 2

    # Create an output image
    smoothed_image = np.zeros_like(image, dtype=np.float64)

    # Convolve the kernel over the image
    for i in range(k_center_y, rows - k_center_y):
        for j in range(k_center_x, cols - k_center_x):
            sum_value = 0.0
            for m in range(k_rows):
                for n in range(k_cols):
                    # Apply the approximate multiplication
                    sum_value += approximate_multiply(kernel[m, n], image[i - m + k_center_y, j - n + k_center_x])

            # Set the smoothed pixel value
            smoothed_image[i, j] = sum_value

    # Clip the values to stay within valid pixel range
    smoothed_image = np.clip(smoothed_image, 0, 255).astype(np.uint8)

    return smoothed_image

# Load the image
image = cv2.imread('butterfly.jpg', cv2.IMREAD_GRAYSCALE)

# Smooth the image
smoothed_image = smooth_image(image, kernel_size, approximate_multiply)

# Define the region of interest (ROI) for a specific portion
# Adjust the coordinates and size as needed
x_start, y_start, width, height = 50, 100, 100, 100

# Crop the ROI from the smoothed image
roi = smoothed_image[y_start:y_start + height, x_start:x_start + width]

# Use Matplotlib to display the original image, smoothed image, and ROI
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Smoothed Image
plt.subplot(1, 3, 2)
plt.imshow(smoothed_image, cmap='gray')
plt.title('Smoothed Image')
plt.axis('off')

# ROI
plt.subplot(1, 3, 3)
plt.imshow(roi, cmap='gray')
plt.title('Zoomed-in Portion')
plt.axis('off')



# Show the plot
plt.show()
