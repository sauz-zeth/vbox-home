from functools import cache

@cache
def f(n, k = 0):
    if n == 80 and k <= 5:
        return 1
    if n > 80 or k > 5:
        return 0

    return f(n + 1, k + 1) + f(n * 2, k + 1) + f(n + n % 4, k + 1)

print(sum(f(i) != 0 for i in range(1, 81)))
