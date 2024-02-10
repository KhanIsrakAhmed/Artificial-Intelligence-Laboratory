'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    11-02-2024     *************************  '''
#Find out the sum of all corresponding pairs between two numpy arrays if multiplication of the pair is positive
import numpy as np


a = np.array([3, -5, 2, -8])
b = np.array([4, -7, -3, 6])


multiplication_result = a * b


positive_multiplications = multiplication_result[multiplication_result > 0]


sum_of_positive_multiplications = np.sum(positive_multiplications)


print("a:", a,end='\t\t')
print("b:", b)
print("Multiplication result:", multiplication_result)
print("Positive multiplications:", positive_multiplications)
print("Sum of positive multiplications:", sum_of_positive_multiplications)
