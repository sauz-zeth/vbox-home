def f(n):
    if n <= 2: return n == 2

    if n > 4:
        return f(n - 1) + f(n - 3) + f(n % 4)
    else:
        return f(n - 1) + f(n - 3)

print(f(22))
