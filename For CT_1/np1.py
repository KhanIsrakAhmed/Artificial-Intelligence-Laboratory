'''   ****************  Author :  Khan Israk Ahmed  *************************  '''
'''     ****************  Date:    10-02-2024     *************************  '''


import numpy as np
from matplotlib import pyplot as plt
x = np.array([0.5,1,1.5,2,2.5,3.5,3.75,4.25])
y = x**3

plt.scatter(x, y, color="red", s=120, marker='*')
plt.plot(x, y)
plt.show()