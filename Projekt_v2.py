from numba import jit
import cmath
import time
import numpy as np
import matplotlib.pyplot as plt

x_min = -1.5
y_min = -1
x_max = 0.5
y_max = 1
x_res = 1000
y_res = 1000
max_it = 50
x_width = (x_max - x_min) / x_res
y_width = (y_max - y_min) / y_res

@jit(nopython=True)
def color(p, max_it):
    z = p
    for i in range(max_it):
        z = z*z + p
        if abs(z)>2:
            return False
    return True

start = time.process_time()

matrix = np.empty((y_res,x_res), dtype=bool)

for i in range(y_res):
    for ii in range(x_res):
        point = complex(x_min + x_width * (ii + 0.5), y_max - y_width * (i + 0.5))
        matrix[i,ii] = color(point, max_it)

plt.imshow(matrix)

print(time.process_time() - start)

plt.show()
