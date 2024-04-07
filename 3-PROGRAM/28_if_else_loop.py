Marks = int(input("enter your marks"))
if(Marks>100):
    print("invalid marks")
else:    
    if(Marks>90 and Marks<=100): 
        print("A grade")
    elif(Marks<=90 and Marks>80):
        print(" B grade")
    elif(Marks<=80 and Marks>70):
        print("C grade")
    elif(Marks<=70 and Marks>60):
        print("D grade")
    elif(Marks<=60 and Marks>50):
        print("E grade")
    elif(Marks<=50 and Marks>33):
        print("F grade")
    else:
        print("failed")          