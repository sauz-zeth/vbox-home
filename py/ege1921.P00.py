from functools import cache

@cache
def f(x, y):
    if x + y >= 77:
        return 0

    a = [f(x + 1, y), f(x * 2, y), f(x, y + 1), f(x, y * 2)]
    a_ = [t for t in a if t <= 0]

    return -max(a_) + 1 if a_ else -max(a)

for y in range(1, 99 + 1):
    for x in range(7, 77 + 1):
        print(f(x, y), end = ' ')

    print()
