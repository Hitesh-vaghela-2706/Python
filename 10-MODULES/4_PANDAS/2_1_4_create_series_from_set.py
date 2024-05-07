import pandas as pd
 
A = {1,2,3,4,5,6}
try:
    B = pd.Series(A)
    print(B)
except TypeError as t:
    print(t)
    print("can't create series from set")