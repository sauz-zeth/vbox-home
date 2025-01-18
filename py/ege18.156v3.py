from itertools import permutations

def ok(f, a):
    return all(map(f, a))

def even(x):
    return x % 2 == 0

def odd(x):
    return x % 2 != 0

n = 0
for p in permutations(range(10), 5):
    if p[4] == 0 or p[0] % 5 != 0: continue

    po = p[1::2]
    pe = p[::2]

    if ok(even, po) and ok(odd, pe) or ok(even, pe) and ok(odd, po):
        n += 1

print(n)


