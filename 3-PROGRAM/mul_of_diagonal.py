A = [[1,2,3],[4,10,6],[7,8,9]]
sum1 = sum2 = 1
row = 0
column = 2
# first diagonal
for i in range(0,3):
    for j in range(0,3):
        if(i==j):
            sum1 *= A[i][j]
# second diagonal
while(row<3):
    for i in range(0,3):
        for j in range(0,3):
            if(i==row and j == column):
                sum2 *= A[i][j]
    row += 1
    column -= 1
# multiplication of diagonals
print(sum1*sum2)        