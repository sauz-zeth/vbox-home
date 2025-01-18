def f(n):
    if n == 16: return 1
    if n > 16: return 0

    return f(n + 1) + f(n * 2)

print(f(1))
