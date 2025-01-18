def f(n, k = 0):
    if n >= 27: return k == 7 and n == 27

    return f(n + 1, k + 1) + f(n + 4, k + 1) + f(n * 2, k + 1)

print(f(3))
