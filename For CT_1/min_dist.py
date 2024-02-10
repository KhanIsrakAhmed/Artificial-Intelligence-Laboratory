'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    11-02-2024     *************************  '''

#Given two 2d numpy arrays each representing a set of 2D points. Find out the minimum distance between two corresponding pair and its index.

import numpy as np

a = np.array([[1, 1],
              [2, 2],
              [1, 3],
              [4, 3]])

b = np.array([[1, -1],
              [5, 2],
              [2, 3],
              [-1, 0]])



# from matplotlib import pyplot as plt

# x = np.array([0.5, 1, 1.5, 2, 2.5, 3.5, 3.75, 4.25])
# y = x**3

# plt.scatter(x, y, color="red", s=120, marker='*')
# plt.plot(x, y)
# plt.show()