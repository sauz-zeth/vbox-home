def f(n, k = 0):
    if n <= 3: return k == 6 and n == 3


    if n % 2 == 0:
        return f(n - 1, k + 1) + f(n - 4, k + 1) + f(n // 2, k + 1)
    else:
        return f(n - 1, k + 1) + f(n - 4, k + 1)

print(f(27))
