from itertools import pairwise

f = open('24-181.txt')
s = f.readline().strip()

a = map(len, s.split('.'))

print(max(map(sum, pairwise(a))) + 1)
