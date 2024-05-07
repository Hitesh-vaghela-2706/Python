# csv is nothing but a exel file

# csv means comma separated files

import pandas as pd

A = pd.read_csv('csv_files\data.csv')
# here full path given bcz both files are at different folders
# but if both in same folder no need to give path give only name
# for example...  df = pd.read_csv('data.csv') 
print(A) 
# data of csv file is large so it shows only  
# first and last 5 rows of data