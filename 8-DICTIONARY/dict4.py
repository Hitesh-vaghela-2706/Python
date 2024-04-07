A = int(input("enter a number of students"))

name = []
for i in range (1,A+2):
    B = str(input("enter a name"))
    name.insert(i,B)
print(name)
se = []
for i in range (1,A+2):
    if i == 1:
        B = str(input("enter a subject name"))
    else:
        B = int(input("enter a marks"))
    se.insert(i,B)
print(se)
C = dict(zip(name,se))
print(C)