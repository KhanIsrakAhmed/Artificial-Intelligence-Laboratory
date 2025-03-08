import pandas as pd
import numpy as np
import math

path = '/Artificial-Intelligence-Laboratory/New folder/iris.csv'

df = pd.read_csv(path)

X = np.array(df[df.columns[2:]].values)
y = np.array(df[[str(df.columns[0])]].values)
X_cols = len(df.columns[2:])

shuffled_indices_list = np.random.permutation(len(y))

X_shuffled = X[shuffled_indices_list]
y_shuffled = y[shuffled_indices_list]

# Number of training rows
M = int(0.8 * len(y))
M_prime = len(y) - M

k = 5
X_train = X_shuffled[:M]
y_train = y_shuffled[:M]
X_test = X_shuffled[M:]
y_test = y_shuffled[M:]

y_test_predicted = np.empty((M_prime))


def euclidean_distance(x_test, X_train, i, j, X_cols):
    result = 0.0
    for m in range(X_cols):
        result += (x_test[i][m] - X_train[j][m]) ** 2
    return math.sqrt(result)


for i in range(M_prime):
    D = np.empty((M, 2))
    for j in range(M):
        distance = euclidean_distance(X_test, X_train, i, j, X_cols)
        D[j] = (distance, int(y_train[j][0]))
    
    y_neighbor = []
    # Loop to find nearest neighbors and update y_neighbor
    for m in range(k):
        min_dist_index = D.argmin(axis=0)[0]
        y_neighbor.append(D[min_dist_index][1])
        # Delete the row corresponding to the minimum distance
        D = np.delete(D, min_dist_index, axis=0)
    
    class_frequency = np.zeros(k)  # 1D numpy array
    for m in range(k):
        class_frequency[int(y_neighbor[m])] += 1
    y_test_predicted[i] = class_frequency.argmax()

# Accuracy
print("Predicted vs. Original")
accurate = 0
for i in range(M_prime):
    print(int(y_test_predicted[i]), " ", y_test[i][0], end="  ")
    print(y_test_predicted[i] == y_test[i][0])
    if y_test_predicted[i] == y_test[i][0]:
        accurate += 1

print('Total number of Test Data = ', str(M_prime))
print('Total number of Accurate Data = ', str(accurate))
print("ACCURACY of the Model = ", str(float(accurate / M_prime) * 100) + "%")
