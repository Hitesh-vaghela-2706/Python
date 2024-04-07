# PROGRAM 11 :-
# Write a Python program to find factorial of a number using user defined function

def recur_factorial(n):
    if(n==1):
        return n
    else:
        return n*recur_factorial(n-1)    
num = int(input("enter a number"))
if(num<0):
    print("factorial does not exists for negetive number ")
elif(num==0):
    print("factorial of 0 is 1")
else:
    print("factorial is :- ",recur_factorial(num))