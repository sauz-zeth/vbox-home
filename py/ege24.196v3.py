import re

f = open('ege24.196.txt')
s = f.read().strip()

print(max(map(len, re.findall('(?:Z[XY])+', s))) // 2)
