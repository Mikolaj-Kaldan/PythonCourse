import numpy as np
import matplotlib.pyplot as plt
n = 100
x = np.random.rand(n)
y = np.random.rand(n)
colors = np.where(x**2 + y**2 < 1, "g", "r")
size = (abs(x) + abs(y))*10.0
plt.scatter(x, y, s=size, c = colors)
plt.show()
