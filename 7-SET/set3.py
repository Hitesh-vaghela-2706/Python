# creating a empty set of student enrollment
students_enrollmant = set()

# add student enrollment in set
A = int(input("enter a number of students :- "))
for i in range (0,A):
    B =  int(input("enter a enrollment"))
    students_enrollmant.add(B)
print(students_enrollmant)
