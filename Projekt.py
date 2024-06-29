import tkinter as tk
from numba import jit
import cmath
import time

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

root = tk.Tk()
Mandel = tk.Canvas(root, bg = "white", height = y_res, width = x_res)

start = time.process_time()

for i in range(y_res):
    for ii in range(x_res):
        point = complex(x_min + x_width * (ii + 0.5), y_max - y_width * (i + 0.5))
        if color(point, max_it):
            Mandel.create_oval(ii, i, ii, i, fill = "black")

print(time.process_time() - start)

Mandel.pack()
root.mainloop()
