from functools import cache

@cache
def f(n):
    print(n, end = ' ')
    if n < 2:
        return n

    if n % 2 == 0:
        return f(n // 2) + 1
    else:
        return f(3 * n + 1) + 1

n = 0
for i in range(1, 100 + 1):
    try:
        if f(i) > 100:
            n += 1
        print()
    except RecursionError:
        pass

print(n)
