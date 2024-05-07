import pandas as pd
A = pd.read_csv("csv_files\Abugdata.csv")
B = A['Calories'].dropna()
print(B)
A["Duration"].dropna(inplace=True)
print(A) # not working