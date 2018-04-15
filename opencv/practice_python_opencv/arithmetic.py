from __future__ import print_function
import numpy as np
import cv2

image = cv2.imread("./images/others/002.jpg")
cv2.imshow("Original", image)

print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)

M = np.ones(image.shape, dtype = "uint8") * 50
subtractred = cv2.subtract(image, M)
cv2.imshow("Subtractred", subtractred)
cv2.waitKey(0)
