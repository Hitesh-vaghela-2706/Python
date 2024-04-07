# Write a program to perform union, intersection, difference, and 
# symmetric difference and membership testing operation for the given sets.

a = {1,3,6,7}
b = {3,8,9,6}
# UNION operation
c = a.union(b) 
print("union operation")
print(c)
# INTERSECTION operation
c = a.intersection(b) 
print("intersection operation")
print(c)
# DIFFERENCE operation
c = a.difference(b) 
print("difference operation")
print(c)
# SYSTEMATIC DIFFERENCE operation
c = a^b
print("systemetic difference operation")
print(c)