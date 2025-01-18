import re

f = open('24-212.txt')

s = f.readline().strip()

print(max(map(len, (m[0] for m in re.finditer(r'([BCD][AO])+', s)))) // 2)
