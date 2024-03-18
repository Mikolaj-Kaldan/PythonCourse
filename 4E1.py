p = ((0.8, 0.3), (0.6, 0.7), (0.8, 0.7), (0.7, 1.0), (0.1, 0.1))
print(list(filter((lambda p: (False,True)[pow(p[0],2) + pow(p[1],2) <= 1]),p)))
