# in dictionary index= is used to aceess elements
import pandas as pd

A = {
    "physics" : 89 ,
    "english" : 78 ,
    "sanskrit" : 91 ,
    "chemistry" : 93 ,
    "maths" : 95
}
B = ["maths","chemistry"]
C = pd.Series(A,index=B)
print(C)