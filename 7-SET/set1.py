# Write a program to create a set of students’ enrolment number 
# and sort them and perform add and delete operation on it.

# creating a set of student enrollment
students_enrollmant = {153,155,127,120,125}
print("before any operation set is",students_enrollmant)
# add operation
enroll = int(input("enter a enrollment number"))
students_enrollmant.add(enroll)
print("add enroll 111 in set :-" ,students_enrollmant)
# delete  operation using remove
students_enrollmant.remove(153)
print("remove 153 enroll from set" ,students_enrollmant)
# delete operation using pop
students_enrollmant.pop()
print("remove 1st enroll from set" ,students_enrollmant)