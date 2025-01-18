from itertools import permutations

n = 0
for p in set(permutations('КАБАЛА', 6)):
    s = ''.join(p)
    if 'АА' not in s:
        n += 1

print(n)
