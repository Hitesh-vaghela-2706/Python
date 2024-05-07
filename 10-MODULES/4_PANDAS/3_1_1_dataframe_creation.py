# dtaframe only created with dictionary
import pandas as pd

A = {
    "state" : ["gujarat","maharastra","rajastan","madhaypradesh","panjab"] ,

    "capital" : ["gandhinagar","mumbai","jaypur","bhopal","chhatishgadh"] ,

    "literacy %" : [80,70,78,92,88] ,

    "temperature" : [32,36,37,45,28] ,

}
B = pd.DataFrame(A)
print(B)
# in this method all list must be a same size otherwise it returns a error
# so if we want to put some value NAN we will have to write NAN at that position
