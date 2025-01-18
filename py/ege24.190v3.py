import re

f = open('24-181.txt')

s = f.readline().strip()

s = re.sub(r'[AEIOUY]', '#', s)

print(max(len(x) for x in s.split('#') if x.count('.') >= 6))
