# Write a program to count number of vowels using sets in given string 

def vowel_count(str):  
    count = 0 
    vowel_set = set("aeiouAEIOU") 
    for i in str: 
        if i in vowel_set: 
            print(i,end=",")
            count = count + 1
    print("\nnumber of vowel is :- ",count)
str = "hiteshvaghela"
vowel_count(str)

def vowel_count(str):  
    count = 0 
    vowel_string = "aeiouAEIOU"
    for i in str: 
        if i in vowel_string: 
            print(i,end=",")
            count = count + 1
    print("\nnumber of vowel is :- ",count)
str = "hiteshvaghela"
vowel_count(str)

def vowel_count(str):  
    count = 0 
    vowel_list = list("aeiouAEIOU")
    for i in str: 
        if i in vowel_list: 
            print(i,end=",")
            count = count + 1
    print("\nnumber of vowel is :- ",count)
str = "hiteshvaghela"
vowel_count(str)