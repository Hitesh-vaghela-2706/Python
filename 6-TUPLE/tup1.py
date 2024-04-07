# Create a tuple to store value of student’s 
# marks of pds subject and display it.

A = int(input("enter total number of students :- "))
B = []
for i in range (0,A):
    marks = int(input("enter a marks of pds subject :- "))
    B.insert(i,marks)
    print(B)
    C = tuple(B)
print(C)
