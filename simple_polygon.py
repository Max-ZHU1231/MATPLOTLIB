import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y,'ro-',label = 'line 1')

plt.title('simple plot')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.legend(loc = 'upper right')

plt.show()