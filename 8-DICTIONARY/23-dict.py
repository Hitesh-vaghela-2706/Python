# PROGRAM 23 :-
# Write a program to create a dictionary of students’ mid semester marks
# of semester-5 subjects(subject name is key and marks is value) 
# and display it according to descending order of marks(value). 

A = {   "ADA" : 56 ,
        "CN" : 48 ,
        "PE" : 64 ,
        "IPDC" : 54 ,
        "PDS" : 66 ,
        "SE" : 51
    }
A.popitem() # it removes last item which we entered in list
# print(A.popitem())
print("\nAfter popitem operation \t",A)

A.pop("IPDC") # it removes item which key we provided
# print(A.pop("SE"))
print("After pop operation       \t",A)

A["CN"] = 100
print("After changing element        \t",A) # Dictionary is mutable data structure in python

#Assending order
sortbyvalue = {  k:v for (k,v) in sorted(A.items() , key = lambda v:v[1])  }
print("Sorting in Assending order \t",sortbyvalue)

#desending order
sortbyvalue = {  k:v for k,v in sorted(A.items() , key = lambda v:v[1] , reverse=True )  }
print("Sorting in Desending order \t", sortbyvalue)
print("\n")
