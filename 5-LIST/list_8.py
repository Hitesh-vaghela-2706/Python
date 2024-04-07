# 
A = [1,2,3,2,4,1,8,8]
B = len(A)
C = []
for i in range(0,B) :
    X = A[i]
    D = A.count(X)
    if(D>1 and X not in C):
        for j in range(0,1):
            C.insert(j,X)
print(C)  
for i in C :
    print("occurence of duplicate number ",i,"is",A.count(i))     

#
A = [1,2,3,2,4,1,8,8]
C = []
for i in A :
    D = A.count(i)
    if(D>1 and i not in C):
        C.append(i)
print(C)  
for i in C :
    print(f"occurence of duplicate number {i} is " , A.count(i))

#
A = [1,2,3,2,4,1,8,8]
B = len(A)
C = []
for i in range(0,B) :
    X = A[i]
    D = A.count(X)
    if(D>1 and X not in C):
        C.append(X)
print(C)  
for i in C :
    print("occurence of duplicate number ",i,"is",A.count(i))