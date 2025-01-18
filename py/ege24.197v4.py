import re

f = open('ege24.197.txt')
s = f.read().strip()

s = re.sub(r'Z(XY|YX)', '.', s)

w = ''

while w in s:
    w += '.'

print(len(w) - 1)

