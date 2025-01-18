from functools import cache

@cache
def f(x, y):
    if x + y >= 77:
        return 0

    a = [f(x + 1, y), f(x * 2, y), f(x, y + 1), f(x, y * 2)]
    a_ = [t for t in a if t <= 0]

    return -max(a_) + 1 if a_ else -max(a)

# 19
for s in range(1, 69 + 1):
    if f(7, s * 2) == 1 or f(7, s + 1) == 1 or f(7 * 2, s) == 1 or f(7 + 1, s) == 1:
        print('19)', s)
        break

# 20
print('20)', end = ' ')
for s in range(1, 69 + 1):
    if f(7, s) == 2:
        print(s, end = ' ')
print()

# 21
for s in range(1, 69 + 1):
    if f(7, s) == -2:
        print('21)', s)
        break

