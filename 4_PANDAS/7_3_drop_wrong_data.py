# also we will able to remove wrong data using drop
import pandas as pd
A = pd.read_csv('csv_files\Abugdata.csv')
for i in A.index:

    if A.loc[i,'Duration']>60:
        A.drop(i,inplace=True)
        print(A)