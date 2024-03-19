p = [(-0.8, -0.3), (0.6, 0.7), (0.8, 0.7), (0.7, -1.0), (-0.1, 0.1)]
print(list(filter((lambda p: (False,True)[pow(p[0],2) + pow(p[1],2) <= 1]),p)))
print(list(filter((lambda p: (False,True)[p[0] + p[1] > 0 and p[0]*p[1] > 0]),p)))
p.sort(key = lambda p: (-p[1],p[0]))
print(p)
p.sort(key = lambda p: abs(p[0])+abs(p[1]))
print(p)
