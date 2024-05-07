# fillna used to fill data at every row where data is null
# fill is used to fill data at perticular row
import pandas as pd
A = pd.read_csv("csv_files\Abugdata.csv")
B = A.fillna(120)
print(B)
# if we dont want to create another variable we can write..
# A.fillna(120,inplace=True)
# print(A)