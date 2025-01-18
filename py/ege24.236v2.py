import re
from collections import Counter

f = open('24-235.txt')
s = f.readline().strip()

for _ in range(2):
    s = re.sub(r'(.)\1', r'\1 \1', s)

a = s.split()
m = max(reversed(a), key = len)

print(max(Counter(m).values()))
#print(Counter(m).most_common(1)[0][1])

