import numpy as np
import matplotlib.pyplot as plt

X = np.array([2,5,7,9])
Y = np.array([27,46,39,87])

plt.scatter(X,Y)

SLOPE,INTERCEPT = np.polyfit(X,Y,1)

plt.plot( X , (SLOPE*X)+INTERCEPT )
plt.show()