import pandas as pd
A = pd.read_csv('csv_files\Abugdata.csv')
print(A.duplicated())
# returns true and false 
# where data is duplicate it returns true

# it is also aplicable to find duplicate data from perticular row
print(A['Calories'].duplicated())