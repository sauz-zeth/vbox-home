from itertools import combinations


summ = 0

for c in combinations(range(12), 5):
    a = bytearray(12)

    for i in c:
        a[i] = 1

#    if b'\x01\x01' in a: continue
    if bytes([1, 1]) in a: continue

    summ += 3 * 4**11 if a[0] == 0 else 4**12

print(summ)
