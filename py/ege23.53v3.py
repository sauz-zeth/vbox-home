from functools import cache

@cache
def f(n, k = 0):
    if n <= 3: return n == 3
    
    if k == 1:
        return f(n - 2, k + 1)
    else:
        return f(n - 1, k + 1) + f(n - 2, k + 1)

print(f(18))
