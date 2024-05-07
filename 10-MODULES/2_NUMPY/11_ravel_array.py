# ravel is use to reshape (n,m) array into one daimantion array
import numpy as np
A = np.array( [ [1,2,3,4,5,6],[1,2,3,4,5,6],
[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6] ] )
print(A)
print(A.shape) # it is (5,6) array
B = A.ravel()
print(B)