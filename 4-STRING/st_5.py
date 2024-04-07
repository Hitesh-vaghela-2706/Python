# Count the Number of matching characters in a pair of string
# hint...
# Input : str1 = 'aabcddekll12@'
#         str2 = 'bb22ll@55k'
# Output : 5
# (i.e. matching characters :- b, 1, 2, @, k)

str1 = "aabcddekll12@"
str2 = "bb2211@55k"
str3 = ""
str4 = ""

for i in str1:
    if i not in str3:
        str3 = str3 + i
print(str3)

for i in str2:
    if i not in str4:
        str4 = str4 + i
print(str4)

count = 0
print("matching Characters are :- ",end="")
for i in str3:
    if i in str4:
        count +=1
        print(i,end=" ")
print("\n Count of total matching characters is :- ",count)