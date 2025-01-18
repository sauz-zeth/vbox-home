from itertools import islice, accumulate
from collections import Counter
from bisect import bisect

f = open('ege26.58.txt')
S, N = map(int, f.readline().split())

files = sorted(map(int, islice(f, N)))

sa = list(accumulate(files))
n = bisect(sa, S)
    
a = files[:n]
b = files[n:]

da = (S - sa[n - 3]) // 2

amax = b[bisect(b, da) - 1]

print(amax, max(Counter(a).values()))
