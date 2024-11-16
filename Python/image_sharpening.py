import numpy as np
import cv2
import matplotlib.pyplot as plt

# Define the kernel G
G = np.array([
    [1,  4,  7,  4,  1],
    [4, 16, 26, 16,  4],
    [7, 26, 41, 26,  7],
    [4, 16, 26, 16,  4],
    [1,  4,  7,  4,  1]
])

# Define the approximate multiplier function
# def approximate_multiply(a, b):
#     # Placeholder for an approximate multiplication function
#     # Replace this with your actual approximation logic
#     return a * b  # This is exact multiplication, replace with your logic

# Image sharpening function
def sharpen_image(image, G):
    # Get the dimensions of the image and kernel
    rows, cols = image.shape
    k_rows, k_cols = G.shape
    k_center_x = k_cols // 2
    k_center_y = k_rows // 2

    # Create an output image
    sharpened_image = np.zeros_like(image, dtype=np.float64)

    # Convolve the kernel over the image
    for i in range(k_center_y, rows - k_center_y):
        for j in range(k_center_x, cols - k_center_x):
            sum_value = 0.0
            for m in range(k_rows):
                for n in range(k_cols):
                    # Apply the approximate multiplication
                    sum_value += approximate_multiply(G[m, n], image[i - m + k_center_y, j - n + k_center_x])

            # Subtract the convolved value from twice the original pixel
            sharpened_image[i, j] = 2 * image[i, j] - (1 / 273) * sum_value
            #print(sharpened_image)
    # Clip the values to stay within valid pixel range
    sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)

    return sharpened_image

# Load the image
image = cv2.imread('img1.png', cv2.IMREAD_GRAYSCALE)

# Sharpen the image
sharpened_image = sharpen_image(image, G)

# Use Matplotlib to display and save the image
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
#plt.axis('off')

# Sharpened Image
plt.subplot(1, 2, 2)
plt.imshow(sharpened_image, cmap='gray')
plt.title('Sharpened Image')
#plt.axis('off')

# Save the sharpened image
plt.savefig('sharpened_image.png', bbox_inches='tight', pad_inches=0)

# Show the plot
plt.show()
