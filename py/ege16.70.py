from functools import cache

@cache
def f(n):
    if n == 0:
        return 1

    if n > 0:
        return 2 * f(1 - n) + 3 * f(n - 1) + 2
    elif n < 0:
        return -f(-n)

print(sum(int(x) for x in str(f(50))))
