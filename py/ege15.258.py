def f(x, y, a):
    fx = (x >= 11) <= (x * x + 2 * x > a)
    fy = (y * y + 3 * y >= a) <= (y > 8)

    return fx and fy

n = 0
for a in range(-1000, 1000):
    if all(f(x, y, a) for x in range(100) for y in range(100)):
        n += 1

print(n)


