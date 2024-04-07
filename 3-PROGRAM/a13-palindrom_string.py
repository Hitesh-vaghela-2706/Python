# PROGRAM 13 :- 
# Write a Python program to check if the string provided
# by the user is a palindrome or not using user defined function.

def palindrom_string(str):
    b = ""       
    for i in str:
        b = i + b
    if(str==b):
        result = True
    else:
        result = False
    return result
a = input("enter a string :- ")
result = palindrom_string(a)
if result:
    print("yes it is palindrome ")
else:
    print("no it is not palindrome ")


# second method
def palindrom_string_reverse(str):
    new_str = str[::-1]
    if str == new_str:
        result = True
    else:
        result = False
    return result
a = input("enter a string")

result = palindrom_string_reverse(a)
if result:
    print("yes it is palindrome ")
else:
    print("no it is not palindrome ")