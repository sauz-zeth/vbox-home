import re

f = open('ege24.197.txt')
s = f.read().strip()

print(max(map(len, re.findall('(?:ZXY|ZYX)+', s))) // 3)
