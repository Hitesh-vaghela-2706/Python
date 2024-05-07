# using DataFrame.loc[rowname] we can able to access data
import pandas as pd

A = {
    "state" : ["gujarat","maharastra","rajastan","madhaypradesh","panjab"] ,

    "capital" : ["gandhinagar","mumbai","jaypur","bhopal","chhatishgadh"] ,

    "literacy %" : [80,70,78,92,88] ,

    "temperature" : [32,36,37,31,28] ,

}
B = pd.DataFrame(A)
C = B.loc[2]
print(C) # returns whole data of row with index two