# using DataFrame.loc[rowname] we can able to access data
# but
# when we want more thqan one row at a time we will use..
# DataFrame.loc[[r1,r2,r3]] etc...
import pandas as pd

A = {
    "state" : ["gujarat","maharastra","rajastan","madhaypradesh","panjab"] ,

    "capital" : ["gandhinagar","mumbai","jaypur","bhopal","chhatishgadh"] ,

    "literacy %" : [80,70,78,92,88] ,

    "temperature" : [32,36,37,31,28] ,

}
B = pd.DataFrame(A)
C = B.loc[[2,3,4]]
print(C) # returns whole data of r2 r3 r4