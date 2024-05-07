import numpy as np
import matplotlib.pyplot as plt
A = np.random.normal(10.0,2.0,100000)
plt.hist(A,100)
plt.show()