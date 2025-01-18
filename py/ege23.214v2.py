from functools import cache

@cache
def f(n, pn = None, ppn = None, k11 = 0):
    print(n, pn, ppn)
    if n == 600: return k11 > 0
    if n > 600: return 0
    
    k11 += ppn is not None and (n + pn + ppn) % 11 == 0

    s = 0
    for x in [n + 2, n * 3, n * 4]:
        s += f(x, n, pn, k11)

    return s

print(f(1))
