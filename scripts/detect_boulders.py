import cv2
import numpy as np

# Load image
image = cv2.imread('data/test.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur (optional - to smooth the image)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge Detection
edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

# Find contours (shapes)
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw detected boulders (contours) on the original image
for cnt in contours:
    area = cv2.contourArea(cnt)
    if 100 < area < 1000:  # Filter by size
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show final image with boulder boxes
cv2.imshow("Detected Boulders", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
