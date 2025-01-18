from functools import cache


@cache
def f(n, c = 0):
    if n >= 20: return n == 20

    if c == 2:
        return f(n + 1, 1) + f(n * 2, 3)
    else:
        return f(n + 1, 1) + f(n + 3, 2) + f(n * 2, 3)


print(f(2))
