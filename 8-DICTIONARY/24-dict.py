# PROGRAM 28 :-
# Write a program to list of objects of dictionary of 
# student details sort them according to the SPI of students.

A = {
    190280107153 : ("hitesh" , 8.3,3),
    190280107155 : ("vishvjit" , 7.2,2),
    190280107127 : ("yagnik" , 7.6,1),
    190280107020 : ("ravi" , 7.4,7)
}
# list of object
print(list(A.items()))

# sorted dictionary
sortbySPI = {  v:k for k,v in sorted(A.items() , key = lambda v:v[1][2])  }
print(sortbySPI)