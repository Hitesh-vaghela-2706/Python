# number that divisible by the sum of its digit is known as 
# harshed number ex:- 21 here 2+1=3 and 21 is divisible by three.

num = input("Enter A number : \n")
sum = 0
for i in num :
    sum += int(i)
num = int(num)
if(num % sum == 0):
    print("number is harshed number")
else:
    print("numbre is not harshed number")