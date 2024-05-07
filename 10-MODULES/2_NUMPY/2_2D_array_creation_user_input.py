# A basic code for matrix input from user 
import numpy as np
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 

# Initialize matrix 
A = []
print("Enter the entries rowwise:") 

# For user input 
for i in range(R):          # A for loop for row entries 
    B = []
    for j in range(C):      # A for loop for column entries 
        val = int(input("enter a value"))
        B.append(val)
    A.append(B)

print(np.array(A)) 