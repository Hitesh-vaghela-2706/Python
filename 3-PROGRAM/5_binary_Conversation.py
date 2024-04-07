# PROGRAM 4 :-
# Write a program in python to convert binary, octal, hexadecimal numbers to decimal number and vise-versa.
# (Hint: use int() and Use bin, oct ,hex functions)(Also write it without using built-in function) 

print("TYPE 1 TO SEE CONVERSION FROM DECIMAL TO BINARY,OCTAL,HEXADECIMAL")
print("TYPE 2 TO VICE-VERSA.")
ch = input("PLEASE  ENTER YOUR CHOICE::")
if ch =="1" :          
     dec=int(input("PLEASE ENTER DECIMAL NUMBER:"))
     print(bin(dec)," in Binary")
     print(oct(dec)," in Octal")
     print(hex(dec)," in Hexadecimal")                     
elif ch == "2": 
     print("TYPE b TO SEE CONVERSION FROM BINARY TO DECIMAL ")
     print("TYPE o TO SEE CONVERSION FROM OCTAL TO DECIMAL")
     print("TYPE h TO SEE CONVERSION FROM HEXADECIMAL TO DECIMAL")
     p=input("PLEASE ENTER YOUR CHOICE::")
     if p == "b":
          v=input("PLEASE ENTER BINARY NUMBER::")
          print((int(v,2))," in Decimal")
     elif p == "o":
          v = input("PLEASE INPUT OCTAL NUMBER")   
          print((int(v,8))," in Decimal")
     elif p == "h":
          v=input("PLEASE ENTER HEXADECIAML NUMBER::")  
          print((int(v,16))," in Decimal")
     else:
          print("PLEASE ENTER A RIGHT CHOICE!!!")
else:
     print("PLEASE ENTER A RIGHT CHOICE!!!!")