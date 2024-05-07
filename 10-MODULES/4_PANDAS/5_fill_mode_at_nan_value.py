import pandas as pd
A = pd.read_csv("csv_files\Abugdata.csv")
B = A['Calories'].mode() [0]
# print(B) # returns mode of Calories
A['Calories'].fillna(B,inplace=True)
print(A)