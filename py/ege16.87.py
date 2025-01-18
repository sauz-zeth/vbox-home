from functools import cache

@cache
def f(n):
    if n < 2:
        return 1

    if n % 3 == 0:
        return f(n // 3) + 1
    else:
        return f(n - 2) + 5

n = 0

for i in range(1, 100000 + 1):
    if f(i) == 55:
        n += 1

print(n)
