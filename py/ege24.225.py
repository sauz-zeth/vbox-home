import re

f = open('24-225.txt')
s = f.readline().strip()

s = s.replace('FF', 'F*F').replace('FF', 'F*F')

# FFFF
# F*FF*F
# F*F*F*F

n = max(int(x[1:-1]) for x in s.split('*')[1:-1] if re.fullmatch(r'F44\d\d78\d\d\d3F', x))

print(sum(int(x) for x in str(n) if int(x) % 2 == 0))
