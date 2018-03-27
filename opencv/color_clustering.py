from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True, help = "Path to the image")
# ap.add_argument("-c", "--clusters", required = True, type = int, help = '# of cluster')
# args = vars(ap.parse_args())

image = cv2.imread("./images/light_green1.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure()
plt.axis("off")
plt.imshow(image)

image = image.reshape((image.shape[0] * image.shape[1], 3))

# clt = KMeans(n_clusters = args["clusters"])
clt = KMeans(3)
clt.fit(image)

hist = utils.centroid_histogram(clt)
bar = utils.plot_colors(hist, clt.cluster_centers_)

plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()
