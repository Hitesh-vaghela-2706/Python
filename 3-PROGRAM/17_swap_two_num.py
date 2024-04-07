#write a program to exchange two variables...

#type 1 (with temp. variable)
A = 5
B = 4
print(f"before exchange A={A} and B={B}")
temp = A
A = B
B = temp
print(f"after exchange A={A} and B={B}")

#type 2 (without temp. vzriable)
A = 7
B = 8
print(f"before exchange A={A} and B={B}")
A = A+B
B = A-B
A = A-B
print(f"after exchange A={A} and B={B}")

#type 3 one liner swap using unpacking concept
A,B = 5,6
B,A = A,B