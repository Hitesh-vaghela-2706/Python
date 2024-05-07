import pandas as pd
A = pd.read_csv("csv_files\Abugdata.csv")
B = A.dropna()
# dropna used to drop every row where data is null
# drop is used to drop perticular row
print(B)
# here there is no change in original data but...
# if we want to change original data
B = A.dropna(inplace=True)
print(A)