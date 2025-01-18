import re
from collections import Counter

f = open('24-235.txt')
s = f.readline().strip()

a = re.split(r'(?<=(.))\1*(?=\1)', s)
m = max(reversed(a), key = len)

print(max(Counter(m).values()))
