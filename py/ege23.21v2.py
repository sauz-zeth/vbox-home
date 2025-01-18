def f(n):
    if n >= 51: return n == 51

    return f(n + 1) + f(n + 10 + (n % 10 != 9))

print(f(25))
