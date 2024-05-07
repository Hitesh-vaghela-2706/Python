import pandas as pd
A = pd.read_csv('csv_files\Abugdata.csv')
# here in this data at index 7 in duration is 450 but it is wrong
# we want to replace it with 45
A.loc[7,'Duration'] = 45
print(A)