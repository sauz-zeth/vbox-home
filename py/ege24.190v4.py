import re

f = open('24-181.txt')
s = f.readline().strip()

print(max(len(x) for x in re.split(r'[AEIOUY]', s) if x.count('.') >= 6))
