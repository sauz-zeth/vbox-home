def f(x, y, a):
    return 3 * y + 2 * x != 130 or 3 * x > a or 2 * y > a

for a in reversed(range(200)):
    if all(f(x, y, a) for x in range(200, 0, -1) for y in range(200, 0, -1)):
        print(a)
        break
