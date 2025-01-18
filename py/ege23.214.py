from functools import cache


@cache
def f(n, pn = None, ppn = None, k11 = 0):
    if n == 600 and k11:
        return 1
    if n > 600:
        return 0
    
    k11 += ppn is not None and (n + pn + ppn) % 11 == 0
    
    return f(n + 2, n, pn, k11) + f(n * 3, n, pn, k11) + f(n * 4, n, pn, k11)

print(f(1))
