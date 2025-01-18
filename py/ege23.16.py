from functools import cache

@cache
def f(n):
    if n == 38: return 1
    if n > 38: return 0

    return f(n + 1) + f(n * 2) + f(n ** 2)

print(f(2))

