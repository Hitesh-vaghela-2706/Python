# mode -the most comman value/ most repetable value

from scipy import stats
A = [3,3,3,5,6,53,6,23,3,4]
B = stats.mode(A)
print(B)