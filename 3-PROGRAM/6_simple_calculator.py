# PROGRAM 6 :- 
# Write a program in python to implement simple calculator.

print("Please type in the math operation you would like to complete")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
operation = input(  " enter a operation :- ")

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == '+':
    print("a+b=",number_1 + number_2)
elif operation == '-':
        print("a-b=",number_1 - number_2)
elif operation == '*':
    print("a*b=",number_1 * number_2)
elif operation == '/':
    print("a/b=",number_1 / number_2)
else:
    print('You have not typed a valid operator, please run the program again.')