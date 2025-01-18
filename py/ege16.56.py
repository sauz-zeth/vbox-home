from functools import cache

@cache
def f(n):
    if n > 20:
        return n * n * n + n

    if n % 2 == 0:
        return 3 * f(n + 1) + f(n + 3)
    else:
        return f(n + 2) + 2 * f(n + 3)

print(sum(1 for n in range(1, 1000 + 1) if '1' not in str(f(n))))
