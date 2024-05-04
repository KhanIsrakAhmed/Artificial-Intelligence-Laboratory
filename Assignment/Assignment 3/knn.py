import pandas as pd
import numpy as np
import math

path = 'd:/GItHub/Artificial-Intelligence-Laboratory/Assignment/Assignment 3/iris.csv'

def load_data(path):
    df = pd.read_csv(path)
    X = np.array(df[df.columns[2:]].values)
    y = np.array(df[[str(df.columns[0])]].values.flatten())
    return X, y

def split_data(X_shuffled, y_shuffled, train_ratio=0.8):
    M = int(train_ratio * len(y_shuffled))
    X_train = X_shuffled[:M]
    y_train = y_shuffled[:M]
    X_test = X_shuffled[M:]
    y_test = y_shuffled[M:]
    return X_train, y_train, X_test, y_test

def euclidean_distance(x_test, X_train):
    distances = np.sqrt(np.sum((X_train - x_test)**2, axis=1))
    return distances

def predict_labels(distances, y_train, k=5):
    nearest_indices = np.argsort(distances)[:k]
    nearest_labels = y_train[nearest_indices]
    predicted_label = np.argmax(np.bincount(nearest_labels))
    return predicted_label

def knn_classifier(X_train, y_train, X_test, k=5):
    y_test_predicted = np.empty(len(X_test))
    for i, x_test in enumerate(X_test):
        distances = euclidean_distance(x_test, X_train)
        y_test_predicted[i] = predict_labels(distances, y_train, k)
    return y_test_predicted

def evaluate_accuracy(y_test, y_test_predicted):
    accurate = np.sum(y_test == y_test_predicted)
    return accurate

X, y = load_data(path)

shuffled_indices = np.random.permutation(len(y))
X_shuffled = X[shuffled_indices]
y_shuffled = y[shuffled_indices]

X_train, y_train, X_test, y_test = split_data(X_shuffled, y_shuffled)

k = 5
y_test_predicted = knn_classifier(X_train, y_train, X_test, k)

accurate = evaluate_accuracy(y_test, y_test_predicted)
M_prime = len(y_test)
print('Total number of Test Data =', M_prime)
print('Total number of Accurate Data =', accurate)
print("ACCURACY of the Model =", str(float(accurate/M_prime)*100) + "%")


# Total number of Test Data = 30
# Total number of Accurate Data = 29
# ACCURACY of the Model = 96.66666666666667%