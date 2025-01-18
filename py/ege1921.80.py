from functools import cache

@cache
def f(n):
    if 25 <= n <= 45:
        return (0, -1)
    if n > 45:
        return (0, 1)

    a = [f(n + 1), f(n * 2)]
    an = [t for t in a if t[1] < 0]

    t = min(an) if an else max(a)
    return (t[0] + bool(an), -t[1])

# 19)
for s in range(1, 24 + 1):
    if f(s + 1) == (1, 1) or f(s * 2) == (1, 1):
        print('19)', s)
        break

# 20)
print('20)', *(s for s in range(1, 24 + 1) if f(s) == (2, 1)))
# 21)
print('21)', *(s for s in range(1, 24 + 1) if f(s) == (2, -1)))
