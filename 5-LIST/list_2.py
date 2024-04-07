# find length of list
# using len function
A = [1,2,3,4,5,6]
print(len(A))


# without len function:-
length = 0
A = [2,6,5,3,8,5,7]
for i in A:
    length +=1
print(length)    

#using user define function
def findlength(list):
    length = 0
    for i in list:
        length += 1
    return length
A = [2,5,7,9,78,56,45,4,34,3]
print(findlength(A))