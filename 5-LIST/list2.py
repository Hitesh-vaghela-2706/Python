# Python program to print all even numbers in a range
# Python program to print all odd numbers in a range

# Python program to print positive Numbers in a List
list1 = [11, -21, 0, 45, 66, -93]
for num in list1:
    if num >= 0:
       print(num, end = " ")

# Python program to print negative Numbers in a List
list1 = [-10, 21, -4, -45, -66, 93]
num = 0    
while(num < len(list1)):
    if list1[num] < 0:
        print(list1[num], end = " ")
    num += 1