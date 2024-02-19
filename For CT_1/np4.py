'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    17-02-2024     *************************  '''


import numpy as np
List = ['A', 'B','A', 'C','B', 'A','B','C']

uniquelist,cnt = np.unique(List,return_counts= True)

print (uniquelist,'->',cnt)


print(np.arange(1,10,3))

print(np.arange(10,5,-2))


print(np.linspace(5,20,4))

print(np.eye(3))