# PROGRAM 13 :- 
# Write a program to find Highest Common Factor(HCF) and
# Greatest Common Divisor(GCD) of two numbers using function.

# function define
def find_hcf(a,b):
    l = []
    if a>b:
        small = b
    else:
        small = a
    for i in range(1,small+1):
        if(a%i == 0) and (b%i == 0):
            hcf = i
            l.append(i)
        print('all factors of these two numbers',l)
    return hcf

# take input
num1 = int(input("enter 1st number "))
num2 = int(input("enter 2nd number "))
print(f"hcf of {num1} and {num2} is :- " , find_hcf(num1,num2))