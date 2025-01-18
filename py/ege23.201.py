from functools import cache

@cache
def f(n, e = 0):
    if n == 402 and e <= 2:
        return 1
    if n > 402 or e > 2:
        return 0 

    e += n % 2 == 0
    return f(n + 2, e) + f(n * 2, e) + f(n * 3, e)

N = 1
print(f(N, -(N % 2 == 0)))

