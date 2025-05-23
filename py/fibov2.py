from functools import cache

@cache
def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return F(n - 1) + F(n - 2)

print(F(50))
