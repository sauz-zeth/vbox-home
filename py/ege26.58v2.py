from itertools import islice
from collections import Counter

f = open('ege26.58.txt')
s, N = map(int, f.readline().split())

files = sorted(map(int, islice(f, N)))

n = 0
for x in files:
    if s - x < 0: break
    s -= x
    n += 1

a = files[:n]
b = files[n:]

da = (s + sum(a[-2:])) // 2

amax = [x for x in b if x <= da][-1]

print(amax, max(Counter(a).values()))
