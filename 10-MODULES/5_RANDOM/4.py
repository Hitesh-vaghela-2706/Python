import numpy as np
import random as r
c=0
for i in range(1,11):
    A = np.random.randint(1,21)
    B = np.random.randint(1,21)
    if A==B:
        c = c+1
print(c)