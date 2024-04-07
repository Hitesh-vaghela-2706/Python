V = int(input("enter Total No. of Vehicle\n"))
W = int(input("Enter Total No. of Wheels\n"))
if(V>W or W<2 or W %2!=0):
    print("INVALID INPUT")
else:
    max2wheel = int(W/2) # possible maximum two wheels
    max4wheel = int(W/4) # possible maximum four wheels
    for i in range(0,max2wheel):
        for j in range(0,max4wheel):
            if((2*i + 4*j == W) and (i+j == 200) ): # checking for condition match
                print(f"two wheels {i} four wheels {j}")