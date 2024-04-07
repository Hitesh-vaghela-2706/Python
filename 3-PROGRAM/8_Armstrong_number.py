# PROGRAM 8 :-
# Write a Python program to check if the number 
# provided by the user is an Armstrong number.

# armstrong number 153 = 1^3 + 5^3 + 3^3

print("without user defined function")
num = int(input("Enter number to check for Armstrong:"))
sum = 0
temp = num
order = len(str(num))
while(num>0):
    digit = num%10
    sum = sum + digit**order
    num//=10
if(sum==temp):
    print("Given number ",temp," is an Armstrong number.")
else:
    print("Given number ",temp," is not an Armstrong number.")

print("using user defined function")
def arm_num(num):
    sum = 0
    temp = num
    order = len(str(num))
    while(num>0):
        digit = num%10
        sum = sum + digit**order
        num//=10
    if(sum==temp):
        print(f"Given number ",temp," is an Armstrong number.")
    else:
        print(f"Given number ",temp," is not an Armstrong number.")
# taking number and check 
A = int(input("enter a number"))
print(arm_num(A))