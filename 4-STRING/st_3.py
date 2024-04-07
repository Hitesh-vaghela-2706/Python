# snake case each word seperated with underscore 
# ex vaghela_hitesh_rameshbhai

# camel case means first letter of first word is small all other words first letter is capital 
# ex vaghelaHiteshRameshbhai

# pascal case all words first letter is capital
# ex VaghelaHiteshRameshbhai

# Convert Snake case to Pascal case
test_str = 'hitesh_is_good_boy'
print("The original string is : " + test_str)
# Convert Snake case to Pascal case
# Using title() + replace()
res = test_str.replace("_", " ").title().replace(" ", "")
print("The String after changing case : " + str(res)) 

# covert snake case to camel case
string1 = "hitesh_loves_coding"
print("original string " , string1)
temp = string1.replace("_"," ").title().replace(" ","")
temp1 = ""
for i in range(len(temp)):
    if i == 0:
        temp1 += temp[i].lower()
    else:
        temp1 += temp[i]
print(temp1)