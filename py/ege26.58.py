from itertools import islice
from collections import Counter

f = open('ege26.58.txt')
S, N = map(int, f.readline().split())

files = sorted(map(int, islice(f, N)))

a = []
s = 0
n = 0
for x in files:
    if s + x > S: break
    s += x
    n += 1

a = files[:n]
b = files[n:]

da = (S - sum(a[:-2])) // 2

for x in b:
    if x > da: break
    amax = x

print(amax, Counter(a).most_common(1)[0][1])
