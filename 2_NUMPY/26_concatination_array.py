import numpy as np


# concatenation in one dimention array
A = np.array([1,2,3])
B = np.array([5,6,7])
D = np.array([5,7,9])

C = np.concatenate([A,B]) # combines two arrays
print(C)
# also possible to concate more than two arrays
E = np.concatenate([A,B,D])
print(E)

# concatenation in two dimention array
X = np.array([[1,3,5],[2,6,8]])
Y = np.concatenate([X,X])
print(Y) # bydefault concatinate on axis = 0
Y = np.concatenate([X,X],axis=1)
print(Y)