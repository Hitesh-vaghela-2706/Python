i = 0
A = int(input("enter range:- "))
print("odd number is :- ")
for i in range(A) :
    if i%2!=0:
        print(i,end=",")

print("even number is :- ")
for i in range(A) :
    if i%2 ==0:
        print(i,end=",")
        # i = i + 1