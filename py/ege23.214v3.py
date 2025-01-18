from functools import lru_cache
import sys

sys.setrecursionlimit(1207)

@lru_cache(None)
def f(n, pn = None, ppn = None, k11 = 0):
    print(n, pn, ppn)
    if n == 600: return k11 > 0
    if n > 600: return 0
    
    k11 += ppn is not None and (n + pn + ppn) % 11 == 0

    return sum(f(x, n, pn, k11) for x in [n + 2, n * 3, n * 4])

print(f(1))
