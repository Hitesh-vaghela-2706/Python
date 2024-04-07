# PROGRAM 22 :-
# Write a program to create a dictionary from string 
# in which individual character is key and its count in string is value of key.

from collections import defaultdict, Counter
str1 = 'hiteshvaghela' 
my_dict = {} 
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)

# using dictionary comprihension
A = "hiteshvaghela"
d = {i:A.count(i) for i in A}
print(d)

# using for loop...
A = "hiteshvaghela"
X = {}
for i in A:
    X[i] = A.count(i)
print(X)

# without using any built-in fuctions...

def count_char(ch1,str):
    l = len(str)
    cnt = 0
    for i in range(l):
        if(str[i]==ch1):
            cnt += 1
    return cnt
A = "hiteshvaghela"
X = {}
for i in A:
    X[i] = count_char(i,A)
print(X)