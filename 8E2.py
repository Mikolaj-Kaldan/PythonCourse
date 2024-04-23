import numpy as np
v1 = np.array(np.arange(10))
v2 = []
for x in v1:
    if x%2 == 1:
        v2 = np.concatenate((v2,[v1[x]]))
v3 = v1[::-1]
