# using Dataframe[columnname].loc[rowname] we can able to access data
import pandas as pd

A = {
    "state" : ["gujarat","maharastra","rajastan","madhaypradesh","panjab"] ,

    "capital" : ["gandhinagar","mumbai","jaypur","bhopal","chhatishgadh"] ,

    "literacy %" : [80,70,78,92,88] ,

    "temperature" : [32,36,37,31,28] ,

}
B = pd.DataFrame(A)
C = B["state"].loc[2]
print(C) # return value of column state at row with index 2