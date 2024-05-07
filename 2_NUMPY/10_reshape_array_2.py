import numpy as np
# (n,m) array conversation into (x,y)
# 2D to 2D reshape
print("\n")
A = np.array( [ [1,2,4],[2,6,8],[6,7,3],[3,7,1] ])
print(A)
print(A.shape)
B = A.reshape(3,4) # coverts (4,3) array into (3,4) array
print(B)
print(B.shape)