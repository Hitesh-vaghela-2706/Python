import matplotlib.pyplot as plt

days  = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[],color='b',label='eating',linewidth=5)
plt.plot([],[],color='r',label='working',linewidth=5)
plt.plot([],[],color='c',label='playing',linewidth=5)

plt.stackplot(days, sleeping,eating,working,playing,colors=['m','b','r','c'] )

plt.xlabel('x')
plt.ylabel('y')
plt.title('stackpoint graph')
plt.legend()
plt.show()