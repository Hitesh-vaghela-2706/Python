import numpy as np
# one daimantion array = axis called axis0
# two daimantion array raw called axis0 column called axis1
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A)
print("sum of axis 1",A.sum(axis=1)) # returns [sum of r0,sum of r1,sum of r2]
print("sum of axis 0",A.sum(axis=0)) # returns [sum of c0,sum of c1,sum of c2]

# for example :
#  a   x    i    s =  1
#  x
#  i   1    2    3    6
#  s   4    5    6    15
#  =   7    8    9    24
#  0   12   15   18
