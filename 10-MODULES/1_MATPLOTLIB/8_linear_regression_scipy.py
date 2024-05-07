import matplotlib.pyplot as plt
from scipy import stats

X = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18] # age of car
Y = [100,90,80,70,67,66,55,45,40,63,56,98,74,53,23,56,48,87] # speed of car
plt.scatter(X,Y)

slope,intercept,r,p,std_err = stats.linregress(X,Y)
def myfunc(X):
    return slope*X + intercept

A = list(map(myfunc,X))
plt.plot(X,A)
plt.show()

speed = myfunc(23)
print(speed)
print(r)
print(slope)
print(intercept)
print(p)