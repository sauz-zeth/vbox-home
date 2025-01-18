import re

f = open('24-181.txt')

s = f.readline().strip()

for x in 'AEIOUY':
    s = s.replace(x, '#')

print(max(len(x) for x in s.split('#') if x.count('.') >= 6))
