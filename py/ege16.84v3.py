from functools import cache

@cache
def f(n):
    if n < 2:
        return n

    if n % 2 == 0:
        return f(n // 2) + 1
    else:
        return f(3 * n + 1) + 1

nmax = 0
for i in range(1, 10**7 + 1):
    try:
        n = f(i)
        if n > nmax:
            nmax = n
            inmax = i
    except RecursionError:
        pass

print(nmax, inmax)
