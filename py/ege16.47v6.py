from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 3:
        return n

    if n % 2 == 0:
        return f(n - 1) + 2 * f(n // 2)
    else:
        return f(n - 1) + f(n - 3)

for n in range(1, 100):
    if f(n) >= 10**8:
        print(n - 1)
        break
