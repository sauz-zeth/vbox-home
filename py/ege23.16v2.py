import math

def f(n):
    if n == 2:
        return 2

    if n % 2 == 0 and math.isqrt(n) == math.sqrt(n):
        return f(n - 1) + f(n // 2) + f(math.isqrt(n))

    if n % 2 != 0 and math.isqrt(n) == math.sqrt(n):
        return f(n - 1) + f(math.isqrt(n))

    if n % 2 == 0 and math.isqrt(n) != math.sqrt(n):
        return f(n - 1) + f(n // 2)

    if n % 2 != 0 and math.isqrt(n) != math.sqrt(n):
        return f(n - 1)

print(f(38))

