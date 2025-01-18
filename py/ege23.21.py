def f(n):
    if n >= 51: return n == 51

    if n % 10 == 9:
        return f(n + 1) + f(n + 10)

    else:
        return f(n + 1) + f(n + 11)

print(f(25))
