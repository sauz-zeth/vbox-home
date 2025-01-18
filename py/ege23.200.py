from functools import cache

@cache
def f(n, d = 0):
    if n == 472: return d > 0
    if n > 472: return 0

    return f(n + 3, d - 1) + f(n * 2, d + 1) + f(n * 7, d + 1)

print(f(2))
