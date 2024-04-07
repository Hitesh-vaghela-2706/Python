square = lambda X : X*X
A = [1,3,5]
# want to create a list of A list square list

# method 1
B = []
for i in A :
    B.append(square(i))
print(B)

# method 2
B = list(map(square,A))
print(B)