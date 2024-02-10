'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    10-02-2024     *************************  '''


import numpy as np

a = np.array([3, -5, 2, -8, 9, 0, 7])

print("a =", a)

print( a[[True, False, False, True, True, False, True]])

print("if (a>5))  ---->>>", a>5)

print("if (a>5))  ---->>>", a[a>5]) #values

print("a[a<2]", a<2)
print("a[a<2]", a[a<2])