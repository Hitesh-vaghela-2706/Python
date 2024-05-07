# by default series get index 0,1,2,3..
# but if we want to give index use index=
# this is also same for numpy series and tuple series

import pandas as pd
A = [1,2,3,4]
B = ["x","y","z","w"]
c = pd.Series(A,index=B)
print(c)


import pandas as pd
A = [1,2,3,4]
try:
    B = pd.Series(A,index=["x","y","z"]) # return error beacause
# lenth of data A and index lenth is not equal
except ValueError as e:
    print("invalid indexes")
B = pd.Series(A,index=["x","y","z","w"])
print(B)