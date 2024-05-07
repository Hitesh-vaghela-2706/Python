import matplotlib.pyplot as plt
x = [1,2,3,4,5,5,6]
y = [2,5,6,9,6,8,4]

plt.scatter(x,y,label='skitskat')#,color='pink',marker='*',s=40)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('scatter graph')
plt.legend()
plt.show()