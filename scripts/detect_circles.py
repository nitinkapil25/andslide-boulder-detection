import cv2
import numpy as np

# Load image
image = cv2.imread('data/test.jpg')
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur the image to reduce noise
blurred = cv2.medianBlur(gray, 5)

# Apply Hough Circle Transform
circles = cv2.HoughCircles(
    blurred,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=20,
    param1=50,
    param2=30,
    minRadius=5,
    maxRadius=50
)

# If circles are detected
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(output, (x, y), r, (0, 255, 0), 2)
        cv2.circle(output, (x, y), 2, (0, 0, 255), 3)
        # Save final output image with detected boulders
cv2.imwrite('outputs/detected_boulders.jpg', output)


# Show output
cv2.imshow("Detected Circles (Boulders)", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
