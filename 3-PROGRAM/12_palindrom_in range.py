# PROGRAM 12 :-
# Write a Python program to print all Palindrom numbers 
# in an Interval using user defined function.


A = int(input("lower range"))
B = int(input("higher range"))  
for num in range(A,B):
    reverse = 0
    temp = num
    while(num>0): 
        digit = num%10
        reverse = reverse*10 + digit
        num//=10
    if(temp==reverse):
        print(temp)
