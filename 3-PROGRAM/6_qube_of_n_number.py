def sum_of_square(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i*i)
    return sum
num = int(input("enter a number :- "))
print(sum_of_square(num))