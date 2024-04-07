# PROGRAM 5 :-
# Suppose you want to develop a program to play a lottery.
# The program randomly generates a two-digit number,
# prompts the user to enter a two-digit number, and 
# determines whether the user wins according to the following rules: 
# a) If the user’s input matches the lottery in the exact order, the award is 10,000 INR. 
# b) If all the digits in the user’s input match all the digits in the lottery number, the 
# award is 3,000 INR.
# c) If one digit in the user’s input matches a digit in the lottery number, the award is 
# 1,000 INR


# generating a random number
import random
A = random.randint(10,99)


#spliting random number
temp = A # if A = 75 then...
first_digit_of_Genereted_Number = temp%10 # X = 5 
temp //= 10 
Second_digit_of_Genereted_Number = temp # Y = 7


# take number from user
B = int(input("enter a two digit number"))


# reversing user input number and spliting user number didits
temp1 = B
first_digit_of_User_input_Number = temp1%10 
temp1 //= 10
Second_digit_of_User_input_Number = temp1
D = first_digit_of_User_input_Number*10 + Second_digit_of_User_input_Number





# code for given condition
if A == B :
    print("congrgatulations you win 10,000 INR")
elif A == D :
    print("congratulation you win 3000 INR")
elif first_digit_of_User_input_Number  == first_digit_of_Genereted_Number or \
    first_digit_of_User_input_Number == Second_digit_of_Genereted_Number or \
    Second_digit_of_User_input_Number == first_digit_of_Genereted_Number or \
    Second_digit_of_User_input_Number == Second_digit_of_Genereted_Number:
    print("congratulation you win 1000 INR")
else :
    print("no match found your bad luck try again! ")


print("lucky number is :- ",A)