# armstrong number in list
strtrng = int(input("enter a range"))
endrng = int(input("enter a range"))
# sum = 0 here write is give error because at every time loop executes
# sum is not becoming 0
for num in range(strtrng,endrng):
    order = len(str(num))
    sum = 0
    temp=num
    while temp>0:
        digit=temp%10
        sum += digit**order
        temp//=10
    if num==sum:
        print(num,end=',')

 