from functools import cache

@cache
def f(n, k = 0, c = 0):
    if k == 2 and c == 1: return 0
    if n <= 3: return n == 3
    
    return f(n - 1, k + 1, 1) + f(n - 2, k + 1, 2)

print(f(18))
