from itertools import permutations
from math import prod

alpha = '4' * 5 + '1' * 5

summ = 0

for p in set(permutations(alpha.encode())):
    s = bytearray(p)

    if b'11' in s: continue

    if s[0] == ord('4'):
        s[0] = ord('3')

    pr = prod(map(int, s.decode()))
    summ += pr

print(summ)
