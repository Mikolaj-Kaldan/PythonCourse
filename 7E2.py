import itertools
import random
it_a = itertools.cycle([0,1])
class rand_iter:
    def __iter__(self):
        self.a = random.choice([0, 1])
        return self
    def __next__(self):
        x = self.a
        self.a = random.choice([0, 1])
        return x
it_b = iter(rand_iter())
it_c = itertools.cycle([0,1,0,-1])
