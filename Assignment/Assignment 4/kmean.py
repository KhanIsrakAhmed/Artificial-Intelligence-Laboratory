import numpy as np
import matplotlib.pyplot as plt


X = np.loadtxt(
    'd:/GItHub/Artificial-Intelligence-Laboratory/Assignment/Assignment 4/jain_feats.txt')
centroid_old = np.loadtxt(
    'd:/GItHub/Artificial-Intelligence-Laboratory/Assignment/Assignment 4/jain_centers.txt')
centroid_new = np.zeros([2, 2])

plt.scatter(X[:, 0], X[:, 1], s=10, color='blue')
plt.scatter(centroid_old[:, 0], centroid_old[:, 1],
            marker='*', s=250, color='orange')
plt.show()

label = np.empty(X.shape[0])
for e in range(100):
    for i in range(X.shape[0]):
        dist = np.empty(centroid_old.shape[0])
        for j in range(centroid_old.shape[0]):
            dist[j] = np.sqrt(np.sum((X[i] - centroid_old[j])**2))
        label[i] = np.argmin(dist)

    for j in range(centroid_new.shape[0]):
        centroid_new[j] = np.average(X[label == j], axis=0)

    if np.max(np.abs(centroid_new - centroid_old)) < 1e-7:
        break
    else:
        centroid_old = np.copy(centroid_new)

plt.scatter(X[label == 0, 0], X[label == 0, 1], s=10, color='red')
plt.scatter(X[label == 1, 0], X[label == 1, 1], s=10, color='green')
plt.scatter(centroid_old[0, 0], centroid_old[0, 1],marker='*', s=250, color='red')
plt.scatter(centroid_old[1, 0], centroid_old[1, 1],marker='*', s=250, color='green')
plt.show()
