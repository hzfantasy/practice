from sklearn.cluster import KMeans
import numpy as np
import argparse
import cv2


def centroid_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
    hist = hist.astype("float")
    hist /= hist.sum()
    return hist


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
ap.add_argument("-k", "--clusters", required=True, help="Number of clusters")
args = vars(ap.parse_args())

k = int(args["clusters"])
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = image.reshape((image.shape[0] * image.shape[1], 3))

clt = KMeans(k)
clt.fit(image)
hist = centroid_histogram(clt)
percentages = list(hist)
colors = list(clt.cluster_centers_)

percentages_mapping = {}
for i in range(len(percentages)):
    percentages_mapping[int(percentages[i]*1000)] = i

colors_percentages_sorted = sorted(percentages_mapping, reverse=True)

colors_sorted = []
for percent in colors_percentages_sorted:
    index = percentages_mapping[percent]
    colors_sorted.append(list(colors[index]))

for color in colors_sorted:
    print(color)
