import math
import numpy as np
import scipy.integrate as integrate   # help(integrate)
import matplotlib.pyplot as plt


x_range = 1.0
t_range = 0.1
x_points = 100
t_points = 100
C = 1.0
t = np.linspace(0, t_range, num = t_points+1, dtype = float)
x = np.linspace(0, x_range, num = x_points+1, dtype = float)
dt = t[1] - t[0]
dx = x[1] - x[0]
r = (C * dt / dx)**2
u = np.empty((x_points + 1, t_points + 1), dtype = float)
for i in range(x_points):
    u[i,0] = math.sin(2 * math.pi / x_points)
    u[i,1] = 0.9 * math.sin(2 * math.pi / x_points)
u[0,:] = 0.0
u[x_points,:] = 0.0
for j in range(t_points - 1):
    u[1:-1,j+2] = -u[1:-1,j] + 2*u[1:-1,j+1] + r*(u[:-2,j+1] -2*u[1:-1,j+1] + u[2:,j+1])

plt.imshow(u, cmap='hot', interpolation='bilinear')
plt.colorbar()
plt.show()
