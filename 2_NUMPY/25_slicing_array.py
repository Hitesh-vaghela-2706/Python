import numpy as np
A = np.arange(1,10)
print(A)
B = A.reshape(3,3) # creatind 2D 3*3 array
print(B)

# slicing in one dimentional array

print(A[4]) # returns a value of array at 4th index
# index is start from zero in array
print(A[-3]) # return a value at index -3
# - indexing is start from end of array from -1
print(A[2:7]) # returns a value between index 2 to 7 include index 2
print(A[2:7:2]) # returns a every second value between index 2 to 7 include index 2 
 
# slicing in two dimentional array
print(B[1,2])
print(B[:1,:2]) # return 0th row with 0&1 column
print(B[:,2]) # prints column with index 2
print(B[1,:]) # prints row with index 1
print(B[:,::2]) # return every second column and all row
print(B[::2,:]) # return every second row and all column
print(B[::2,::2]) # return every second row and every second column