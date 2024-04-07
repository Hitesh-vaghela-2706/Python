st1 = input("enter first string\n")
st2 = input("enter second string\n")

st1 = sorted(st1.lower())
st2 = sorted(st2.lower())

if(st1 == st2):
    print("string is anagram")
else:
    print("string is not anagram")
#  anagram string means a strings with same charecter sufffled
#  reshma and ramesh are anagram string

