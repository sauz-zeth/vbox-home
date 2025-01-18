from functools import cache

kmin = float('inf')

@cache
def f(n, k = 0):
    global kmin
    if n == 111:
        if k < kmin:
            kmin = k
        return
    if n > 111 or k >= kmin:
        return

    f(n + 1, k + 1)
    f(n + 5, k + 1)
    f(n * 3, k + 1)

f(1)

@cache
def g(n, k):
    if k == 0:
        return n == 111
    if n > 111:
        return 0

    return g(n + 1, k - 1) + g(n + 5, k - 1) + g(n * 3, k - 1)

print(g(1, kmin))
