# 1D array access and change value of element

# note indexing is starting in array from 0.
import numpy as np

print("\n")
A = np.array([1,3,4,7])
print("1D array req. element is :-\n ",A[3]) # returns avalue at index 3

print("\n")
A[3] = 5
print("1D array is :-\n ",A) # value at index 3 is changed from 7 to 5

# 2D array access and change element value 

print("\n")
A = np.array([ [1,2,3],[4,5,6],[7,8,9] ])
print("2D arrays req. element is :-\n ",A[1,2]) # returns value at row 1 and column 2

print("\n")
A[2,1] = 10
print("2D array is :-\n ",A) # value at row 2 and colun 1 is changed from 8 to 10