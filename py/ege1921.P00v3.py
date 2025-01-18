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
    if any(f(*t) == 1 for t in [(7, s * 2), (7, s + 1), (7 * 2, s), (7 + 1, s)]):
        print('19)', s)
        break

# 20
print('20)', *(s for s in range(1, 69 + 1) if f(7, s) == 2))

# 21
print('21)', min(s for s in range(1, 69 + 1) if f(7, s) == -2))
