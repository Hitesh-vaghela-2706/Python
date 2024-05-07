# it is better to fill mean value rather than random 
# value so we find mean value and fill it

import pandas as pd
A = pd.read_csv("csv_files\Abugdata.csv")
B = A['Calories'].mean()
# print(B) returns mean of Calories
A['Calories'].fillna(B,inplace=True)
print(A)