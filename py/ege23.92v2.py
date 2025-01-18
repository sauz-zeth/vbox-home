def f(n, f9 = False, f12 = False):
    if n >= 20: return n == 20 and f9 and f12
    
    if n == 9:
        f9 = True
    if n == 12:
        f12 = True

    return f(n + 1, f9, f12) + f(n + 3, f9, f12) + f(n * 2, f9, f12)

print(f(3))
