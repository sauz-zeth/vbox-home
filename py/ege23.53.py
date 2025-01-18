from functools import cache

@cache
def f(n):
    if n >= 18: return n == 18
    if n == 16 or n == 15:
        return f(n + 2)

    return f(n + 1) + f(n + 2)

print(f(3))
