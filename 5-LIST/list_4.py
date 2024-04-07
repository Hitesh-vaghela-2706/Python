# write a python program to find sum of all element in list

# using sum built-in function
A = [38,3,3,34,6,8,65,87,5,3,4]
print(sum(A))

# using for loop:-
A = [3,5,7,9,2,6]
sum = 0
for i in A :
    sum = sum + i
print(sum)

# using while loop
A = [3,6,9,12,15]
B = len(A)
i = 0
sum = 0
while(i<B):
    sum = sum + A[i]
    i = i + 1
print(sum)

# other way
A = [4,7,9]
print(A[0]+A[1]+A[2])