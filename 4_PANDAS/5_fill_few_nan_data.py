import pandas as pd
A = pd.read_csv("csv_files\Abugdata.csv")
B = A["Calories"].fillna(144)
print(B)
A['Duration'].fillna(60,inplace=True)
print(A)