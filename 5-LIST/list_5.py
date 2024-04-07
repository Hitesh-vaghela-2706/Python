# write a python program to find 
# smalllest and largest number in list

# using built in function
A = [2,5,8,56,34,57,567,79,976]
print(min(A))
print(max(A))

# using another built in function
A = [1,4,5,2,7,8]
A = sorted(A)
B = len(A)
print("min number is",A[0])
print("max number is",A[B-1])

# using sort()function :-
A = [9,12,3,8,10]
A.sort()
print(A)
B = len(A)
print("min number is ",A[0])
print("max number is ",A[B-1])

# using for loop
A = [1,2,3]
temp1 = 0
for i in A :
    if(i>temp1):
        temp1 = i
print("max num is ",temp1)
temp2 = A[0]
for i in A :
    if(i<temp2):
        temp2 = i
print("min number is",temp2)        