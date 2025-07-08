import cv2
import matplotlib.pyplot as plt

# Load image from data folder
image = cv2.imread('data/test.jpg')

# Convert BGR to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Show the image
plt.imshow(image_rgb)
plt.title("Test Image")
plt.axis("off")
plt.show()
