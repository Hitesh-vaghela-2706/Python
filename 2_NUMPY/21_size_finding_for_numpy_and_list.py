import numpy as np

# size of np array is too less than python list
import sys
pythonlist = [1,2,3,4,5]
pysize = sys.getsizeof(4)*len(pythonlist) # 4 is a element of list we can take any of element
print('size of list',pysize)

numpyary = np.array(pythonlist)
npsize = numpyary.itemsize * numpyary.size
print('size of np array',npsize)
#or
print(numpyary.nbytes) # consumed bytes by array