import re
p = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
B = 'vhitesh927@gmail.com'
result = re.fullmatch(p,B)
if result:
    print("Valid E-mail")
else:
    print("Invalid E-mail")