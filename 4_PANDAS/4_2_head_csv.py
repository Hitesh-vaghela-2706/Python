# head is used to access uper(first) rows of data

import pandas as pd 
A = pd.read_csv("csv_files\data.csv")
print(A.head())
# by default it returns first 5 rows but...
# if we want 10 first rows we can write..
print(A.head(10))