# max in 4 numbers
num1  = int(input("enter a number1  \n"))
num2  = int(input("enter a number2  \n"))
num3  = int(input("enter a number3  \n"))
num4  = int(input("enter a number4  \n"))
if(num1>num2):
    A = num1
else:
    A = num2
if(num3>num4):
    B = num3
else:
    B = num4
if(A>B):
    print("gretest number is",A)
else:
    print("gretest number is",B)  

# max in 3 numbers
num1  = int(input("enter a number1  \n"))
num2  = int(input("enter a number2  \n"))
num3  = int(input("enter a number3  \n"))

if(num1>num2):
    if num1 > num3:
        print("gretest number is",num1)
    else:
        print("gretest number is",num3)
else:
    if num2 > num3:
        print("gretest number is",num2)
    else:
        print("gretest number is",num3) 