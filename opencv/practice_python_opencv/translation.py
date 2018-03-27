import argparse
from practice_python_opencv import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
temp = ap.parse_args()
args = vars(ap.parse_args())

image = cv2.imread("./images/others/002.jpg")
cv2.imshow("Original", image)

# M = np.float32([[1, 0, 25], [0, 1, 50]])
# shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
# cv2.imshow("Shifted Down and Right", shifted)
# cv2.waitKey(0)
#
# M = np.float32([[1, 0, -50], [0, 1, -90]])
# shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
# cv2.imshow("Shifted Up and Left", shifted)
# cv2.waitKey(0)

shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shift Down", shifted)
cv2.waitKey(0)
