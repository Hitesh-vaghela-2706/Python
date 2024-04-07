# reduce function is used to reduce data
from functools import reduce
list = [3,6,8,7,4]
sum = lambda a,b :a+b
red = reduce(sum,list)
print(red)

def max(a,b):
    if a>b:
        return a
    else:
        return b
A = reduce(max,list)
print(A)

def avg(a,b):
    return (a+b)/2
B = reduce(avg,list)
print(B)