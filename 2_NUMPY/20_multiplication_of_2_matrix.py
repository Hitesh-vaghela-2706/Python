import numpy as np

# multiplication of matrix using list
try:
    C = [2,4]*[3,5]
    print(C)
except TypeError as e:
    print( " can't multiply list in python")
    
# multilpiction of mateix using numpy array
A = np.array( [ [2,3],[4,5] ] )
B = np.array( [ [6,7],[8,9] ] )
C = A*B
print(C)