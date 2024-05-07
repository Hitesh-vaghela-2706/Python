# each dot with different color
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,3,6,7,8,9,4,5])
y = np.array([3,5,6,8,5,9,3,4,])

A = np.array(['red','orange','magenta','magenta','magenta','magenta','magenta','magenta'])
plt.scatter(x,y,c=A)
plt.show()