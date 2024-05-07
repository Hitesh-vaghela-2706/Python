# percentile()
# 75 percentile means 1 value which is grater than 75 % values
#for ex...
import numpy as  np
ages = [3,5,7,9,23,45,56,34,23,67,32,42,21,54,65,76,89]
A = np.percentile(ages,75)
print(A)
#output is 56 it means 75% of peoples have less age than 56