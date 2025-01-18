from functools import cache

@cache
def f(n, e):
    if n <= e: return n == e

    num = min(map(int, str(n).replace('0', '')))

    if n % 4 == 0:
        return f(n - 2, e) + f(n - num, e)
    else:
        return f(n - 2, e) + f(n - num, e) + f(n - n % 4, e)

print(f(96, 64) * f(64, 60))
