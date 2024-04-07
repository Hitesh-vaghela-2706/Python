# PROGRAM 21 :-
# Write a program to create a dictionary of student details 
# and perform basic operation on it.

student_dict = {
    "hitesh" : ("vaghela","computer engineering","sem 5",190280107153) ,
    "vishvjit" : ("vaghela", "compute engineering","sem 5",190280107155) ,
    "chirag" : ("chauhan","electrical engineering","sem 7",180207110134) ,
    "vraj" : ("mistry","mechenical engineering","sem 3",210516104123)
}

# accesing paricular value from multiple values
A = []
for i in list(student_dict.values()) :
    i = list(i)
    print(i[3])
    A.append(i[3])
print(A)

# accessing keys without keys() method
for i in student_dict:
    print(i)
# crreating A list of keys
key = [i for i in student_dict]
print(key)

# accesing Values without values() method
for i in student_dict:
    print(student_dict[i])#returns a tuples of each set of value
# Creating A list of Values
value = [list(student_dict[i]) for i in student_dict]
print(value)
# accesing paricular value from multiple values
M = []
for i in range(len(value)):
    M.append(value[i][3])
print(M)

# printing keys...
A = student_dict.keys()
print("\n keys are.... \n" , A)
Y = list(A)
print("\n keys are.... \n" , Y[3])


# printing values...
B = student_dict.values()
print("\n Values are.... \n" , B)
X = list(B)
print("\n Values are.... \n" , X[0][3])


# printing items...
C = student_dict.items()
print("\n items are.... \n" ,C)


# sorting by key...
sort_by_key = {key:value for key,value in sorted(student_dict.items()) }
print("sort_by_key :- " ,sort_by_key)