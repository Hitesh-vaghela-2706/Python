# PROGRAM 3 :-
# Ram wants to know age of his grandfather, who was born on 18th December, 1950. 
# Kindly help ram to know how old is his grandfather? Also, print the calendar for the 
# month and year on which ram’s grandfather was born

# Python3 code to  calculate age in years
 

from datetime import date

def Age(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ( (today.month, today.day) < (birthDate.month, birthDate.day) )
    return age


date_of_birth = int(input("Enter a Date of birth :-  "))
month_of_birth = int(input("Enter a Month of birth :-  "))
year_of_birth = int(input("Enter a Year of birth :-  "))

Final_date = date(year_of_birth,month_of_birth,date_of_birth,) 

# driver code
print(Age(Final_date), "years old in" , date.today().year)