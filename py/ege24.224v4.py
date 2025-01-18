from itertools import repeat
import re

f = open('24-224.txt')
s = f.readline().strip()

pat = re.compile(r'(BAC|CAB)+')

gm = map(pat.match, repeat(s), range(len(s)))
print(max(len(m[0]) for m in gm if m))
