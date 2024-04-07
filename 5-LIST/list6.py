# Python program to find Sum of number digits in List
# The original list is : [12, 67, 98, 34]
# Ans is :- List Integer Summation : [3, 13, 17, 7]

A = [12,67,98,34]
C = []
for i in A:
    B = str(i)
    sum = 0
    for j in range(len(B)):
        sum += int(B[j])
    C.append(sum)
print(C)