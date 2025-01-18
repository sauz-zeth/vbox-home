from functools import cache

@cache
def f(n, k = 0):
    if n == 227: return 0
    if n > 227: return float('inf')

    return min(f(n + 1, k + 1), f(n + 5, k + 1), f(n * 3, k + 1)) + 1

print(f(1))
