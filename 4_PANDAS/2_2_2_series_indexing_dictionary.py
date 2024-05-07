# in dictionary key is counted as index
# if you try to give your own index it return error
import pandas as pd

A = {
    "physics" : 89 ,
    "english" : 78 ,
    "sanskrit" : 91 ,
    "chemistry" : 93 ,
    "maths" : 95
}
print(pd.Series(A))

C = [1,2,3,4,5]
B = pd.Series(A,index=C)
print(B) # returns nan because ones index is set 
# we can't able to change it.
