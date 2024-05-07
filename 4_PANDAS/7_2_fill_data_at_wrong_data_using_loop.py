# if we don't know wrong data's index use for loop
import pandas as pd
A = pd.read_csv('csv_files\Abugdata.csv')
for i in A.index :
    if A.loc[i,'Duration'] > 60 :
        A.loc[i,'Duration'] = 66
print(A)