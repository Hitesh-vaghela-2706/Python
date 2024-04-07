# PROGRAM 9 :-
# Write a Python program to check if the number 
# provided by the user is a palindrome or not.

print("without user defined function")
n=int(input("Enter number to check if it is palidrome or not :"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

print("using user defined function")
def ispalindrom(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")
# taking number and checking
A = int(input("enter a number"))
print(ispalindrom(A))