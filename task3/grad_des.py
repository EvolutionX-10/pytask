import numpy as np
import matplotlib.pyplot as plt

x = np.array([3,4,5,6])
y = np.array([1,2.5,7.8,10])

def grad_des(x,y):
	m = 0
	c = 0
	n = len(x)
	learning_rate = 0.001
	for i in range(100000):
		y_pred = m*x + c
		dm = (-2/n)*sum(x*(y-y_pred))
		dc = (-2/n)*sum(y-y_pred)
		m = m - learning_rate*dm
		c = c - learning_rate*dc
	return m,c

m,c = grad_des(x,y)
print(f"y = {m:.3f}x - {-c:.3f}" if c < 0 else f"y = {m:.3f}x + {c:.3f}")
y_pred = m*x + c
plt.scatter(x,y)
plt.plot(x,y_pred)
plt.show()