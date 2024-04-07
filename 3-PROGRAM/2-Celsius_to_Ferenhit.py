# PROGRAM 2 :-
# Write a Python Program to Convert Celsius to Fahrenheit and vice –a-versa. 
# F=1.8*C+32

print("TYPE 1 TO CONVERT CELSIUS TO FAHRENHEIT :-")
print("TYPE 2 TO CONVERT FAHRENHEIT TO  CELSIOUS :-")

ch = input("PLEASE ENTER THE CHOICE:") 
if ch == "1" :
    C = float(input("ENTER THE TEMPERATURE::"))
    print("TEMPERATURE IN FAHRENHEIT",(1.8*C)+32)
elif ch =="2":
    F = float(input("ENTER THE TEMPERATURE::"))
    print("TEMPERATURE IN FAHRENHEIT",(F-32)/1.8)
else:
    print("ENTER  THE RIGHT CHOICE..")
