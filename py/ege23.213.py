from functools import cache

@cache
def f(n, ko = 0):
    ko = ko + 1 if n % 2 != 0 else 0

    if n == 600 and ko < 2:
        return 1
    if n > 600 or ko >= 2:
        return 0

    return f(n + 2, ko) + f(n * 3, ko) + f(n * 4, ko)

print(f(1))
