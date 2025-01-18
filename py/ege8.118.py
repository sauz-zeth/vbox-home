from itertools import permutations


n = 0
for p in set(permutations('АВРОРА', 6)):
    s = ''.join(p)
    if 'АА' not in s and 'РР' not in s:
        n += 1

print(n)
