# dtype returns datatype of array
# there are mainly used datatypes are int8 int16 int32 int64 float64 etc..

import numpy as np 

A = np.array([ [5,7,9],[458,67,42] ])
print(A.dtype) # bye default numpy gives it int32 dtype for this array 
# but if values are higher(like 10ajab etc) then numpy gives it int 64 dtype

# now, if want to give datatype as per our req. we can able to give it
# for example..
A = np.array([1,3,6,7,8.8],dtype = np.float16)
print(A.dtype)

