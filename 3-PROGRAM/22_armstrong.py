''' 
write a program to check
whether a given number 
is armstrong number or not
'''
num = int(input("enter a number"))
# calculated length of number(no.of digits)
order = len(str(num))
#initial sum
sum = 0
# find sum of cube of each digit
temp = num
while temp>0:
    digit = temp%10
    sum += digit**order
    temp//= 10
#display result
if num==sum:
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")


