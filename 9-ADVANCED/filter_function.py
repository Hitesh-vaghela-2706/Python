def grater_than_5(num):
    if num > 5 :
        return True
    else :
        return False

list1 = [1,4,5,3,1,6,7,3,2,3,8,6,7]
A = filter(grater_than_5,list1)
B = list(A)
print(B)

g_5 = lambda num : num>5
print( list( filter(g_5,list1) ) )