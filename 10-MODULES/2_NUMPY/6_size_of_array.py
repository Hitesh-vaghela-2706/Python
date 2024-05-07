import numpy as np

# size is used to count number of elements in array

A = np.array([1,3,5,87,7,87,0,5,4,8,93,79,2,72,9,2,97,23,80,23,68,4])
print(A.size) #return the count oof  all elements in array
B = A.nbytes # total size of array in bytes
print(B)
C = A.itemsize # size of one element in array
print(C)
# hence total size = itemsize*size
# A.size*A.itemsize == A.nbyte