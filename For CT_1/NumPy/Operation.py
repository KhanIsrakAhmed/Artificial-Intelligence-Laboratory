import numpy as np

# a = np.array([[1, 5, 3],
#               [4, 2, 6]])

# b = np.array([[9, 2, 1],
#               [6, 1, 1]])

# print(a+b)
# print(a-b)
# print(a.shape)
# print(b.shape)
# print(a*b)
# print(a/b)


# a = np.array([[1, 2, 3],
#               [4, 5, 6]])

# b = np.array([[1, 2, 3],
#               [4, 5, 6]])

# print(b.T)
# print(b.T.shape)
# print(np.matmul(a, b.T))

# a = np.array([21, 2, -35, -4, 5, 66, -72, 8, 90])

# b = np.array([[1, 4],
#               [6, 2],
#               [3, 10]])

# print(a.argmax()) # find maximum element index
# print(b.argmax())
# print("Column wise:", b.argmax(axis=0))
# print("Raw wise:", b.argmax(axis=1))

# b = np.array([[1, 4, 9, 10],
#               [6, 2, -1, -8],
#               [3, -5, 2, 15],
#               [31, 5, 12, -5]])

# print(b[1][2]) # access value like array
# print(b[0:2]) # first two raw
# print(b[0:2, :]) # first two raw
# print(b[:,0:2]) #first to col
# print(b[:,1:3]) # col from 1 to 2
# print(b[:, -1])  # last column
# print(b[:,-2:]) # last 2 col
# print(b[:, 2:])  # last two col
# print(b[1:3, 1:4])  # middle 4 elements

# converting 1D array to 2D array
# a = np.array([3, -5, 2, -8, 9, 0, 7])

# print(a.shape)

# print(a.reshape((1, 7)))
# print(a.reshape((7, 1)))

# b = np.array([1, 2, 3, 4])
# print(b.reshape(2,2))
# print(b.reshape(2,2).T)

# a = np.array([1, -5, 3, -2, 4,])
# print(a[[True, False, True, False, True]])
# print(a > 0)
# print("a[a>5]", a[a > 0])
# print("a[a<2]", a[a < 0])

from matplotlib import pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = x**2

plt.scatter(x, y, color="black")
plt.plot(x, y)
plt.show()
