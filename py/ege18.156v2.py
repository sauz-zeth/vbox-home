from itertools import permutations

def even(x):
    return x % 2 == 0

def odd(x):
    return x % 2 != 0

n = 0
for p in permutations(range(10), 5):
    if p[4] == 0 or p[0] % 5 != 0: continue

    po = p[1::2]
    pe = p[::2]

    if all(map(even, po)) and all(map(odd, pe)) or all(map(even, pe)) and all(map(odd, po)):
        n += 1

print(n)


