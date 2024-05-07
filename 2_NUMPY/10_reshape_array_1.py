# reshape function is used to get desire shape of array

import numpy as np
from numpy.core.fromnumeric import reshape
# 1D to 2D reshape
A = np.array([1,2,3,4,5,6,7,8,9])
B = A.reshape(3,3)
print(B)
#if we try to conver it into (3,2) array 
# here space is only for 6 element and we
# have 9 elements so it is not possible...
try:
    print(A.reshape(3,2))
except ValueError as e:
    print(e)
    print("matrix is not convertable with your entered matrix")