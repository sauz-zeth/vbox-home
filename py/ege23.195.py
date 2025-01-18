def f(n, k23 = 0):
    if n == 100 and k23 <= 2:
        return 1
    if n > 100 or k23 > 2:
        return 0

    return f(n + 1, k23) + f(n * 2, k23 + 1) + f(n * 3, k23 + 1)

print(f(1))
