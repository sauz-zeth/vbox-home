def f(x, y, a):
    fx = (x <= 11) <= (x**2 <= a)
    fy = (y**2 < a) <= (y <= 12)

    return fx and fy

for a in range(1000, -1, -1):
    if all(f(x, y, a) for x in range(1000) for y in range(1000)): break

print(a)


