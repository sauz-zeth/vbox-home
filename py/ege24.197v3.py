import re

f = open('ege24.197.txt')
s = f.read().strip()

print(max(map(len, (m[0] for m in re.finditer('(ZXY|ZYX)+', s)))) // 3)
