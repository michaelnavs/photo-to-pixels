import numpy as np
from scipy.io import loadmat
from matplotlib.image import imread
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


def cloudIdentification(filename: str) -> np.ndarray:
    """
    Apply mask to image, use kmeans to cluster clear sky pixels, cloud pixels, and background pixels.
    Return np.ndarray of clear sky pixels in shape of image from filename
    """
    org_img = imread(filename)
    width, height = org_img.shape[0], org_img.shape[1]

    mask = loadmat("./mask.mat")
    mask_arr = np.array(mask["mask"])

    segment_img = org_img.copy()
    for idx, val in np.ndenumerate(mask_arr):
        if val == 0:
            for i in range(3):
                segment_img[idx][i] = 0

    data = np.array(segment_img).reshape((width * height, 3))
    data = data[:, 0] / (data[:, 2])
    data[np.isnan(data)] = 0
    data[np.isinf(data)] = 0

    start_points = np.array([0, 0.5, 0.8, 1]).reshape((-1, 1))
    clf = KMeans(n_clusters=4, init=start_points).fit(data.reshape((-1, 1)))
    clusterImg = np.reshape(clf.labels_, (width, height))

    C = np.array(clf.cluster_centers_)
    ind = C.argsort(axis=0)

    for idx, val in np.ndenumerate(clusterImg):
        if val != ind[1, 0]:
            for i in range(3):
                segment_img[idx][i] = 0

    return segment_img
