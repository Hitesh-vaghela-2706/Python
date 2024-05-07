# using index= we can able to give our own index names
# bby default index are 0,1,2,3,4...
import pandas as pd

A = {
    "state" : ["gujarat","maharastra","rajastan","madhaypradesh","panjab"] ,

    "capital" : ["gandhinagar","mumbai","jaypur","bhopal","chhatishgadh"] ,

    "literacy %" : [80,70,78,92,88] ,

    "temperature" : [32,36,37,31,28] ,

}
C = ["i","ii","iii","iv","v"]
B = pd.DataFrame(A,index=C)
print(B)