

import csv
import time

startcsv = time.time()
with open("stastic.csv",mode="r") as mydataset:
    csvreader = csv.reader(mydataset)
    row = []
    for i in csvreader:
        row.append(i)
stopcsv = time.time() 
csvtime = stopcsv - startcsv
print("time required for csv file reading using csv module is :- ",csvtime)

import pandas as pd
import time

startpanda = time.time()
dataset = pd.read_csv("stastic.csv")
row1 = []
for i in dataset:
    row1.append(i)
stoppanda = time.time()
pandatime = stoppanda - startpanda
print("time required for csv file reading using panda module is :- ",pandatime)


