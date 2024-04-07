# remove i’th character from string in Python

# first method
test_str = "HiteshVaghela"
print ("The original string is : " + test_str)
new_str = ""
for i in range(len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]
print ("The string after removal of i'th character : " + new_str)

# second method
A = "HiteshVaghela"
B = A.replace(A[2],"")
print(B)