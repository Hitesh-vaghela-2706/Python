import pandas as pd
A = pd.read_csv('csv_files\Abugdata.csv')
A.drop_duplicates(inplace=True)
print(A)