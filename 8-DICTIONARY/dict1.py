STUDENT = 3

S_enroll = []
for i in range(1,STUDENT+1):
    X = int(input("enter a enrollment number :- "))
    S_enroll.insert(i,X)

S_name = []
for i in range(1,STUDENT+1):
    Y = input("enter a student name :- ")
    S_name.insert(i,Y)

S_SPI = []
for i in range(1,STUDENT+1):
    Z = float(input("enter a SPI of student :- "))
    S_SPI.insert(i,Z)

SI = list( zip(S_name,S_SPI) )
print(SI)
sdict = dict(zip(S_enroll,SI))
print("dictionary of student ",sdict)