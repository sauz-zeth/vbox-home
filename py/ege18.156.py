from itertools import permutations

n = 0
for p in permutations(range(10), 5):
    if p[4] == 0 or p[0] % 5 != 0: continue
    p0, p1, p2, p3, p4 = p
    if (p0 % 2 != 0 and p1 % 2 == 0 and p2 % 2 != 0 and p3 % 2 == 0 and p4 % 2 != 0) or (p0 % 2 == 0 and p1 % 2 != 0 and p2 % 2 == 0 and p3 % 2 != 0 and p4 % 2 == 0):
        n += 1

print(n)


