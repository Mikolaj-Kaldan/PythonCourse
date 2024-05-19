import math
import numpy as np
import scipy.integrate as integrate   # help(integrate)
import matplotlib.pyplot as plt


x_range = 1.0
t_range = 0.05
x_points = 100
t_points = 10000
D = 1.0
t = np.linspace(0, t_range, num = t_points+1, dtype = float)
x = np.linspace(0, x_range, num = x_points+1, dtype = float)
dt = t[1] - t[0]
dx = x[1] - x[0]
r = D * dt / (dx * dx)
print(r)
u = np.empty((x_points + 1, t_points + 1), dtype = float)
u[:,0] = np.where(abs(x - 0.5) < 0.1, 1.0, 0.0)
u[0,:] = 0.0
u[x_points,:] = 0.0
for j in range(t_points):
    u[1:-1,j+1] = r*u[:-2,j] + (1-2*r)*u[1:-1,j] + r*u[2:,j]
plt.imshow(u[:,::20], cmap='hot', interpolation='bilinear')
plt.colorbar()
plt.show()
