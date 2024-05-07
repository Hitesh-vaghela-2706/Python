# when data is too large and we want to show whole data
# use dataframe.to_string()

import pandas as pd

A = pd.read_csv('csv_files\data.csv') 
print(A.to_string())