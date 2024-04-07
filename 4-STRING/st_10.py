# check wheather a given string is making 
# palindrom by rearrangeing elements or not
str = input("Enter A string to check   ")
l = list(str)
s1 = set(l)
m = list(s1)
B = [l.count(i) for i in m]
c = 0
for i in B:
    if(i%2 != 0):
        c += 1
if(c>1):
    print("no")
else:
    print("yes")