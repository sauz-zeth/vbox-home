from functools import cache

@cache
def f(x, y):
    if x + y >= 62:
        return 0

    a = [f(x + 2, y), f(x * 2, y), f(x, y + 2), f(x, y * 2)]
    a_ = [t for t in a if t <= 0]

    return -max(a_) + 1 if a_ else -max(a)

# 19
for s in range(1, 54 + 1):
    if f(7, s + 2) == 1 or f(7, s * 2) == 1 or f(7 + 2, s) == 1 or f(7 * 2, s) == 1:
        print('19)', s)
        break

# 20
print('20)', min(s for s in range(1, 54 + 1) if f(7, s) == 2))

# 21
print('21)', *(s for s in range(1, 54 + 1) if f(7, s) == -2))
