from functools import cache

@cache
def f(x, y, z):
    if x + y + z >= 73:
        return 0

    a = []
    for k in [3, 13, 23]:
        a.append(f(x + k, y, z))
        a.append(f(x, y + k, z))
        a.append(f(x, y, z + k))

    a_ = [x for x in a if x <= 0]

    return -max(a_) + 1 if a_ else -max(a)

def ok19(s):
    for k in [3, 13, 23]:
        if f(2 + k, s, 2 * s) == 1 or f(2, s + k, 2 * s) == 1 or f(2, s, 2 * s + k) == 1:
            return True
    return False

def ok21(s):
    a = set()
    for k in [3, 13, 23]:
        a.update([f(2 + k, s, 2 * s), f(2, s + k, 2 * s), f(2, s, 2 * s + k)])

    return 1 in a and 2 in a

# 19
print('19)', min(filter(ok19, range(1, 23 + 1))))

# 20
print('20)', min(s for s in range(1, 23 + 1) if f(2, s, 2 * s) == 2), end = ' ')
print(max(s for s in range(1, 23 + 1) if f(2, s, 2 * s) == 2))

# 21
print('21)', *(filter(ok21, range(1, 23 + 1))))
