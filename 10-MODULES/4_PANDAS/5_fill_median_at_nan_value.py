# it is better to fill mean value rather than random 
# value so we find mean value and fill it

import pandas as pd
A = pd.read_csv("csv_files\Abugdata.csv")
B = A['Duration'].median()
# print(B) # returns median of Calories
A['Duration'].fillna(B,inplace=True)
print(A)