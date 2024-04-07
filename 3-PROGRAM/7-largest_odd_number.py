# PROGRAM 7 :-
# Write a program which will allow user to enter 10 numbers 
# and display largest odd number from them.
# It will display appropriate message in case 
# if no odd number is found and display count of odd numbers. 


ODD=0
MAX_ODD_NUMBER=0
for i in range(0,10):
    inp = int(input("ENTER THE NUMBER"))
    if inp%2 != 0:
        ODD += 1
        if inp > MAX_ODD_NUMBER :
            MAX_ODD_NUMBER = inp

if MAX_ODD_NUMBER==0:
    print("NO ODD NUMBERS FOUND!!!")
else:
    print("LARGEST ODD NO IN INPUT IS::",MAX_ODD_NUMBER)
    print("TOTAL ODD NUMBERS IN INPUT::",ODD)