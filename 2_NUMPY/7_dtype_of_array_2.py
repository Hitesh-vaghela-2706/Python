# dtype returns datatype of array
# there are mainly used datatypes are int8 int16 int32 int64 float64 etc..
# this is the second way to give datatpye
import numpy as np 

A = np.array([ [5,7,9],[458,67,42] ])
print(A.dtype) # bye default numpy gives it int32 dtype for this array 
# but if values are higher(like 10ajab etc) then numpy gives it int 64 dtype

# now, if want to give datatype as per our req. we can able to give it
# for example..
A = np.array([1,3,6,7,8.8],dtype ="float64")
print(A.dtype)

# other datatypes in numpy

# int16 
# int32 
# int64 also write _int64
# int8 
# uint16 
# uint32 
# uint64 
# uint8
# float16 
# float32 
# float64 also write _float
# complex64 
# complex128 also write _complex