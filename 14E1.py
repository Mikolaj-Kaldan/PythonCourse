from numba import jit
import numpy as np
import random
@jit(nopython=True)
def monte_pi(i):
    inner = 0
    for n in range(pow(10,i)):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            inner += 1
    return 4 * inner / pow(10,i)
for i in range(1, 6):
    print(monte_pi(i))
