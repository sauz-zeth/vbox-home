def f(x, y, a):
    return (2 * y + 5 * x < a) or (2 * x + 4 * y > 100) or (3 * x - 2 * y > 70)

for a in range(200):
    if all(f(x, y, a) for x in range(1, 200) for y in range(1, 200)):
        print(a)
        break
