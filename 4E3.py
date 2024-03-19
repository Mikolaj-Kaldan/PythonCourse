def iter_even():
    i = 0
    while True:
        yield 2*i
        i += 1
def iter_odd():
    i = 0
    while True:
        yield 2*i + 1
        i += 1
def iter_power(k):
    i = 0
    while True:
        yield pow(k,i)
        i += 1
