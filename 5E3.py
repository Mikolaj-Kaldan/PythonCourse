import random
def random_walk(start):
    pos = start
    for x in range(100):
        pos += random.choice([-1, 1])
    return pos
while True:
    print(random_walk(0))
