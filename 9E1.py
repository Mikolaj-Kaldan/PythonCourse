import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10,1000)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_exp = np.exp(-x)
plt.plot(x, y_sin, "r-", label = "sin(x)")
plt.plot(x, y_cos, "g--", label = "cos(x)")
plt.plot(x, y_exp, "b:", label = "exp(-x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
