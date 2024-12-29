import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X1 = np.array([5,5.5,6,6.5,7,7.5,8,8.5]).reshape(-1,1)
y1 = np.array([900,880,840,800,740,680,650,650])

X2 = np.array([5,5.5,6,6.5,7,7.5,8,8.5,9.5]).reshape(-1,1)
y2 = np.array([900,880,840,800,740,680,650,650,900])


model1 = LinearRegression()
model1.fit(X1, y1)
X_new1 = np.array([[5], [9.5]]) 
y_predict1 = model1.predict(X_new1)



model2 = LinearRegression()
model2.fit(X2, y2)

X_new2 = np.array([[5], [9.5]]) 
y_predict2 = model2.predict(X_new1)


plt.scatter(X1, y1, color='blue', label='Data set 1')
plt.plot(X_new1, y_predict1, color='red', label='Regression Straight Line 1')

plt.scatter(X2, y2, color='green', label='Data set 2')
plt.plot(X_new2, y_predict2, color='orange', label='Regression Straight Line 2')

plt.xlabel('X')
plt.ylabel('y')
plt.title('Regression Straight Line')
plt.legend()
plt.grid()


plt.show()