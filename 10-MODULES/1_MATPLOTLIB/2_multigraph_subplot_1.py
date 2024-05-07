import matplotlib.pyplot as plt

x = [1,3]
y = [4,4]
plt.subplot(1,2,1)#(no.of row , no.of column , plot no.)
plt.plot(x,y)

x1 = [2,3]
y1 = [4,6]
plt.subplot(1,2,2)#(no.of row , no.of column , plot no.)
plt.plot(x1,y1)

plt.show()

