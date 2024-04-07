# fibonachi series
n1 = 0
n2 = 1

number = int(input("Enter a Range  :-  ")) - 2
print(n1,end=',')
print(n2,end=',')

for i in range (number):
    n3 = n1 + n2
    print(n3,end=',')
    n1 = n2
    n2 = n3
print('...')


 # fibonachi series swaping without temporary
n1,n2 = 0,1
number = int(input("Enter a Range  :-  ")) - 2
print(n1,end=',')
print(n2,end=',')
for i in range (number):
    n1,n2  = n2,n1+n2
    print(n2,end=',')
print('...')