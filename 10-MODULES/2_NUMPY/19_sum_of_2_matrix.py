import numpy as np

#  sum of matrix using list:
a = [1,5]
b = [4,8]
c = a + b 
print(c)# it returns the concetanated list not a sum of list

#  sum of matrix using numpu array
A = np.array(a)
B = np.array(b)
C = A + B
print(C)