# PROGRAM 12 :- 
# Write a Python program to check if the number provided
# by the user is a palindrome or not using user defined function.

def palindrome(number):
    temp = number
    reverse = 0
    while(number>0):
        digit = number%10
        reverse = reverse*10 + digit
        number//=10
    if(temp==reverse):
        print("palindrome")
    else:
        print("not palindrome")  
A = int(input("enter a number"))
print(palindrome(A))


# range of palindrom
def palindrome(strt,end):
    L = []
    for number in range(strt,end):
        temp = number
        reverse = 0
        while(number>0):
            digit = number%10
            reverse = reverse*10 + digit
            number//=10
        if(temp==reverse):
            L.append(temp)
    return L
strt = int(input("enter a start number"))
end = int(input("enter a end number"))
print(palindrome(strt=strt,end=end))