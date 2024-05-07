# using to_datetime() we can able to make data in correct formate

import pandas as pd
A = pd.read_csv('csv_files\Abugdata.csv')
A['Date'] = pd.to_datetime(A['Date'])
print(A)