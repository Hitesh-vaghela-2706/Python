import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [5,6,5,8]

plt.plot(x,y,linewidth='1',label='graph(x,y)',marker='D',ms=4,color='g')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('graph of line\ncheck it')
plt.legend()
plt.grid()
plt.show()