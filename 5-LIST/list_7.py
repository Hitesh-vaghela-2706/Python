# write a python program to get marks of n student and sort it
# also sort in decresing order
A = int(input("how many students mark you want to enter"))
i = 0
B = []
for i in range(0,A):
    B.insert(i,int(input("enter a marks")))
print(B)   
print(sorted(B))
C = sorted(B)
C.reverse()
print(C)