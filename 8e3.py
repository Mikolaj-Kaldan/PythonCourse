import numpy as np
m1 = np.random.randint(10, size=(4, 5))
m2 = m1[0][::-1]
for row in range(1, len(m1)):
    m2 = np.vstack((m2,m1[row][::-1]))
m3 = m1[::-1][0]
for column in range(1, len(m1)):
    m3 = np.vstack((m3,m1[::-1][column]))
m4 = m1[1][1:-1:1]  # m1[1:-1:1][1:-1:1] nie działa
for row in range(2, len(m1)-1):
    m4 = np.vstack((m4,m1[row][1:-1:1]))
