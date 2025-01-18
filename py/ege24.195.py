import re

f = open('24-191.txt')
s = f.readline().strip()
print(sum(1 for x in re.finditer(r'A[^ABF]*F[^ABF]*F[^ABF]*B', s) if len(x[0]) >= 20))
