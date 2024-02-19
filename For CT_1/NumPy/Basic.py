import numpy as np

a = np.array([10, 50, 30, 40])
# print(a)

b = np.array([[3, 2, 1],
              [4, 9, 6],
              [8, 5, 7]])
# print(b)

# print(a.shape)
# print(b.shape)
# r,c = b.shape
# print(r,c)

# print(a.max())
# print(b.max())

# print("Column wise:", b.max(axis=0))
# print("Raw wise:", b.max(axis=1))

# print("Column sum:", b.sum(axis=0))
# print("Raw wise sum:", b.sum(axis=1))

# print("Column wise mean:", b.mean(axis=0))
# print("Raw wise mean:", b.mean(axis=1))

# print (a.max(),b.max())
# print (a.min(),b.min())
# print (a.min()-b.max())
# print ("column wise max", b.max(axis=0))
# print("Raw wise min", b.min(axis=1))
i= b.sum(axis=0)
print ("column wise sum", i)

print ("column wise mean ", b.mean(axis=0))
