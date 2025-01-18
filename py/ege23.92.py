def f(n, e):
    if n >= e: return n == e

    return f(n + 1, e) + f(n + 3, e) + f(n * 2, e)

print(f(3, 9) * f(9, 12) * f(12, 20))
