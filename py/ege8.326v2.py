from itertools import combinations


summ = 0

for c in combinations(range(12), 5):
    a = ['e'] * 12

    for i in c:
        a[i] = 'o'

    s = ''.join(a)

    if 'oo' in s: continue

    if a[0] == 'e':
        summ += 3 * 4**11
    else:
        summ += 4**12

print(summ)
