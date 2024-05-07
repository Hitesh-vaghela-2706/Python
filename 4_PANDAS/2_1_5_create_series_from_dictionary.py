import pandas as pd

A = {
    "physics" : 89 ,
    "english" : 78 ,
    "sanskrit" : 91 ,
    "chemistry" : 93 ,
    "maths" : 95
}

B = pd.Series(A)
print(B)