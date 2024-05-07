# histogram graph making
import random
import numpy as np
# print(numpy.verion)
x = np.random.randint(1,100,50)
print(x)

import matplotlib.pyplot as plt
plt.hist(x,10,rwidth=0.9)#25 is thambhla number
plt.show()