def f(n):
    if n >= 15: return n == 15
    if n == 8: return 0
    
    return f(n + 1) + f(n + 2) + f(n + 3)

print(f(3))

