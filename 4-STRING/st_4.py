# Find length of a string in python

# using len function
str = "lover"
print(len(str))

# using for loop
str1 = "Hitesh"
lenght = 0
for i in str1:
    lenght += 1
print(lenght)
  
# using Function
def findLen(str):
    counter = 0    
    for i in str:
        counter += 1
    return counter

str = "vaghela"
print(findLen(str))