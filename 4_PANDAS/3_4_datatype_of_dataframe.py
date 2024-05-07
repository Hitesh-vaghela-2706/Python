import pandas as pd
A = {
    "name/subject" : ["hitesh","vishvjit","ravi","yagnik"] ,
    "mysql" : [67,56,65,59] , 
    "python" : [65,51,68,47] ,
    "java" : [51,59,49,54] ,
    "c++" : [63,53,69,70]
}
B = pd.DataFrame(A)
print(B)
print(B.dtypes)

print(B.index)
print(B.columns)
print(B.values)
print(B.describe())
del B["java"]
print(B)