'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    10-02-2024     *************************  '''

import numpy as np

a = np.array([21,2,-35,-4,23,66,-72,8,9])

b = np.array([[1, 4],
              [6, 2],
              [3, 5]])

print(a.argmax())
print(b.argmax())


# print("Column Wise", b.argmax(axis = 0))
# print("Row Wise", b.argmax(axis = 1))
# print("--------------MAX------------------")
# # Broadcasting
# c = np.array(
#     [[1,2],
#      [3,4]]
# )
# d = np.array(
#     [2,3]
# )

# print(c+d)
# print("--------------MAX------------------")
# b = np.array([[1, 4, 9, 10],
#               [6, 2, -1, -8],
#               [3, -5, 2, 15],
#               [31, 5, 12, -5]])

# print(b[1][2])
# print(b[:2]) # first two rows
# print(b[0:2, :]) # first two rows
# print(b[:, 1:3],end='\n\n') # middle two columns
# print(b[:, -1],end='\n\n') # last column
# print(b[:, -1:],end='\n\n') # last column
# print(b[:, 3:]) # last column
# print(b[:, -2:]) # last two columns
# print(b[:, 2:]) # after first two columns
# print(b[1:3, 1:4]) # middle 4 elements