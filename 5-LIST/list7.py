# Python program to print all positive numbers in a range
# Python program to print all negative numbers in a range

# Python program to print Even Numbers in a List
list1 = [10, 21, 4, 45, 66, 93]
for num in list1:
    if num % 2 == 0:
       print(num, end = " ")


# Python program to print odd Numbers in a List
list1 = [10, 21, 4, 45, 66, 93]
i = 0      
while(i < len(list1)):
    if list1[i] % 2 != 0:
        print(list1[i], end = " ")
    i += 1