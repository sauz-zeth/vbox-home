from functools import cache

@cache
def f(c = 0, pc = 0, k = 0, ko = 0):
    if pc % 2 != 0 and c % 2 != 0: return 0
    if k == 12: return ko == 5

    return sum(f(nc, c, k + 1, ko + nc % 2) for nc in range(k == 0, 8))

print(f())
