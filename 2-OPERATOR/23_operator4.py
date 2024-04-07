#write a program to remove last digit from number
a = 123456
#if we want to access last digit
b = a%10
print(b)
# if we want to remove 1 digit
a//=10
print(a)
# if we want to remove 2 digit
a//=100
print(a)
# // also used to get division without reminder
print(3454/3)
b = 3454
b //= 3
print(b)