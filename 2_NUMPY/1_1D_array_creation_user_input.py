import numpy as np

#without loop 1d array , manually insdert every element:

a = []
a.insert(0,5)
a.insert(1,6)
a.insert(2,3)
print('list',a)
b = np.array(a)
print('array',b)

# using loop 1d array
print('enter how many number u want to add  in array')
A = int(input("enter a number \n"))
C = []
for i in range(0,A):
    B = int(input("enter a value which you ewant to insert"))
    C.insert(i,B)
print('list',C)
print("array",np.array(C))
