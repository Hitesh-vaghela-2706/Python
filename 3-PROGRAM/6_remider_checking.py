# write a python program to find reminder of two divided number 
# write a python program to check wheather a given number is divideable or not
A = int(input("enter a number"))
B = int(input("dividend"))
print(f"reminder of {A} divide by {B} is :- ",A%B)
print("reminder of",A,"/",B,"is",A%B )
if(A%B==0):
    print("number is dividable")
else:
    print("number is not dividable")
