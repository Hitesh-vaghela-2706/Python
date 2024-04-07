# write a python program to find occurence of element in ist

# using for loop
A = [2,4,5,5,6,4,5,3,5]
count = 0
x = int(input("enter a number which occurence u want to find"))
for i in A :
    if(i==x):
        count = count + 1
print("occurence of",x,"is",count) 

#using count function
A = [3,3,4,5,6,3,5,3,1]
B = A.count(3)
print("occurence of given number is",B)

# using user define function
def count(list,x):
    return list.count(x)
A = [1,3,5,7,7,3,7,1]
x = 7
print(f"{x} is occured in A is",count(A,x),"times") 