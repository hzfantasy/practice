import unittest
import glob
# from PIL import Image
from image_compare import ImgMatcher


class MatcherTest(unittest.TestCase):
    def setUp(self):
        self.matcher = ImgMatcher("./images/0.png")
        self.icon_resolution = "1440X2880"
        self.find_resolution = "1440X2880"

    # def find_test(self, icon_file, true_list):
    #     icon = "./images/" + self.icon_resolution + "/icons/" + icon_file
    #     matcher = ImgMatcher(icon)
    #     test_images = glob.glob("./images/tests/" + self.find_resolution + "/*.png")
    #     for img in test_images:
    #         print "Find " + icon + " in " + img
    #         print matcher.find_in(img)
    #         if img in true_list:
    #             self.assertEqual(matcher.find_in(img), True)
    #         else:
    #             self.assertEqual(matcher.find_in(img), True)
    #
    #         # assert matcher.find(img)
    #
    # def test_find_assignment(self):
    #     icon = "./images/" + self.icon_resolution + "/icons/assignment.png"
    #     matcher = ImgMatcher(icon)
    #     test_images = glob.glob("./images/tests/" + self.find_resolution + "/*.png")
    #     for img in test_images:
    #         print "Find " + icon + " in " + img
    #         print matcher.find_in(img)
    #         # assert matcher.find(img)

    def test_find_audio(self):
        matcher = ImgMatcher("./images/1125X2436/Untitled.png")
        test_images = glob.glob("./images/tests/1125X2436/2018*.png")
        for img in test_images:
            print "FIND in " + img
            print matcher.find_in(img)


if __name__ == "__main__":
    unittest.main()
