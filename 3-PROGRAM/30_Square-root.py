# write a program to find root
A = int(input("enter a number"))
for num in range(0,A+1):
    B = num*num
    if(B==A):
        print("root is",num)

# write a program to print square in given rng
A = int(input("enter a range"))
for num in range(0,A+1):
    B = num*num
    print(B,end=",") 
