# import the necessary packages
import argparse
import cv2

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="path to the input image")
# ap.add_argument("-c", "--cascade", default="/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalcatface_extended.xml", help="path to cat detector haar cascade")
# args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread('./images/cat005.jpg') #args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the cat detector Haar cascade, then detect cat faces
# in the input image
detector = cv2.CascadeClassifier("/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalcatface_extended.xml") #args["cascade"])
rects = detector.detectMultiScale(gray, 1.3, 5) # scaleFactor=1.3, minNeighbors=10, minSize=(75, 75))


# loop over the cat faces and draw a rectangle surrounding each
for (i, (x, y, w, h)) in enumerate(rects):
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

# show the detected cat faces
cv2.imshow("Cat Faces", image)
cv2.waitKey(0)