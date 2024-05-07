# head is used to access lower(last) rows of data

import pandas as pd 
A = pd.read_csv("csv_files\data.csv")
print(A.tail())
# by default it returns last 5 rows but...
# if we want last 10 rows we can write..
print(A.tail(10))