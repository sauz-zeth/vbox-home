from functools import cache

@cache
def f(n):
    if n == 111:
        return 0
    if n > 111:
        return float('inf')

    return min(f(n + 1), f(n + 5), f(n * 3)) + 1

kmin = f(1)
print(kmin)

@cache
def f(n, k = 0):
    if k == kmin:
        return n == 111
    if n > 111:
        return 0

    return f(n + 1, k + 1) + f(n + 5, k + 1) + f(n * 3, k + 1)

print(f(1))
