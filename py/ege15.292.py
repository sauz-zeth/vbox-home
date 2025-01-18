def f(x, y, a):
    return y + 2 * x < a or x > 20 or y > 40

for a in range(-100, 100):
    if all(f(x, y, a) for x in range(1, 100) for y in range(1, 100)): break

print(a)
