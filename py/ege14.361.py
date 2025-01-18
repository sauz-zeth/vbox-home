n = 0
for x in range(6, 100):
    a = x**4 + 3 * x**3 + x**2 + 5 * x + 2
    b = 7 * 100**3 + x * 100**2 + 2 * 100 + 5
    l = a + b
    if l % 11 == 0:
        n += 1

print(n)
