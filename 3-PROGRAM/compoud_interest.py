# A = P(1+R/100)^N

P = eval(input("enter a principal amount :- \n"))
R = eval(input("enter a rate of interest :- \n"))
N = eval(input("entwer a number of years :- \n"))
B = 1 + R/100
C = B**N
A = P*C
print("compound interest is :- ",A)