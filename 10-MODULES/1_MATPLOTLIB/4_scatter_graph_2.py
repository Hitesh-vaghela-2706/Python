import matplotlib.pyplot as plt
import numpy as np
# x = age of car y = speed of car


# day 1
x = np.array([4,6,2])
y = np.array([107,87,120])
plt.scatter(x,y,label='day 1',color='k')

#day 2
# day 1
x = np.array([5,7,4])
y = np.array([150,127,160])
plt.scatter(x,y,label='day 2',color='b')

plt.xlabel("years of cars")
plt.ylabel('speed of cars')
plt.title("cars years vs speeed graph")
plt.legend()
plt.show()