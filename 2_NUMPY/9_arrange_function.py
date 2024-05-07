# arrange function used to create 1D array 
# value of array is number of given range
# numbers are integer only

import numpy as np
A = np.arange(12)
print(A) # create 1D array with element 0 to 11 
# not include 12
A = np.arange(4,13,dtype=np.int32)
print(A) # create 1D array with element 4 to 12
A = np.arange(4,34,2)
print(A) # create 1D array with element 4 to 33 
# with skip value 2
A = np.empty(4)
print(A)# create 1D array with any existing 4 values