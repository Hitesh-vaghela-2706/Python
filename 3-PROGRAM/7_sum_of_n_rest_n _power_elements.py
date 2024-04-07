# write a progrma to calculate the sum of the first N numbers with power N

N = int(input("enter a power"))
def N_power_N(n) :
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i**N) 
    return sum
num = int(input("enter a number :-"))
print(N_power_N(num))
