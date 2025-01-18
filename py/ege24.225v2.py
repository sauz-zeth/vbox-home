import re

f = open('24-225.txt')
s = f.readline().strip()

n = max(int(x) for x in re.split(r'F{2,}', s)[1:-1] if re.fullmatch(r'44\d\d78\d\d\d3', x))

print(sum(int(x) for x in str(n) if int(x) % 2 == 0))
