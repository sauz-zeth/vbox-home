from functools import cache


@cache
def f(n, c = 0, pc = 0):
    if c == pc == 2: return 0
    if n >= 20: return n == 20

    return f(n + 1, 1, c) + f(n + 3, 2, c) + f(n * 2, 3, c)

print(f(2))
