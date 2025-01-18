from functools import cache
from math import *

@cache
def f(n):
    if n >= 82:
        return (0, 1)

    a = [f(n + 10), f(n * 2)]
    an = [t for t in a if t[1] < 0]

    t = min(an) if an else max(a)
    return (t[0] + bool(not an), -t[1])

for s in range(1, 100):
    print(s, (f(s)))
