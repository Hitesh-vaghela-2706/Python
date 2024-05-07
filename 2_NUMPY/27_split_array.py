import numpy as np
A = np.arange(11)
B,C,D = np.split(A,[3,7])
print(B,C,D,"\n")

X = np.arange(16).reshape((4,4))
upper,lower = np.vsplit(X,[1]) # 1 is a index of row from where we want to split verticaly
print(upper,"\n\n",lower,"\n")
left,right = np.hsplit(X,[2]) # 2 is a index of column from where we want to split horizontaly
print(left,"\n\n",right)