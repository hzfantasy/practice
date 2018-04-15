import cv2
import numpy as np
import sys


class ImgMatcher:
    def __init__(self, source_img):
        self.source_img = source_img

    # compare with image
    def find_in(self, template_img, threshold=0.98):
        image = cv2.imread(self.source_img)
        template = cv2.imread(template_img)
        result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        similarity = cv2.minMaxLoc(result)[1]

        if similarity < threshold:
            print similarity
            return similarity
        else:
            print similarity
            coordinates = np.unravel_index(result.argmax(), result.shape)
            print coordinates
            return coordinates


if __name__ == "__main__":
    source_image = sys.argv[1]
    check_image = sys.argv[2]
    threshold_str = sys.argv[3]

    # print source_image
    # print check_image
    matcher = ImgMatcher(source_image)
    matcher.find_in(check_image, float(threshold_str))
