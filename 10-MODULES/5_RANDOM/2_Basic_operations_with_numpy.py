import random
import numpy as np
X = np.random.uniform(1.3,7.8,8)
print(X)
X = np.random.random(5)
print(X)
X = np.random.randint(2,89,16)
print(X)
X = random.randrange(1,7)
print(X)
A = [3,4,5,6,7,8]
X = np.random.choice(A,5)
print(X)
np.random.seed(4)
A = np.random.randint(1,50,10)
print(A)
A = np.random.normal(10,2,100)
print(A)

